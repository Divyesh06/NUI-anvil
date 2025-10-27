from ._anvil_designer import PresetsContainerTemplate
from anvil.designer import in_designer
from anvil.js.window import document
from anvil.js import get_dom_node
class PresetsContainer(PresetsContainerTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        if in_designer:
            get_dom_node(self).querySelector(".preset-container").style.display = "flex"
            document.body.style.marginTop = "70px"