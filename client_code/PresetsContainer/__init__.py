from ._anvil_designer import PresetsContainerTemplate
from anvil.designer import in_designer
from anvil.js.window import document

class PresetsContainer(PresetsContainerTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        if not in_designer:
            self.visible = False
        else:
            document.body.style.marginTop = "70px"