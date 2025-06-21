from ._anvil_designer import Form2Template
class Form2(Form2Template):
    def __init__(self, **properties):
        self.init_components(**properties)


    def button_1_click(self, **event_args):
        self.form1_copy_1.text = "Hey"

    def button_2_click(self, **event_args):
        print(self.form1_copy_1.text)

    def label_1_show(self, **event_args):
        print("show")