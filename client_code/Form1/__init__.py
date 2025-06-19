from ._anvil_designer import Form1Template
from anvil.js.window import document
from anvil.js import get_dom_node
from ..utils import px_convert, id_assigner
from .. import css_manager
#px_convert.convert_to_px("30") 

class Form1(Form1Template):
    def __init__(self, **properties):
        self.dom = document.createElement(properties['html_tag'])
        css_manager.create_stylesheet(self, properties['preset'])
        self.dom.id = id_assigner.get_id()
        self.init_components(**properties)
        get_dom_node(self).appendChild(self.dom)
        self.implement_presets()
        self.block_stylesheet = False
        self.update_stylesheet()
        
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        self._text = value
        if value:
            self.dom.innerText = value
    
    @property
    def html(self):
        return self._html
    
    @html.setter
    def html(self, value):
        self._html = value
        if value:
            self.dom.innerHTML = value
    
    @property
    def font_size(self):
        return self._font_size
    
    @font_size.setter
    def font_size(self, value):
        self._font_size = value
        self.css_properties["font-size"] = px_convert.convert_to_px(value)
        self.update_stylesheet()
    
    @property
    def font(self):
        return self._font
    
    @font.setter
    def font(self, value):
        self._font = value
        self.css_properties["font-family"] = value
        self.update_stylesheet()
    
    @property
    def font_weight(self):
        return self._font_weight
    
    @font_weight.setter
    def font_weight(self, value):
        self._font_weight = value
        self.css_properties["font-weight"] = value
        self.update_stylesheet()
    
    @property
    def foreground(self):
        return self._foreground
    
    @foreground.setter
    def foreground(self, value):
        self._foreground = value
        self.css_properties["color"] = value
        self.update_stylesheet()
    
    @property
    def background(self):
        return self._background
    
    @background.setter
    def background(self, value):
        self._background = value
        self.css_properties["background-color"] = value
        self.update_stylesheet()
    
    @property
    def border_radius(self):
        return self._border_radius
    
    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = value
        self.css_properties["border-radius"] = px_convert.convert_to_px(value)
        self.update_stylesheet()
    
    @property
    def border_size(self):
        return self._border_size
    
    @border_size.setter
    def border_size(self, value):
        self._border_size = value
        if isinstance(value, list):
            converted = [px_convert.convert_to_px(v) for v in value]
            self.css_properties["border-width"] = " ".join(converted)
        else:
            self.css_properties["border-width"] = px_convert.convert_to_px(value)
        self.update_stylesheet()
    
    @property
    def border_style(self):
        return self._border_style
    
    @border_style.setter
    def border_style(self, value):
        self._border_style = value
        self.css_properties["border-style"] = value
        self.update_stylesheet()
    
    @property
    def border_color(self):
        return self._border_color
    
    @border_color.setter
    def border_color(self, value):
        self._border_color = value
        self.css_properties["border-color"] = value
        self.update_stylesheet()

    @property
    def preset(self):
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = value
        self.css_properties["border-color"] = value
        self.update_stylesheet()


   