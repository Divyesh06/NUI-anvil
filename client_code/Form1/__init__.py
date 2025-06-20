from ._anvil_designer import Form1Template
from anvil.js.window import document
from anvil.js import get_dom_node
from ..utils import px_convert, id_assigner
from .. import css_manager
from anvil.designer import in_designer

class Form1(Form1Template):
    def init(self, **properties):
        css_manager.create_stylesheet(self)
        self.uid = id_assigner.get_id()
        self.last_tag = properties['html_tag']
        self._text_type = properties['text_type']
        self._text = properties['text']
        self.dom = None
        self.create_dom(self.last_tag)

        self.init_components(**properties)

        self.block_stylesheet = False
        self.update_stylesheet()

    def create_dom(self, tag):
        if self.dom:
            self.dom.remove()
        self.dom = document.createElement(tag)
        self.dom.id = self.uid
        get_dom_node(self).appendChild(self.dom)

    @property
    def html_tag(self):
        return self._html_tag

    @html_tag.setter
    def html_tag(self, value):
        self._html_tag = value
        if value != self.last_tag:
            self.create_dom(value)
            self.last_tag = value
            self.text = self._text
            self.update_preset()
            self.update_stylesheet()    

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self._set_text()

    @property
    def text_type(self):
        return self._text_type

    @text_type.setter
    def text_type(self, value):
        self._text_type = value
        self._set_text()

    def _set_text(self):
        if in_designer:
            if not self._text:
                self.dom.innerText = self.__name__
                self.dom.style.opacity = 0.5
                return
            else:
                self.dom.style.opacity = ""
        if self._text_type == 'plain':
            self.dom.innerText = self._text
        else:
            self.dom.innerHTML = self._text

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        self._font_size = value
        self.set_property("font-size", px_convert.convert_to_px(value))

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value
        self.set_property("font-family", value)

    @property
    def font_weight(self):
        return self._font_weight

    @font_weight.setter
    def font_weight(self, value):
        self._font_weight = value
        self.set_property("font-weight", value)

    @property
    def foreground(self):
        return self._foreground

    @foreground.setter
    def foreground(self, value):
        self._foreground = value
        self.set_property("color", value)

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        self._background = value
        self.set_property("background-color", value)

    @property
    def border_radius(self):
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = value
        value = value.split()
        value = " ".join([px_convert.convert_to_px(v) for v in value])
        
        self.set_property("border-radius", value)

    @property
    def margin(self):
        return self._margin
    
    @margin.setter
    def margin(self, value):
        self._margin = value
        value = value.split()
        value = " ".join([px_convert.convert_to_px(v) for v in value])
        self.set_property("margin", value)
    
    
    @property
    def padding(self):
        return self._padding
    
    @padding.setter
    def padding(self, value):
        self._padding = value
        value = value.split()
        value = " ".join([px_convert.convert_to_px(v) for v in value])
        self.set_property("padding", value)
        
    @property
    def border_size(self):
        return self._border_size

    @border_size.setter
    def border_size(self, value):
        self._border_size = value
        value = value.split()
        value = " ".join([px_convert.convert_to_px(v) for v in value])
        
        self.set_property("border-width", value)

    @property
    def border_style(self):
        return self._border_style

    @border_style.setter
    def border_style(self, value):
        self._border_style = value
        self.set_property("border-style", value)

    @property
    def border_color(self):
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = value
        self.set_property("border-color", value)


        
    @property
    def text_align(self):
        return self._text_align

    @text_align.setter
    def text_align(self, value):
        self._text_align = value
        self.set_property("text-align", value)

    @property
    def css(self):
        return self._css

    @css.setter
    def css(self, value):
        self._css = value
        self.update_stylesheet()

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value
        if not in_designer:
            if not value:
                self.set_property("display", "none")
            else:
                self.set_property("display", "")
        else:
            if not value:
                self.set_property("opacity", "0.3")
            else:
                self.set_property("opacity", "1")

    @property
    def preset(self):
        return self._preset

    @preset.setter
    def preset(self, value):
        self._preset = value
        self.update_preset()

    def set_property(self, name, value):
        self.css_properties[name] = value
        self.update_stylesheet()
