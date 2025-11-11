from ._anvil_designer import Form3Template


class Form3(Form3Template):
    def __init__(self, **properties):
        self.init_components(**properties)
