from._anvil_designer import PresetsContainerTemplate
from anvil.designer import in_designer
from anvil.js.window import document
from anvil.js import get_dom_node
from..utils import true_view
class PresetsContainer(PresetsContainerTemplate):
	def __init__(A,**C):
		B='70px';A.init_components(**C)
		if not in_designer:return
		A.html="\n<div class='nui-preset-container'>\n    <span style='margin-right: 10px'>Presets</span>\n    <div anvil-slot-repeat='default' anvil-name='container-slot'></div>\n\n</div>\n\n\n<style>\n.anvil-container:has(>.nui-preset-container) {\n    position: fixed;\n    left: 0;\n    top: 0;\n    width: 100vw;\n}\n.nui-preset-container {\n    gap: 10px;\n    padding-right: 80px;\n    z-index: 99999999;\n    background: #1f1f1f;\n    padding: 10px 65px 10px 10px;\n    color: #ddd;\n    width: 100%;\n    height: 75px;\n    display: flex;\n    align-items: center;\n    overflow: auto hidden;\n}\n\n.nui-preset-container button{\n    color: black;\n    white-space: nowrap;\n\n}\n</style>    \n";A.visible=True;document.body.style.marginTop=B
		@true_view.true_view
		def D(state):
			if state:get_dom_node(A).style.display='none';document.body.style.marginTop=''
			else:get_dom_node(A).style.display='flex';document.body.style.marginTop=B