from ._anvil_designer import True_Html_StructureTemplate
from .. import components as NUI

class True_Html_Structure(True_Html_StructureTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        


    def button_1_click(self, **event_args):
        self.label_1.remove_from_parent()
        print(self.label_1.parent)

    def button_1_copy_click(self, **event_args):
        self.container_2.add_component(self.label_1)
        print(self.label_1.parent)
