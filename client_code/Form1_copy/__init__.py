from ._anvil_designer import Form1_copyTemplate
from anvil.js.window import document
from anvil.js import get_dom_node
from ..utils import px_convert, id_assigner
#px_convert.convert_to_px("30")

class Form1_copy(Form1_copyTemplate):
    def __init__(self, **properties):
        self.dom = document.createElement(properties['html_tag'])
        self.stylesheet = None

        self.dom.id = id_assigner.get_id()

        self._border_size = []
        self._border_style = ""
        self._border_color = ""
        self.properties = properties
        self.init_components(**properties)
        get_dom_node(self).appendChild(self.dom)

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
        self.dom.style.fontSize = px_convert.convert_to_px(value)

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value
        self.dom.style.fontFamily = value

    @property
    def font_weight(self):
        return self._font_weight

    @font_weight.setter
    def font_weight(self, value):
        self._font_weight = value
        self.dom.style.fontWeight = value

    @property
    def foreground(self):
        return self._foreground

    @foreground.setter
    def foreground(self, value):
        self._foreground = value
        self.dom.style.color = value

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        self._background = value
        self.dom.style.backgroundColor = value

    @property
    def border_radius(self):
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = value
        self.dom.style.borderRadius = px_convert.convert_to_px(value)

    @property
    def border_size(self):
        return self._border_size

    @border_size.setter
    def border_size(self, value):
        self._border_size = value
        if isinstance(value, list):
            converted = [px_convert.convert_to_px(v) for v in value]
            self.dom.style.borderWidth = " ".join(converted)
        else:
            self.dom.style.borderWidth = px_convert.convert_to_px(value)

    @property
    def border_style(self):
        return self._border_style

    @border_style.setter
    def border_style(self, value):
        self._border_style = value
        self.dom.style.borderStyle = value

    @property
    def border_color(self):
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = value
        self.dom.style.borderColor = value

    @property
    def css(self):
        return self._css

    @css.setter
    def css(self, value):
        self._css = value
        self.generate_stylesheet()



    def generate_stylesheet(self):
        if self.stylesheet:
            self.stylesheet.remove()
        if self.css:
            stylesheet_content = f"""
#{self.dom.id} {{
    {';'.join(self.css.splitlines())}
}}
            """
            print(stylesheet_content)
            self.stylesheet = document.createElement("style")
            self.stylesheet.textContent = stylesheet_content
            get_dom_node(self).appendChild(self.stylesheet)
