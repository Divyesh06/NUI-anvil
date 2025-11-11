from ._anvil_designer import Form1Template
from ..Form2 import Form2

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        a = Form2()
        a.container_1.remove_from_parent()
        self.container_1.add_component(a.container_1)
