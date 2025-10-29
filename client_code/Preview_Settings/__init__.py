from ._anvil_designer import Preview_SettingsTemplate
from anvil import *
from anvil.js import window
from ..utils import true_view
from anvil.designer import in_designer
class Preview_Settings(Preview_SettingsTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        if not in_designer:
            return

        self.inflate_stylesheet = window.document.createElement("style")
        self.inflate_stylesheet.textContent = """
.nui-container.inflate {
    padding: 20px;
}      
"""
        

    @property
    def true_view(self):
        return self._true_view

    @true_view.setter
    def true_view(self, value):
        self._true_view = value
        true_view.raise_all(value)
        
    @property
    def inflate_container(self):
        return self._inflate_contains

    @inflate_container.setter
    def inflate_container(self, value):
        self._inflate_container = value
        if se

    def form_show(self, **event_args):
        true_view.raise_all(self._true_view)
        