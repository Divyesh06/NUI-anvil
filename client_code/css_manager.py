from anvil.js.window import document
from anvil.js import get_dom_node
from . import presets

def create_stylesheet(self, form):
    
    self.block_stylesheet = True
    self.preset_stylesheet = document.createElement("style")
    get_dom_node(form).appendChild(self.preset_stylesheet)    
    self.stylesheet = document.createElement("style")
    get_dom_node(form).appendChild(self.stylesheet)    
    
    def update_stylesheet():
        if self.block_stylesheet:
            return

        properties = self.css_properties        
        css_rules = ";".join(f"{key}: {value}" for key, value in properties.items())  
        
        stylesheet_content = f"""    
            #{self.dom.id} {{
                {css_rules};
                {';'.join(self.css.splitlines()) if self.css else ""}
            }}
        """
        
        self.stylesheet.textContent = stylesheet_content    

    def update_preset():
        preset_data = presets.data.get(self.preset, {})
        
        preset_rules = ";".join(f"{key}: {value}" for key, value in preset_data.items())
        stylesheet_content = f"""    
            #{self.dom.id} {{
                {preset_rules};
                {';'.join(self.css.splitlines()) if self.css else ""}
            }}
        """

        self.preset_stylesheet.textContent = stylesheet_content
        
    
    self.update_stylesheet = update_stylesheet
    self.update_preset = update_preset
    self.css_properties = {}