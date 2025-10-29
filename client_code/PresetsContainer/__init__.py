from ._anvil_designer import PresetsContainerTemplate
from anvil.designer import in_designer
from anvil.js.window import document
from anvil.js import get_dom_node
from ..utils import true_view

class PresetsContainer(PresetsContainerTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        if in_designer:
            get_dom_node(self).querySelector(".preset-container").style.display = "flex"
            document.body.style.marginTop = "70px"

            @true_view.true_view
            def true_view_toggle(state):
                if state:
                    get_dom_node(self).style.display = "none"
                    document.body.style.marginTop = ""
                else:
                    get_dom_node(self).style.display = "flex"
                    document.body.style.marginTop = "70px"
            