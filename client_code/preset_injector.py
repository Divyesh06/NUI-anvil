from .css_parser import css_parser
from anvil.js.window import document
from . import presets

preset_data = presets.data

presets_stylesheet = document.createElement("style")

presets_css = ""

for preset,css in preset_data.items():
    presets_css+=f"\n{css_parser(css, f'.{preset}')}"

presets_stylesheet.textContent = presets_css

document.body.appendChild(presets_stylesheet)