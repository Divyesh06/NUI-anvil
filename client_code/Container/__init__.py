from ._anvil_designer import ContainerTemplate
from .. import SuperComponent

class Container(ContainerTemplate):
    def __init__(self, **properties):
        self.super_comp = SuperComponent.SuperComponent(self, events = ["hover", "hover_out", "click"], **properties)

        self.is_container = True

 
        self.init_components(**properties)
        self.dom.appendChild(self.dom_nodes['container-slot'])

        

    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            super_comp = object.__getattribute__(self, "super_comp")
            return getattr(super_comp, name)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        setattr(self.super_comp, name, value)
