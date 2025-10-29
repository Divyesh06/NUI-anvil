from ._anvil_designer import Form1Template


class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def file_loader_1_change(self, file, **event_args):
        self.image_1.source = file