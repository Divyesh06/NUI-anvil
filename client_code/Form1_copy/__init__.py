from ._anvil_designer import Form1_copyTemplate
from anvil.js.window import document
from anvil.js import get_dom_node
from ..utils import px_convert, id_assigner
from .. import css_manager
from anvil.designer import in_designer
from .. import Properties

class Form1_copy(Form1_copyTemplate):
    def __init__(self, **properties):
        self.super = Properties.SuperComponent()
        css_manager.create_stylesheet(self)
        self.uid = id_assigner.get_id()
        self.last_tag = properties['html_tag']
        self._text_type = properties['text_type']
        self._text = properties['text']
        self.dom = None
        self.create_dom(self.last_tag)

        self.init_components(**properties)

        self.block_stylesheet = False
        self.update_stylesheet()

    def __getattribute__(self, name):
        try:
            # Try local attribute first
            return object.__getattribute__(self, name)
        except AttributeError:
            # Delegate to self.super if attribute not found
            fallback = object.__getattribute__(self, "super")
            return getattr(fallback, name)

    def __setattr__(self, name, value):
        if name in ("super", "own_attr"):
            object.__setattr__(self, name, value)
        else:
            fallback = object.__getattribute__(self, "super")
            setattr(fallback, name, value)