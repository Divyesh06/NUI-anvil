from anvil.js.window import document
from anvil.js import get_dom_node, window
from .utils import px_convert, id_assigner
from .css_parser import css_parser
from anvil.designer import in_designer, get_design_name
from anvil import Media

events_map = {
    "hover": "mouseenter",
    "hover_out": "mouseleave",
    "click": "click",
    "change": "change",
    "input": "input",
    "focus": "focus",
    "lost_focus": "blur"
}

reverse_events_map = {v: k for k, v in events_map.items()}

class SuperComponent:
    def __init__(self, form, dom=None, events=[], **properties):
        self.form = form
        self.events = events
        self.is_container = False
        self.is_textbox = False
        self.is_textarea = False
        self._html_tag = None
        self._text = None
        self._source = None
        self._alt = None
        self._display_mode = None
        self._hover_css = None
        self._active_css = None
        self._focus_css = None
        self._placeholder_css = None
        self._disabled_css = None
        self._text_type = None
        self._font_size = None
        self._font = None
        self._type = None
        self._font_weight = None
        self._foreground = None
        self._background = None
        self._border_radius = None
        self._margin = None
        self._placeholder = None
        self._padding = None
        self._border_size = None
        self._border_style = None
        self._icon = None
        self._icon_align = None
        self._icon_size = None
        self._icon_css = None
        self._custom_icon = None
        self._border_color = None
        self._text_align = None
        self._css = None
        self._href = None
        self._target = None
        self._visible = None
        self._enabled = None
        self._preset = None
        self._true_html_structure = None
        self._children_css = None
        self._added_attrs = []
        self.css_properties = {}
        self.states_css = {}
        self.last_tag = None
        self.uid = id_assigner.get_id()
        self.last_tag = properties['html_tag']
        self._text_type = properties.get('text_type')
        self._text = properties.get('text')
        self.dom = None
        self.text_dom = None
        self.block_stylesheet = True

        # Initialize stylesheets as None - they'll be created only when needed
        self.other_stylesheet = None
        self.icon_stylesheet = None
        self.stylesheet = None
        self.children_stylesheet = None

        if not dom:
            self._create_dom(self.last_tag)
        else:
            self.dom = dom

        self.block_stylesheet = False
        self._update_stylesheet()

        for event in self.events:
            self.dom.addEventListener(events_map[event], self._global_events_handler)

        if in_designer:
            self.css_properties['transition'] = "all 0.25s ease-in-out"  # For smoother UI building
            self.designer_name = "Loading"
            self.form.add_event_handler("show", self._on_show_design)

        # for key,value in properties['attrs'].items():
        #     self.dom.setAttribute(key, value)

        self._add_component = form.add_component
        self._remove_component = form.remove_from_parent
        
        

    def _global_events_handler(self, e):
        self.form.raise_event(reverse_events_map[e.type], sender=self.form, event=e)

    def _refresh_components(self):
        components = self.form.get_components()
        self.form.clear()
        for comp in components:
            self.form.add_component(comp)

    @property
    def html_tag(self):
        return self._html_tag

    @html_tag.setter
    def html_tag(self, value):
        self._html_tag = value
        if value != self.last_tag:
            self._create_dom(value)
            self.last_tag = value
            self.text = self._text
            if self.is_container:
                self.dom.innerHTML = "Container children disappeared. Please add any component anywhere to see them again"
            self._update_stylesheet()

    @property
    def true_html_structure(self):
        return self._true_html_structure

    @true_html_structure.setter
    def true_html_structure(self, value):
        self._true_html_structure = value
        if value:
            if not in_designer:
                self.form.add_component = self.add_to_html_structure

    @property
    def alt(self):
        return self._alt

    @alt.setter
    def alt(self, value):
        self.dom.alt = value

    @property
    def href(self):
        return self._href

    @href.setter
    def href(self, value):
        self.dom.href = value

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self.dom.target = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        if isinstance(value, str):
            self.dom.src = value
        elif isinstance(value, Media):
            self.dom.src = window.URL.createObjectURL(window.Blob([value.get_bytes()], {type: value.content_type}))
        elif value:
            raise ValueError("Unsupported type of source")

    @property
    def display_mode(self):
        return self._display_mode

    @display_mode.setter
    def display_mode(self, value):
        self.set_property("object-fit", value)

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        if isinstance(value, str):
            self.dom.src = value
        elif isinstance(value, Media):
            self.dom.src = window.URL.createObjectURL(window.Blob([value.get_bytes()], {type: value.content_type}))
        elif value:
            raise ValueError("Unsupported type of source")
        
    def remove_from_parent(self):
        parent = self.form.parent
        if getattr(parent, "true_html_structure", False):
            self._remove_component()
            self.dom.remove()
        else:
            self._remove_component()

    def add_to_html_structure(self, child, **slot):
        from .Preset import Preset
        from .StyleSheet import StyleSheet
        from .PresetsContainer import PresetsContainer
        if isinstance(child, Preset) or isinstance(child, StyleSheet):
            
            self.dom.appendChild(child.presets_stylesheet)
            
        elif isinstance(child, PresetsContainer):
            self.dom.appendChild(get_dom_node(child).querySelector(".preset-container"))
            

        child_dom = get_dom_node(child)
        child_dom_nui = child_dom.querySelector(".nui")
        self._add_component(child)
        child_dom.remove()
        if child_dom_nui:
            self.dom.appendChild(child_dom_nui)
            for stylesheet in child_dom.querySelectorAll("style"):
                child_dom_nui.appendChild(stylesheet)
            for slot in self.dom.querySelectorAll('[anvil-name="container-slot"]'):
                slot.remove()
        

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        if not self.is_textbox:
            self._set_text()
        else:
            self.dom.value = value

    @property
    def placeholder(self):
        return self._placeholder

    @placeholder.setter
    def placeholder(self, value):
        self._placeholder = value
        self.dom.placeholder = value
        if in_designer:
            self._toggle_ghost_label()

    @property
    def text_type(self):
        return self._text_type

    @text_type.setter
    def text_type(self, value):
        self._text_type = value
        self._set_text()

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
        self.dom.type = value

    def _set_text(self):
        if self.is_textbox:
            return
        if in_designer:
            self._toggle_ghost_label()
        self.dom.innerText = self._text
        # else:
        #     self.dom.innerHTML = self._text
        if in_designer:
            self._toggle_ghost_label()
        self._update_icon()

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
        self.set_property("color", value.replace(" ", "_"))

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        self._background = value
        self.set_property("background-color", value.replace(" ", "_"))

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self.set_property("height", px_convert.convert_to_px(value))

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self.set_property("width", px_convert.convert_to_px(value))

    @property
    def border_radius(self):
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = value
        value = " ".join([px_convert.convert_to_px(v) for v in value.split()]) if isinstance(value, str) else px_convert.convert_to_px(value)
        self.set_property("border-radius", value)

    @property
    def margin(self):
        return self._margin

    @margin.setter
    def margin(self, value):
        self._margin = value
        value = " ".join([px_convert.convert_to_px(v) for v in value.split()]) if isinstance(value, str) else px_convert.convert_to_px(value)
        self.set_property("margin", value)

    @property
    def padding(self):
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = value
        value = " ".join([px_convert.convert_to_px(v) for v in value.split()]) if isinstance(value, str) else px_convert.convert_to_px(value)
        self.set_property("padding", value)

    @property
    def border_size(self):
        return self._border_size

    @border_size.setter
    def border_size(self, value):
        self._border_size = value
        value = " ".join([px_convert.convert_to_px(v) for v in value.split()]) if isinstance(value, str) else px_convert.convert_to_px(value)
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
        self.set_property("border-color", value.replace(" ", "_"))

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
        self._update_other_stylesheet()

    @property
    def hover_css(self):
        return self._hover_css

    @hover_css.setter
    def hover_css(self, value):
        self._hover_css = value
        self.states_css['hover'] = value
        self._update_other_stylesheet()

    @property
    def focus_css(self):
        return self._focus_css

    @focus_css.setter
    def focus_css(self, value):
        self._focus_css = value
        self.states_css['focus'] = value
        self._update_other_stylesheet()

    @property
    def placeholder_css(self):
        return self._placeholder_css

    @placeholder_css.setter
    def placeholder_css(self, value):
        self._placeholder_css = value
        self.states_css[':placeholder'] = value
        self._update_other_stylesheet()

    @property
    def disabled_css(self):
        return self._disabled_css

    @disabled_css.setter
    def disabled_css(self, value):
        self._disabled_css = value
        self.states_css['disabled'] = value
        self._update_other_stylesheet()

    @property
    def active_css(self):
        return self._active_css

    @active_css.setter
    def active_css(self, value):
        self._active_css = value
        self.states_css['active'] = value
        self._update_other_stylesheet()

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value
        if not in_designer:
            if not value:
                self.dom.style.background = "red"
                self.dom.style.display = "none"
            else:
                self.dom.style.background = ""
                self.dom.style.display = ""
        else:
            if not value:
                self.set_property("opacity", "0.3")
            else:
                self.set_property("opacity", "1")

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value
        self.dom.disabled = not value

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
            self.dom.classList.add(preset)

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
        self._update_icon()

    @property
    def custom_icon(self):
        return self._custom_icon

    @custom_icon.setter
    def custom_icon(self, value):
        self._custom_icon = value
        self._update_icon()

    @property
    def icon_align(self):
        return self._icon_align

    @icon_align.setter
    def icon_align(self, value):
        self._icon_align = value
        self._update_icon()

    @property
    def icon_size(self):
        return self._icon_size

    @icon_size.setter
    def icon_size(self, value):
        self._icon_size = px_convert.convert_to_px(value)
        self._update_icon()

    @property
    def children_css(self):
        return self._children_css

    @children_css.setter
    def children_css(self, value):
        self._children_css = value
        if value:
            if not self.children_stylesheet:
                self.children_stylesheet = document.createElement("style")
                get_dom_node(self.form).appendChild(self.children_stylesheet)
            self.children_stylesheet.textContent = css_parser(value, f'#{self.uid} [anvil-name="container-slot"]')
        elif self.children_stylesheet:
            self.children_stylesheet.textContent = ""
            # Optionally remove the stylesheet entirely if you want to clean up:
            # self.children_stylesheet.remove()
            # self.children_stylesheet = None

    @property
    def icon_css(self):
        return self._icon_css

    @icon_css.setter
    def icon_css(self, value):
        self._icon_css = value
        if value:
            if not self.icon_stylesheet:
                self.icon_stylesheet = document.createElement("style")
                get_dom_node(self.form).appendChild(self.icon_stylesheet)
            self.icon_stylesheet.textContent = css_parser(value, f'#{self.uid} [nui-icon=true]')
        elif self.icon_stylesheet:
            self.icon_stylesheet.textContent = ""
            # Optionally remove the stylesheet entirely if you want to clean up:
            # self.icon_stylesheet.remove()
            # self.icon_stylesheet = None

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        self._attributes = value
        for attr in self._added_attrs:
            self.dom.removeAttribute(attr)
      
        for attr in self._attributes:
            attr_key, attr_value = attr.split(":", 1)
            attr_key = attr_key.strip()
            attr_value = attr_value.strip()
            self._added_attrs.append(attr_key)
            self.dom.setAttribute(attr_key, attr_value)

    def _update_icon(self):
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
            if align in ["top", "bottom"]:
                icon_el.style.display = "block"
            # icon_el.style.margin = "auto"
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
            event_callback(sender=self.form, event=e)

        self.dom.addEventListener(event_name, event_raiser)

    def set_property(self, name, value):
        self.css_properties[name] = value
        self._update_stylesheet()

    def add_preset(self, value):
        if value not in self.preset:
            self.preset = self.preset + [value]

    def remove_preset(self, value):
        if value in self.preset:
            self.preset = [v for v in self.preset if v != value]

    def toggle_preset(self, value):
        if value in self.preset:
            self.remove_preset(value)
        else:
            self.add_preset(value)

    def _create_dom(self, tag):
        if self.dom:
            self.dom.remove()
        self.dom = document.createElement(tag)
        self.dom.id = self.uid
        self.dom.classList.add("nui")
        get_dom_node(self.form).appendChild(self.dom)

    def _update_stylesheet(self):
        if self.block_stylesheet:
            return
            
        properties = self.css_properties
        css_rules = "\n".join(f"{key}: {value}" for key, value in properties.items() if value)
        
        if css_rules:  # Only create stylesheet if there are actual rules
            if not self.stylesheet:
                self.stylesheet = document.createElement("style")
                get_dom_node(self.form).appendChild(self.stylesheet)
            parsed_css = css_parser(css_rules, f"#{self.uid}")
            self.stylesheet.textContent = parsed_css
        elif self.stylesheet:
            # Clear the stylesheet if no rules exist
            self.stylesheet.textContent = ""
            # Optionally remove the stylesheet entirely if you want to clean up:
            # self.stylesheet.remove()
            # self.stylesheet = None

    def _toggle_ghost_label(self):
        if self.is_container:
            return
        if self.is_textbox or self.is_textarea:
            if not self.placeholder and not self.text:
                self.dom.placeholder = self.designer_name
            else:
                self.dom.placeholder = self.placeholder
        else:
            if not self.text:
                self.dom.innerText = self.designer_name
                self.dom.style.color = "#aaa"
            else:
                self.dom.style.color = ""

    def _on_show_design(self, **event_args):
        self.designer_name = get_design_name(self.form)
        self._toggle_ghost_label()

    def _update_other_stylesheet(self):
        if self.block_stylesheet:
            return
            
        other_css = self.css or ""
        for state, css in self.states_css.items():
            if not css:
                continue
            other_css += f"\n:{state}\n{(css)}"
            
        if other_css.strip():  # Only create/update if there's actual CSS content
            if not self.other_stylesheet:
                self.other_stylesheet = document.createElement("style")
                get_dom_node(self.form).appendChild(self.other_stylesheet)
            parsed_css = css_parser(other_css, f"#{self.uid}")
            self.other_stylesheet.textContent = parsed_css
        elif self.other_stylesheet:
           
            self.other_stylesheet.textContent = ""
