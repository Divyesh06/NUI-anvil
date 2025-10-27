from ._anvil_designer import ButtonTemplate
from .. import SuperComponent

class Button(ButtonTemplate):
    def __init__(self, **properties):
        self.super_comp = SuperComponent.SuperComponent(self, events = ["hover", "hover_out", "click"], **properties)
        self.remove_from_parent = self.super_comp.remove_from_parent
        self.init_components(**properties)

    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            super_comp = object.__getattribute__(self, "super_comp")
            return getattr(super_comp, name)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        setattr(self.super_comp, name, value)

    