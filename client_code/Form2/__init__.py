from ._anvil_designer import Form2Template
from anvil.js import window
from anvil import alert
class Form2(Form2Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        #self.label_1.font_size = 200
       # self.label_1.pp = 200

 