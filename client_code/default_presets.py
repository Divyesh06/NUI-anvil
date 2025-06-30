from anvil.js.window import document
presets_stylesheet=document.createElement('style')
document.body.appendChild(presets_stylesheet)
default_css='\n[nui-icon="true"] {\n    padding-right: 5px;\n}\n\n.default-label {\n    margin: 5px 0;\n}\n\n.default-btn {\n    margin: 5px 0;\n    padding: 8px 15px;\n    border-radius: 15px;\n}\n\n.default-textbox {\n    border-radius: 5px;\n    border: solid #ccc 1px;\n    border-style: solid;\n    width: 100%;\n    padding: 8px 12px;\n}\n\n.default-textarea {\n    border-radius: 5px;\n    border: solid #ccc 1px;\n    border-style: solid;\n    width: 100%;\n    padding: 8px 12px;\n}\n'
presets_stylesheet.textContent=default_css