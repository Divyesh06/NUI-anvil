from anvil.js.window import document
from anvil.js import get_dom_node
from . import presets

def create_stylesheet(self):
    self.block_stylesheet = True
    self.stylesheet = document.createElement("style")
    get_dom_node(self).appendChild(self.stylesheet)    
    
    def update_stylesheet():
        if self.block_stylesheet:
            return

        properties = self.css_properties        
        css_rules = ";".join(f"{key}: {value}" for key, value in properties.items() if key!="border-style" or properties['border-width'])  
        preset_data = presets.data.get(self.preset)
        if preset_data:
            css_rules+= ";".join(f"{key}: {value}" for key, value in preset_data.items() if not properties.get(preset_data))  
        stylesheet_content = f"""
    #{self.dom.id} {{
        {css_rules};
        {';'.join(self.css.splitlines()) if self.css else ""}
    }}"""
        self.stylesheet.textContent = stylesheet_content    
    
    self.update_stylesheet = update_stylesheet
    self.css_properties = {}
    

