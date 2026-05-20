from._anvil_designer import PresetTemplate
from anvil.js import get_dom_node,window
from anvil.js.window import document
from..css_parser import css_parser
from anvil.designer import in_designer
from..Button import Button
from..Label import Label
class Preset(PresetTemplate):
	def __init__(A,**B):
		if in_designer:A.visible=True;A.preset_edit_button=Button(border_radius=7);A.add_component(A.preset_edit_button)
		A.name=None;A.css=None;A.presets_stylesheet=document.createElement('style');A.init_components(**B)
	@property
	def name(self):return self._name
	@name.setter
	def name(self,value):self._name=value;self.init_preset()
	@property
	def css(self):return self._css
	@css.setter
	def css(self,value):self._css=value;self.init_preset()
	def init_preset(A):
		if A.name is not None:A.presets_stylesheet.textContent=css_parser(A.css,f".{A.name}")
		if in_designer:A.preset_edit_button.text=A.name
	def form_show(A,**C):
		B=get_dom_node(A)
		if not in_designer:B.style.display='none'
		if not A.presets_stylesheet.parentNode:B.appendChild(A.presets_stylesheet)
		if A.parent.__class__.__name__!='PresetsContainer':A.add_component(Label(text='Add to PresetsContainer for easier access'))
	def form_hide(A,**B):A.presets_stylesheet.remove();get_dom_node(A).remove()