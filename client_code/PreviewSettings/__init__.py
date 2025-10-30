from ._anvil_designer import PreviewSettingsTemplate
from anvil import *
from anvil.js import window
from ..utils import true_view
from anvil.designer import in_designer
class PreviewSettings(PreviewSettingsTemplate):
    def __init__(self, **properties):
        
        if not in_designer:
            return

        self.html = """
<div class="nui-preview-icon">
    <i class="fa fa-eye" ></i>
</div>

<style>
.anvil-container:has(>.nui-preview-icon) {
    z-index: 999999999;
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    right: 10px;
    top: 10px;
    font-size: 18px;
    color: #555;
    width: 50px;
    height: 50px;
    background: white;
    border: solid #11abeb 2px;
    border-radius: 50%;
}
    
</style>        
"""

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
        window.true_view = value
        true_view.raise_all(value)
        
        
    @property
    def inflate_containers(self):
        return self._inflate_containers

    @inflate_containers.setter
    def inflate_containers(self, value):
        self._inflate_containers = value
        if self._inflate_containers:
           window.document.body.classList.add("inflate")
        else:
            window.document.body.classList.remove("inflate")

    def form_show(self, **event_args):
        true_view.raise_all(self._true_view)
        