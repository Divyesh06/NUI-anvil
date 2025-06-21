from .css_parser import css_parser
from anvil.js.window import document

classes_stylesheet = document.createElement("style")
document.body.appendChild(classes_stylesheet)

presets = {

}

default_presets = {
"default-label" : """
    margin: 5px 0;
"""
}

def init_presets():
    presets_css = ""
    merged_dict = {**presets, **default_presets}
    for preset,css in merged_dict.items():
        presets_css+=f"\n{css_parser(css, f'.nui-{preset}')}"

    classes_stylesheet.textContent = presets_css

