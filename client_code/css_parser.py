from anvil.js import window
import re

anvil_theme_vars = window.anvilThemeVars

def css_parser(raw_css, main_selector):
    
    # Cleanup optional braces and enforce semicolon splitting
    raw_css = raw_css.replace('{', '').replace('}', '')
    lines = re.split(r'[;\n]+', raw_css)
    lines = [line.strip() for line in lines if line.strip()]

    css_blocks = []
        
    current_selector = main_selector
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
            current_selector = f"{main_selector}:{pseudo}"
            current_block = []
        elif line.startswith("."):
            flush_block()
            class_name = line
            current_selector = f"{main_selector} {class_name}"
            current_block = []
        elif line.startswith("@"):
            flush_block()
            current_selector = main_selector
            current_media = line.strip()
            current_block = []
        elif re.match(r'\w[\w-]*\s*:', line):
            current_block.append(line)
        else:
            # New section or invalid line
            flush_block()
            current_selector = main_selector
            current_media = None
            current_block = []

    flush_block()

    return "\n\n".join(css_blocks)

from . import preset_injector