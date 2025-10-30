from ._anvil_designer import PresetsContainerTemplate
from anvil.designer import in_designer
from anvil.js.window import document
from anvil.js import get_dom_node
from ..utils import true_view

class PresetsContainer(PresetsContainerTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        if not in_designer:
            return
        self.html = """
<div class='nui-preset-container'>
    <span style='margin-right: 10px'>Presets</span>
    <div anvil-slot-repeat='default' anvil-name='container-slot'></div>

</div>


<style>
.anvil-container:has(>.nui-preset-container) {
    position: fixed;
    left: 0;
    top: 0;
    width: 100vw;
}
.nui-preset-container {
    gap: 10px;
    padding-right: 80px;
    z-index: 99999999;
    background: #1f1f1f;
    padding: 10px 65px 10px 10px;
    color: #ddd;
    width: 100%;
    height: 75px;
    display: flex;
    align-items: center;
    overflow: auto hidden;
}

.nui-preset-container button{
    color: black;
    white-space: nowrap;

}
</style>    
"""
        self.visible = True
        document.body.style.marginTop = "70px"

        @true_view.true_view
        def true_view_toggle(state):
            if state:
                get_dom_node(self).style.display = "none"
                document.body.style.marginTop = ""
            else:
                get_dom_node(self).style.display = "flex"
                document.body.style.marginTop = "70px"
        