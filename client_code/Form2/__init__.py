from ._anvil_designer import Form2Template


class Form2(Form2Template):
    def __init__(self, **properties):
        self.init_components(**properties)
