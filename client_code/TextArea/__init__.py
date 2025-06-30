from._anvil_designer import TextAreaTemplate
from..import SuperComponent
class TextArea(TextAreaTemplate):
	def __init__(A,**B):A.super_comp=SuperComponent.SuperComponent(A,events=['hover','hover_out','focus','lost_focus','change'],**B);A.is_textarea=True;A.init_components(**B);A.add_event('input',A._set_text_on_input)
	def _set_text_on_input(B,**A):A['sender'].text=A['event'].target.value;B.raise_event('input')
	def __getattr__(A,name):
		try:return object.__getattribute__(A,name)
		except AttributeError:B=object.__getattribute__(A,'super_comp');return getattr(B,name)
	def __setattr__(A,name,value):B=value;object.__setattr__(A,name,B);setattr(A.super_comp,name,B)