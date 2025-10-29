from ._anvil_designer import Preview_SettingsTemplate
from anvil import *
from anvil.js import window
from ..utils import true_view
from anvil.designer import in_designer
class Preview_Settings(Preview_SettingsTemplate):
    def __init__(self, **properties):
        
        if not in_designer:
            return

        self.visible = True
        self.inflate_stylesheet = window.document.createElement("style")
        self.inflate_stylesheet.textContent = """
.inflate .nui-container, .inflate .anvil-container:not(.html-templated-panel)  {
    padding: 25px;
}      
"""
        window.document.head.appendChild(self.inflate_stylesheet)
        self.init_components(**properties)
        self.set_event_handler("show", self.form_show)

    @property
    def true_view(self):
        return self._true_view

    @true_view.setter
    def true_view(self, value):
        self._true_view = value
        true_view.raise_all(value)
        
    @property
    def inflate_container(self):
        return self._inflate_container

    @inflate_container.setter
    def inflate_container(self, value):
        self._inflate_container = value
        if self._inflate_container:
           window.document.body.classList.add("inflate")
        else:
            window.document.body.classList.remove("inflate")

    def form_show(self, **event_args):
        true_view.raise_all(self._true_view)
        