_A='StyleSheet'
from._anvil_designer import StyleSheetTemplate
from anvil.js import get_dom_node,window
from anvil.js.window import document
from..css_parser import css_parser
from anvil.designer import in_designer,get_design_name
from..Button import Button
from..Label import Label
class StyleSheet(StyleSheetTemplate):
	def __init__(A,**B):
		if in_designer:A.preset_edit_button=Button(border_radius=7);A.add_component(A.preset_edit_button)
		A.presets_stylesheet=document.createElement('style');A.css=None;A.init_components(**B)
	@property
	def css(self):return self._css
	@css.setter
	def css(self,value):self._css=value;self.init_preset()
	def init_preset(A):
		A.presets_stylesheet.textContent=A.css
		if in_designer:A.preset_edit_button.text=get_design_name(A)or _A
	def form_show(A,**C):
		B=get_dom_node(A)
		if not in_designer:B.style.display='none'
		if not A.presets_stylesheet.parentNode:B.appendChild(A.presets_stylesheet)
		if A.parent.__class__.__name__!='PresetsContainer':A.add_component(Label(text='Add to PresetsContainer for easier access'))
		if in_designer:A.preset_edit_button.text=get_design_name(A)or _A
	def form_hide(A,**B):A.presets_stylesheet.remove();get_dom_node(A).remove()