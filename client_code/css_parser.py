from anvil.js import window
import re

anvil_theme_vars = window.anvilThemeVars
def css_parser(raw_css, main_selector):
    # Remove braces and split into lines

    if not raw_css:
        return ""
    raw_css = raw_css.replace('{', '').replace('}', '')
    lines = [line.lstrip() for line in re.split(r'[;\n]+', raw_css) if line.strip()]

    css_blocks = []
    current_selector = main_selector
    current_media = None
    current_block = []

    def replace_theme_vars(value):
        if "theme:" not in value:
            return value
        parts = value.split()
        
        for i, part in enumerate(parts):
            if part.startswith("theme:"):
                theme_key = part[len("theme:"):].strip()
                css_var = anvil_theme_vars.get(theme_key.replace("_"," "))
                if not css_var:
                    css_var = anvil_theme_vars.get(theme_key)
                if css_var:
                    parts[i] = f"var({css_var})"
        
        return " ".join(parts)

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
        body = "; ".join(rules)
        block = f"{current_selector} {{\n  {body};\n}}"
        if current_media:
            block = f"{current_media} {{\n  {block}\n}}"
        css_blocks.append(block)

    def is_property_line(line):
        return re.match(r'^[\w-]+\s*:', line)

    for line in lines:
        if is_property_line(line):
            current_block.append(line)
        elif line.startswith("@"):
            flush_block()
            current_selector = main_selector
            current_media = line
            current_block = []
        else:
            flush_block()
            raw_line = line.rstrip()  # Preserve leading space
            if raw_line.startswith("&"):
                current_selector = raw_line.replace("&", main_selector)
            elif raw_line[:1] in (">", "+", "~", "[", ":", ".", "#") or raw_line.startswith(" "):
                current_selector = f"{main_selector}{raw_line}"
            else:
                current_selector = f"{main_selector} {raw_line}"
            current_media = None
            current_block = []

    flush_block()
    return "\n\n".join(css_blocks)

from . import default_presets