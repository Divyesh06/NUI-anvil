from ._anvil_designer import PresetsTemplate

class Presets(PresetsTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def form_show(self, **event_args):
        from . import presets
        presets.init_presets()