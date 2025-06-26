from .css_parser import css_parser
from anvil.js.window import document

classes_stylesheet = document.createElement("style")
document.body.appendChild(classes_stylesheet)

presets = {

}


def init_presets():
    presets_css = ""
    
    for preset,css in presets.items():
        presets_css+=f"\n{css_parser(css, preset)}"

    classes_stylesheet.textContent = presets_css

