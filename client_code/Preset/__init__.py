_A=None
from._anvil_designer import PresetTemplate
from anvil.js import get_dom_node,window
from anvil.js.window import document
from..css_parser import css_parser
from anvil.designer import in_designer
from..Button import Button
class Preset(PresetTemplate):
	def __init__(A,**B):
		if in_designer:A.preset_edit_button=Button(border_radius=7);A.add_component(A.preset_edit_button);A.timer_1.interval=.2
		A.name=_A;A.css=_A;A.presets_stylesheet=document.createElement('style');A.init_components(**B)
	def get_preset_container(B):
		try:
			A=window.preset_container
			if not A.parentNode:document.body.prepend(A)
		except:A=_A
		if not A:A=document.createElement('div');A.style.display='flex';A.style.gap='5px';A.style.padding='5px 10px';A.style.left='0';A.style.backgroundColor='#141414';A.style.borderBottom='solid #666 1px';A.style.alignItems='center';A.style.top='0';A.style.width='100vw';A.innerHTML="<span style = 'padding-right: 10px; font-weight: 600; color: #ddd; '>Presets:</span>";window.preset_container=A;document.body.prepend(A)
		return A
	@property
	def name(self):return self._name
	@name.setter
	def name(self,value):self._name=value;self.init_preset()
	@property
	def css(self):return self._css
	@css.setter
	def css(self,value):self._css=value;self.init_preset()
	def init_preset(A):
		if A.name is not _A:A.presets_stylesheet.textContent=css_parser(A.css,f".{A.name}")
		if in_designer:A.preset_edit_button.text=A.name
	def form_show(A,**C):
		B=get_dom_node(A)
		if not in_designer:B.style.display='none'
		else:get_dom_node(A).remove();A.get_preset_container().appendChild(get_dom_node(A))
		if not A.presets_stylesheet.parentNode:B.appendChild(A.presets_stylesheet)
	def form_hide(A,**B):A.presets_stylesheet.remove();get_dom_node(A).remove()
	def timer_1_tick(A,**B):A.get_preset_container()