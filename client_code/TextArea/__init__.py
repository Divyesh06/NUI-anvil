from ._anvil_designer import TextAreaTemplate
from .. import SuperComponent

class TextArea(TextAreaTemplate):
    def __init__(self, **properties):
        self.super_comp = SuperComponent.SuperComponent(self, events = ["hover", "hover_out", "focus", "lost_focus", "change"], **properties)
        self.is_textarea = True
        self.init_components(**properties)
        self.add_event("input", self._set_text_on_input)

    def _set_text_on_input(self, **event_args):
        event_args['sender'].text = event_args['event'].target.value
        self.raise_event("input")
        
    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            super_comp = object.__getattribute__(self, "super_comp")
            return getattr(super_comp, name)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        setattr(self.super_comp, name, value)
