from anvil.js.window import document
from anvil.js import get_dom_node, window
from . import presets
import re

anvil_theme_vars = window.anvilThemeVars

def create_stylesheet(self, form):
    
    self.block_stylesheet = True
    self.preset_stylesheet = document.createElement("style")
    get_dom_node(form).appendChild(self.preset_stylesheet)    
    self.stylesheet = document.createElement("style")
    get_dom_node(form).appendChild(self.stylesheet)    
    self.other_stylesheet = document.createElement("style")
    get_dom_node(form).appendChild(self.other_stylesheet)    
    
    def update_stylesheet():
        if self.block_stylesheet:
            return

        properties = self.css_properties 

        css_rules = "\n".join(f"{key}: {value}" for key, value in properties.items())
        css_rules+="\n"+ (self.css or "")
        
        parsed_css = css_parser(self, css_rules)
        
        self.stylesheet.textContent = parsed_css

    def update_other_stylesheet():
        if self.block_stylesheet:
            return

        other_css = self.other_css or ""

        for state, css in self.states_css.items():
            if not css:
                continue
            other_css+=f"\n:{state}\n{(css)}"
        
        parsed_css = css_parser(self, other_css)

        self.other_stylesheet.textContent = parsed_css

    def update_preset():
        preset_data = presets.data.get(self.preset, {})
        
        preset_rules = ";".join(f"{key}: {value}" for key, value in preset_data.items())
        stylesheet_content = f"""    
            #{self.dom.id} {{
                {preset_rules};
            }}
        """

        self.preset_stylesheet.textContent = stylesheet_content
        
    
    self.update_stylesheet = update_stylesheet
    self.update_preset = update_preset
    self.update_other_stylesheet = update_other_stylesheet
    self.css_properties = {}

def css_parser(self, raw_css):
    
    # Cleanup optional braces and enforce semicolon splitting
    raw_css = raw_css.replace('{', '').replace('}', '')
    lines = re.split(r'[;\n]+', raw_css)
    lines = [line.strip() for line in lines if line.strip()]

    css_blocks = []
    current_selector = f"#{self.uid}"
    current_media = None
    current_block = []

    def replace_theme_vars(value):
        if value.startswith("theme:"):
            theme_key = value[len("theme:"):].strip()
            css_var = anvil_theme_vars.get(theme_key)
            return f"var({css_var})" if css_var else value
        return value

    def flush_block():
        if not current_block:
            return
        rules = []
        for rule in current_block:
            if ":" not in rule:
                continue
            prop, val = map(str.strip, rule.split(":", 1))
            val = replace_theme_vars(val)
            rules.append(f"{prop}: {val}")
        if not rules:
            return
        body = ";".join(rules)
        block = f"{current_selector} {{\n  {body};\n}}"
        if current_media:
            block = f"{current_media} {{\n  {block}\n}}"
        css_blocks.append(block)
        
    for line in lines:
        if line.startswith(":"):
            flush_block()
            pseudo = line[1:].strip()
            current_selector = f"#{self.uid}:{pseudo}"
            current_block = []
        elif line.startswith("!"):
            flush_block()
            class_name = line[1:].strip()
            current_selector = f"#{self.uid} .{class_name}"
            current_block = []
        elif line.startswith("@"):
            flush_block()
            current_selector = f"#{self.uid}"
            current_media = line.strip()
            current_block = []
        elif re.match(r'\w[\w-]*\s*:', line):
            current_block.append(line)
        else:
            # New section or invalid line
            flush_block()
            current_selector = f"#{self.uid}"
            current_media = None
            current_block = []

    flush_block()

    return "\n\n".join(css_blocks)