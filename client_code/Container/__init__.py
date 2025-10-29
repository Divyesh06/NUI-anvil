from ._anvil_designer import ContainerTemplate
from .. import SuperComponent
from anvil.designer import in_designer
from ..utils import true_view

class Container(ContainerTemplate):
    def __init__(self, **properties):
        self.super_comp = SuperComponent.SuperComponent(self, events = ["hover", "hover_out", "click"], **properties)
        
        self.is_container = True

        
        self.init_components(**properties)
        self.dom.appendChild(self.dom_nodes['container-slot'])
        
        if in_designer:
            
            self.set_property("min-height", "40px")

            @true_view.true_view
            def true_view_toggle(state):
                if state:
                    self.css_properties.pop("min-height", None)
                    self._update_stylesheet()
                else:
                    self.set_property("min-height", "40px")

        
        

    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            super_comp = object.__getattribute__(self, "super_comp")
            return getattr(super_comp, name)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        setattr(self.super_comp, name, value)

