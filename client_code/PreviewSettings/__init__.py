from._anvil_designer import PreviewSettingsTemplate
from anvil import*
from anvil.js import window
from..utils import true_view
from anvil.designer import in_designer
class PreviewSettings(PreviewSettingsTemplate):
	def __init__(self,**properties):
		if not in_designer:return
		self.html='\n<div class="nui-preview-icon">\n    <i class="fa fa-eye" ></i>\n</div>\n\n<style>\n.anvil-container:has(>.nui-preview-icon) {\n    z-index: 999999999;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    position: fixed;\n    right: 10px;\n    top: 10px;\n    font-size: 18px;\n    color: #555;\n    width: 50px;\n    height: 50px;\n    background: white;\n    border: solid #11abeb 2px;\n    border-radius: 50%;\n}\n    \n</style>        \n';self.visible=True;self.inflate_stylesheet=window.document.createElement('style');self.inflate_stylesheet.textContent='\n.inflate .nui-container, .inflate .anvil-container:not(.html-templated-panel)  {\n    padding: 25px;\n}      \n';window.document.head.appendChild(self.inflate_stylesheet);self.init_components(**properties);self.set_event_handler('show',self.form_show)
	@property
	def true_view(self):return self._true_view
	@true_view.setter
	def true_view(self,value):self._true_view=value;window.true_view=value;true_view.raise_all(value)
	@property
	def inflate_containers(self):return self._inflate_containers
	@inflate_containers.setter
	def inflate_containers(self,value):
		A='inflate';self._inflate_containers=value
		if self._inflate_containers:window.document.body.classList.add(A)
		else:window.document.body.classList.remove(A)
	def form_show(self,**event_args):true_view.raise_all(self._true_view)