from ._anvil_designer import Form2Template
class Form2(Form2Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def button_1_click(self, **event_args):
        self.label_1.text = "Hello"