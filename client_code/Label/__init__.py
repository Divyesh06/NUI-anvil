from ._anvil_designer import LabelTemplate
from ..SuperComponent import SuperComponent
from anvil.js import get_dom_node
from anvil import alert
class Label(SuperComponent, LabelTemplate):
    def __init__(self, **properties):
        print(properties)
        super().__init__(self, events = ["hover", "hover_out", "click"], dom=get_dom_node(self),**properties)
    #     self.remove_from_parent = self.super_comp.remove_from_parent
    #     self.init_components(**properties)
        

    # def __getattr__(self, name):
    #     try:
    #         return object.__getattribute__(self, name)
    #     except AttributeError:
    #         super_comp = object.__getattribute__(self, "super_comp")
    #         return getattr(super_comp, name)

    # def __setattr__(self, name, value):
    #     object.__setattr__(self, name, value)
    #     setattr(self.super_comp, name, value)
