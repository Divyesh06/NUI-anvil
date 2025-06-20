from ._anvil_designer import LabelTemplate
from anvil.js.window import document
from anvil.js import get_dom_node
from ..utils import px_convert, id_assigner
from .. import css_manager
from anvil.designer import in_designer
from .. import SuperComponent

super_comp = None

class Label(LabelTemplate):
    def __init__(self, **properties):
        global super_comp
        super_comp = SuperComponent.SuperComponent(self, **properties)
        self.init_components(**properties)

    def __getattr__(self, name):
        return getattr(self, name)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        setattr(super_comp, name, value)