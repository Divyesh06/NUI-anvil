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
    border: none;
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

presets_stylesheet.textContent = default_css

