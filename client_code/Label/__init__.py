from ._anvil_designer import LabelTemplate
from .. import SuperComponent

class Label(LabelTemplate):
    def __init__(self, **properties):
        self.super_comp = SuperComponent.SuperComponent(self, **properties)
        self.init_components(**properties)

    def __getattr__(self, name):
        return getattr(self, name)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        setattr(self.super_comp, name, value)