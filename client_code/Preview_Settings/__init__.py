from ._anvil_designer import Preview_SettingsTemplate
from anvil import *
from anvil.js import window
from ..utils import true_view
class Preview_Settings(Preview_SettingsTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    @property
    def true_view(self):
        return self._true_view

    @true_view.setter
    def true_view(self, value):
        self._true_view = value
        true_view.raise_all(value)
        