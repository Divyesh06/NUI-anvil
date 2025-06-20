from ._anvil_designer import LabelTemplate
from anvil.js.window import document
from anvil.js import get_dom_node
from ..utils import px_convert, id_assigner
from .. import css_manager
from anvil.designer import in_designer
from ..Super import SuperComponent
class Label(SuperComponent):
    def __init__(self, **properties):
        for i in dir(LabelTemplate):
            try:
                setattr(self, i, getattr(LabelTemplate, i))
            except:
                pass
        super().init(self, a = 'b')