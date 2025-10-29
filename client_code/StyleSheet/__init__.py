from ._anvil_designer import StyleSheetTemplate
from anvil.js import get_dom_node, window
from anvil.js.window import document
from ..css_parser import css_parser
from anvil.designer import in_designer, get_design_name
from ..Button import Button
from ..Label import Label

class StyleSheet(StyleSheetTemplate):
    def __init__(self, **properties):
        if in_designer:
            self.preset_edit_button = Button(border_radius=7)
            self.add_component(self.preset_edit_button)
           
        self.presets_stylesheet = document.createElement("style")
        self.css = None
        self.init_components(**properties)

    @property
    def css(self):
        return self._css

    @css.setter
    def css(self, value):
        self._css = value
        self.init_preset()

    def init_preset(self):
        self.presets_stylesheet.textContent = self.css
            

        if in_designer:
            self.preset_edit_button.text = get_design_name(self) or "StyleSheet"

    def form_show(self, **event_args):
        self_dom = get_dom_node(self)
        if not in_designer:
            self_dom.style.display = "none"            

        if not self.presets_stylesheet.parentNode:
            self_dom.appendChild(self.presets_stylesheet)

        if self.parent.__class__.__name__ != "PresetsContainer":
            self.add_component(Label(text = "Add to PresetsContainer for easier access"))


        if in_designer:
            self.preset_edit_button.text = get_design_name(self) or "StyleSheet"

    def form_hide(self, **event_args):
        self.presets_stylesheet.remove()
        get_dom_node(self).remove()
