from ._anvil_designer import PresetsTemplate
from anvil.js import get_dom_node, window

class Presets(PresetsTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        presets_stylesheet = document.createElement("style")
        get_dom_node(self).appendChild(presets_stylesheet)

    def form_show(self, **event_args):
        from . import presets
        presets.init_presets()