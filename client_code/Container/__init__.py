from._anvil_designer import ContainerTemplate
from..import SuperComponent
from anvil.designer import in_designer
from..utils import true_view
from anvil.js import window,get_dom_node
class Container(ContainerTemplate):
	def __init__(A,**C):
		D='40px';B='min-height';A.super_comp=SuperComponent.SuperComponent(A,events=['hover','hover_out','click'],is_container=True,**C);A.init_components(**C);A.dom.appendChild(A.dom_nodes['container-slot']);A.true_view=False
		if in_designer:
			A.set_property(B,D)
			@true_view.true_view
			def E(state):
				C=state;A.true_view=C
				if C:
					A.css_properties.pop(B,None);A._update_stylesheet()
					if A.true_html_structure:
						for E in A.get_components():A.add_to_html_structure(E)
				else:A.set_property(B,D)
	def __getattr__(A,name):
		try:return object.__getattribute__(A,name)
		except AttributeError:B=object.__getattribute__(A,'super_comp');return getattr(B,name)
	def __setattr__(A,name,value):B=value;object.__setattr__(A,name,B);setattr(A.super_comp,name,B)