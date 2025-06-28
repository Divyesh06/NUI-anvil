from ._anvil_designer import TextBoxTemplate
from .. import SuperComponent

class TextBox(TextBoxTemplate):
    def __init__(self, **properties):
        self.super_comp = SuperComponent.SuperComponent(self, events = ["hover", "hover_out", "focus", "lost_focus", "input", "change"], **properties)
        self.is_textbox = True
        self.init_components(**properties)

        self.add_event("keydown", self._detect_enter_press)

    def _detect_enter_press(self, **event_args):
        if event_args['event'].key == "Enter":
            self.raise_event("pressed_enter")

    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            super_comp = object.__getattribute__(self, "super_comp")
            return getattr(super_comp, name)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        setattr(self.super_comp, name, value)
