from ._anvil_designer import PresetTemplate
from anvil.js import get_dom_node, window
from anvil.js.window import document
from ..css_parser import css_parser
from anvil.designer import in_designer
from ..Button import Button

class Preset(PresetTemplate):
    def __init__(self, **properties):
        

        if in_designer:
            self.preset_edit_button = Button(border_radius = "7")
            self.add_component(self.preset_edit_button)
            self.timer_1.interval = 0.2
            
        self.name = None
        self.css = None
        self.presets_stylesheet = document.createElement("style")

        self.init_components(**properties)
        
    def get_preset_container(self):
       
        try:
            preset_container = window.preset_container
            if not preset_container.parentNode:
                document.body.prepend(preset_container)
                
        except Exception as e:
            print(str(e))
            preset_container = None
            
        if not preset_container:
            preset_container = document.createElement("div")
            preset_container.style.display = "flex"
            preset_container.style.flexDirection = "row-reverse"
            preset_container.style.gap = "5px"
            preset_container.style.padding = "5px 10px"
            preset_container.style.left = "0"
            preset_container.style.top = "0"
            preset_container.style.width = "100vw"

            window.preset_container = preset_container
            document.body.prepend(preset_container)
            
        return preset_container
            
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.init_preset()

    @property
    def css(self):
        return self._css

    @css.setter
    def css(self, value):
        self._css = value
        self.init_preset()

    
    def init_preset(self):
        if self.name is not None:
            self.presets_stylesheet.textContent = css_parser(self.css, f".{self.name}")\

        if in_designer:
            self.preset_edit_button.text = self.name

    def form_show(self, **event_args):
        
        self_dom = get_dom_node(self)
        if not in_designer:
            self_dom.style.display = "none"
            
        else:
            get_dom_node(self).remove()
            self.get_preset_container().appendChild(get_dom_node(self))

        if not self.presets_stylesheet.parentNode:
            self_dom.appendChild(self.presets_stylesheet)

    def form_hide(self, **event_args):
        self.presets_stylesheet.remove()
        get_dom_node(self).remove()

    def timer_1_tick(self, **event_args):
        self.get_preset_container()