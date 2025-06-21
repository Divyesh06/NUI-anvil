from anvil.js.window import document
from anvil.js import get_dom_node, window
from .utils import px_convert, id_assigner
from . import css_manager
from anvil.designer import in_designer

ICON_CLASS_MAP = {
    "fa": "fa",           # Font Awesome (e.g., fa:user)
    "fas": "fas",         # Font Awesome Solid
    "far": "far",         # Font Awesome Regular
    "fab": "fab",         # Font Awesome Brands
    "bi": "bi",           # Bootstrap Icons
    "material": "material-icons",  # Material Icons
    "feather": "feather",  # Feather Icons (usually replaced by SVG injection)
    "lucide": "lucide",    # Lucide Icons (usually replaced by SVG injection)
}

class SuperComponent:
    def __init__(self, form, **properties):
        self.form = form
        self._html_tag = None
        self._text = None
        self._other_css = None
        self._hover_css = None
        self._text_type = None
        self._font_size = None
        self._font = None
        self._font_weight = None
        self._foreground = None
        self._background = None
        self._border_radius = None
        self._margin = None
        self._padding = None
        self._border_size = None
        self._border_style = None
        self._icon = None
        self._icon_align = None
        self._border_color = None
        self._text_align = None
        self._css = None
        self._visible = None
        self._preset = None
        
        self.css_properties = {}
        self.states_css = {}
        
        self.last_tag = None
        
        css_manager.create_stylesheet(self, self.form)
        self.uid = id_assigner.get_id()
        self.last_tag = properties['html_tag']
        self._text_type = properties['text_type']
        self._text = properties.get('text')
        self.dom = None
        self.text_dom = None
        
        self.create_dom(self.last_tag)

        self.block_stylesheet = False
        self.update_stylesheet()

        if in_designer:
            self.css_properties['transition'] = "all 0.25s ease-in-out"
        
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
                self.dom.innerText = self.form.__name__
                self.dom.style.opacity = 0.5
                return
            else:
                self.dom.style.opacity = ""
        if self._text_type == 'plain':
            self.dom.innerText = self._text
        else:
            self.dom.innerHTML = self._text

        self.update_icon()
    
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

        if not self.border_style:
            self.border_style = "solid"
    
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
    def other_css(self):
        return self._other_css

    @other_css.setter
    def other_css(self, value):
        self._other_css = value
        self.update_other_stylesheet()

    @property
    def hover_css(self):
        return self._hover_css

    @hover_css.setter
    def hover_css(self, value):
        self._hover_css = value
        self.states_css['hover'] = value
        self.update_other_stylesheet()
    
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

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
        self.update_icon()

    @property
    def icon_align(self):
        return self._icon_align

    @icon_align.setter
    def icon_align(self, value):
        self._icon_align = value
        self.update_icon()

    def update_icon(self):
        for child in list(self.dom.children):
            if child.getAttribute("data-role") == "dynamic-icon":
                self.dom.removeChild(child)

        if not hasattr(self, "icon") or not self.icon:
            return

        # Parse the icon string
        if ":" not in self.icon:
            return  # invalid format
        lib, name = self.icon.split(":", 1)

        # Create the icon element
        icon_el = document.createElement("i")
        icon_el.setAttribute("data-role", "dynamic-icon")

        if lib in ["material"]:
            icon_el.className = ICON_CLASS_MAP[lib]
            icon_el.textContent = name
        elif lib in ICON_CLASS_MAP:
            icon_el.classList.add(ICON_CLASS_MAP[lib])
            icon_el.classList.add(f"{lib}-{name}")
        elif lib in ["feather", "lucide"]:
            # Use SVG injection icon frameworks
            icon_el = document.createElement("i")
            icon_el.setAttribute("data-role", "dynamic-icon")
            icon_el.setAttribute("data-icon-lib", lib)
            icon_el.setAttribute("data-icon-name", name)
            icon_el.classList.add(f"{lib}")
            icon_el.classList.add(f"{name}")
        else:
            return  # Unknown lib

        # Apply alignment
        align = getattr(self, "icon_align", "left")
        icon_el.style.margin = "4px"
        icon_el.style.display = "inline-block"

        if align in ["left", "right"]:
            icon_el.style.verticalAlign = "middle"
        elif align in ["top", "bottom"]:
            icon_el.style.display = "block"
            icon_el.style.margin = "auto"

        # Insert the icon in the correct place
        if align == "left":
            self.dom.insertBefore(icon_el, self.dom.firstChild)
        elif align == "right":
            self.dom.appendChild(icon_el)
        elif align == "top":
            self.dom.insertBefore(icon_el, self.dom.firstChild)
        elif align == "bottom":
            self.dom.appendChild(icon_el)

        # Optional: re-render SVG if Feather/Lucide is used
        if lib == "feather" and hasattr(window, "feather"):
            window.feather.replace()
        elif lib == "lucide" and hasattr(window, "lucide"):
            window.lucide.createIcons()

    def create_dom(self, tag):
        if self.dom:
            self.dom.remove()
        self.dom = document.createElement(tag)
        self.dom.id = self.uid
        get_dom_node(self.form).appendChild(self.dom)
        
    def set_property(self, name, value):
        self.css_properties[name] = value
        self.update_stylesheet()
