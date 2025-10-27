from ._anvil_designer import PresetsContainerTemplate
from anvil.designer import in_designer


class PresetsContainer(PresetsContainerTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        if not in_designer:
            self.visible = False