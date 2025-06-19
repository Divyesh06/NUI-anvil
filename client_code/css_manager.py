from anvil.js.window import document
from anvil.js import get_dom_node
from . import presets

def create_stylesheet(self, preset):
    self.block_stylesheet = True
    self.stylesheet = document.createElement("style")
    get_dom_node(self).appendChild(self.stylesheet)

    def implement_presets():
        preset_data = presets.data.get(preset)
        if preset_data:
            for key, value in preset_data.items():
                if not self.css_properties.get(key):
                    self.css_properties[key] = value
    
    def update_stylesheet():
        if self.block_stylesheet:
            return

        self.implement_presets()
        
        properties = self.css_properties

        css_rules = ";".join(f"{key}: {value}" for key, value in properties.items() if key!="border-style" or properties['border-width'])  
        stylesheet_content = f"""
    #{self.dom.id} {{
        {css_rules};
        {';'.join(self.css.splitlines()) if self.css else ""}
    }}"""
        self.stylesheet.textContent = stylesheet_content    
    
    self.update_stylesheet = update_stylesheet
    self.css_properties = {}
    self.implement_presets = implement_presets

