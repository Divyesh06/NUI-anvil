from ._anvil_designer import Form2Template
from anvil.js import window
class Form2(Form2Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        #self.label_1.font_size = 200
       # self.label_1.pp = 200

    def label_1_hover(self, **event_args):
        print(event_args['sender'])
        print(event_args['event'])

    def button_3_click(self, **event_args):
        print("Clicked")

    def container_1_click(self, **event_args):
        print("Click")