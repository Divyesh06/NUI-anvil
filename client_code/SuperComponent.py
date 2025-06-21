from anvil.js.window import document
from anvil.js import get_dom_node
from .utils import px_convert, id_assigner
from .css_parser import css_parser
from anvil.designer import in_designer

events_map = {
    "hover": "mouseenter",
    "hover_out": "mouseleave",
    "click": "click"
}

reverse_events_map = {v: k for k, v in events_map.items()}

class SuperComponent:
    def __init__(self, form, events = [], **properties):
        self.form = form
        self.events = events
        
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
        self._icon_size = None
        self._icon_css = None
        self._custom_icon =  None
        self._border_color = None
        self._text_align = None
        self._css = None
        self._visible = None
        self._preset = None
        
        self.css_properties = {}
        self.states_css = {}
        
        self.last_tag = None
        
        
        self.uid = id_assigner.get_id()
        self.last_tag = properties['html_tag']
        self._text_type = properties['text_type']
        self._text = properties.get('text')
        self.dom = None
        self.text_dom = None

        self.block_stylesheet = True
    
        self.stylesheet = document.createElement("style")
        get_dom_node(form).appendChild(self.stylesheet)    
        self.other_stylesheet = document.createElement("style")
        get_dom_node(form).appendChild(self.other_stylesheet)   

        self.icon_stylesheet = document.createElement("style")
        get_dom_node(form).appendChild(self.icon_stylesheet)   
            
        self.create_dom(self.last_tag)

        self.block_stylesheet = False
        self.update_stylesheet()

        for event in self.events:
            self.dom.addEventListener(events_map[event], self.global_events_handler)
            
        if in_designer:
            self.css_properties['transition'] = "all 0.25s ease-in-out" #For smoother UI building

    def global_events_handler(self, e):
        self.form.raise_event(reverse_events_map[e.type], sender = self.form, event = e)
        
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
        previous_presets = self._preset or []
        
        previous_presets = previous_presets.copy()
            
        self._preset = value

        for preset in previous_presets:
            self.dom.classList.remove(preset)

        for preset in value:
            self.dom.classList.add(value)
        

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
        self.update_icon()

    @property
    def custom_icon(self):
        return self._custom_icon

    @custom_icon.setter
    def custom_icon(self, value):
        self._custom_icon = value
        self.update_icon()


    @property
    def icon_align(self):
        return self._icon_align

    @icon_align.setter
    def icon_align(self, value):
        self._icon_align = value
        self.update_icon()

    @property
    def icon_size(self):
        return self._icon_size

    @icon_size.setter
    def icon_size(self, value):
        self._icon_size = value
        self.update_icon()

    @property
    def icon_css(self):
        return self._icon_css

    @icon_css.setter
    def icon_css(self, value):
        self._icon_css = value
        self.icon_stylesheet.textContent = css_parser(value, f'#{self.uid} [nui-icon=true]')

    def update_icon(self):
        
        icon_el = self.dom.querySelector('[nui-icon="true"]')
        if icon_el:
            icon_el.remove()

        if self.custom_icon:
            icon_el = document.createElement("i")
            
            icon_el.innerHTML = self.custom_icon
            self.dom.appendChild(icon_el)
            
            

        elif self.icon and ":" in self.icon:
            lib, name = self.icon.split(":", 1)
            icon_el = document.createElement("i")
    
            if lib == 'bi':
                icon_el.className = f'bi bi-{name}'
                
            elif lib.startswith("fa"):
                icon_el.className = f'{lib} fa-{name}'
    
            elif lib == 'mi':
                icon_el.className = "material-icons"
                icon_el.textContent = name

            icon_el.style.fontSize = self.icon_size

        else:
            return
        icon_el.setAttribute("nui-icon", "true")
        
        align = self.icon_align
        
        
        icon_el.style.display = "inline-block"

        if align in ["left", "right"]:
            icon_el.style.verticalAlign = "middle"
        elif align in ["top", "bottom"]:
            icon_el.style.display = "block"
            #icon_el.style.margin = "auto"

        if align == "left":
            self.dom.insertBefore(icon_el, self.dom.firstChild)
        elif align == "right":
            self.dom.appendChild(icon_el)
        elif align == "top":
            self.dom.insertBefore(icon_el, self.dom.firstChild)
        elif align == "bottom":
            self.dom.appendChild(icon_el)

    def add_event(self, event_name, event_callback):
        
        def event_raiser(e):
            event_callback(sender = self.form, event = e)
            
        self.dom.addEventListener(event_name, event_raiser)

        
    def create_dom(self, tag):
        if self.dom:
            self.dom.remove()
        self.dom = document.createElement(tag)
        self.dom.id = self.uid
        get_dom_node(self.form).appendChild(self.dom)
        
    def set_property(self, name, value):
        self.css_properties[name] = value
        self.update_stylesheet()

    def update_stylesheet(self):
        if self.block_stylesheet:
            return

        properties = self.css_properties 

        css_rules = "\n".join(f"{key}: {value}" for key, value in properties.items())
        css_rules+="\n"+ (self.css or "")

        parsed_css = css_parser(css_rules, f"#{self.uid}")

        self.stylesheet.textContent = parsed_css
    
    def update_other_stylesheet(self):
        if self.block_stylesheet:
            return

        other_css = self.other_css or ""

        for state, css in self.states_css.items():
            if not css:
                continue
            other_css+=f"\n:{state}\n{(css)}"

        parsed_css = css_parser(other_css, f"#{self.uid}")

        self.other_stylesheet.textContent = parsed_css