from._anvil_designer import LabelTemplate
from..import SuperComponent
class Label(LabelTemplate):
	def __init__(A,**B):A.super_comp=SuperComponent.SuperComponent(A,events=['hover','hover_out'],**B);A.init_components(**B)
	def __getattr__(A,name):
		try:return object.__getattribute__(A,name)
		except AttributeError:B=object.__getattribute__(A,'super_comp');return getattr(B,name)
	def __setattr__(A,name,value):B=value;object.__setattr__(A,name,B);setattr(A.super_comp,name,B)