from ._anvil_designer import ContainerTemplate
from ..SuperComponent import SuperComponent
from anvil.designer import in_designer
from ..utils import true_view
from anvil.js import window,get_dom_node

class Container(ContainerTemplate,SuperComponent):
    def __init__(self, **properties):
        SuperComponent.__init__(self, events = ["hover", "hover_out", "click"], is_container = True, dom = get_dom_node(self.container),**properties)
        # self.super_comp = SuperComponent.SuperComponent()
            
        self.init_components(**properties)
        
        self.true_view = False
        if in_designer:
            
            self.set_property("min-height", "40px")

            @true_view.true_view
            def true_view_toggle(state):
                self.true_view = state
                if state:
                    self.css_properties.pop("min-height", None)
                    self._update_stylesheet()

                    if self.true_html_structure:
                        for component in self.get_components():
                            self.add_to_html_structure(component)
                    
                else:
                    self.set_property("min-height", "40px")
                    
            
                
                
    
    def __getattr__(self, name):
        
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            super_comp = object.__getattribute__(self, "super_comp")
            return getattr(super_comp, name)

    def __setattr__(self, name, value):
        try:
            object.__setattr__(self, name, value)
            setattr(self.super_comp, name, value)
        except:
            pass
            #object.__setattr__(self, name, value)
            

