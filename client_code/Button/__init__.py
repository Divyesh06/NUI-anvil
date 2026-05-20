from._anvil_designer import ButtonTemplate
from..import SuperComponent
class Button(ButtonTemplate):
	def __init__(A,**B):A.super_comp=SuperComponent.SuperComponent(A,events=['hover','hover_out','click'],**B);A.remove_from_parent=A.super_comp.remove_from_parent;A.init_components(**B)
	def __getattr__(A,name):
		try:return object.__getattribute__(A,name)
		except AttributeError:B=object.__getattribute__(A,'super_comp');return getattr(B,name)
	def __setattr__(A,name,value):B=value;object.__setattr__(A,name,B);setattr(A.super_comp,name,B)