from._anvil_designer import ContainerTemplate
from..import SuperComponent
from anvil.designer import in_designer
class Container(ContainerTemplate):
	def __init__(A,**B):
		A.super_comp=SuperComponent.SuperComponent(A,events=['hover','hover_out','click'],**B);A.is_container=True;A.init_components(**B);A.dom.appendChild(A.dom_nodes['container-slot'])
		if in_designer:A.set_property('min-height','40px')
	def __getattr__(A,name):
		try:return object.__getattribute__(A,name)
		except AttributeError:B=object.__getattribute__(A,'super_comp');return getattr(B,name)
	def __setattr__(A,name,value):B=value;object.__setattr__(A,name,B);setattr(A.super_comp,name,B)