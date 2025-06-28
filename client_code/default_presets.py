from .css_parser import css_parser
from anvil.js.window import document

presets_stylesheet = document.createElement("style")
document.body.appendChild(presets_stylesheet)

default_css = """
[nui-icon="true"] {
    padding-right: 5px;
}

.default-label {
    margin: 5px 0;
}

.default-btn {
    margin: 5px 0;
    padding: 8px 15px;
    border-radius: 15px;
}

.default-textbox {
    border-radius: 5px;
    border: solid #ccc 1px;
    border-style: solid;
    width: 100%;
    padding: 8px 12px;
}

.default-textarea {
    border-radius: 5px;
    border: solid #ccc 1px;
    border-style: solid;
    width: 100%;
    padding: 8px 12px;
}
"""

def init_presets():
    presets_css = ""
    
    for preset,css in preset.items():
        presets_css+=f"\n{css_parser(css, '.'+preset)}"

    classes_stylesheet.textContent = default_css+presets_css

