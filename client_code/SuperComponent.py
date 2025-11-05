_H='Unsupported type of source'
_G='change'
_F='focus'
_E='style'
_D='margin'
_C=False
_B=' '
_A=None
from anvil.js.window import document
from anvil.js import get_dom_node,window
from.utils import px_convert,id_assigner
from.css_parser import css_parser
from anvil.designer import in_designer,get_design_name,update_component_properties
from anvil import Media,alert
from.utils import true_view
events_map={'hover':'mouseenter','hover_out':'mouseleave','click':'click',_G:_G,'input':'input',_F:_F,'lost_focus':'blur'}
reverse_events_map={B:A for(A,B)in events_map.items()}
class SuperComponent:
	def __init__(A,form,dom=_A,events=[],is_container=_C,**C):
		B=form;A.form=B;A.events=events;A.is_container=is_container;A.is_textbox=_C;A.is_textarea=_C;A.is_nui=True;A._html_tag=_A;A._text=_A;A._source=_A;A._alt=_A;A._display_mode=_A;A._hover_css=_A;A._active_css=_A;A._focus_css=_A;A._placeholder_css=_A;A._disabled_css=_A;A._text_type=_A;A._font_size=_A;A._font=_A;A._type=_A;A._font_weight=_A;A._foreground=_A;A._background=_A;A._border_radius=_A;A._margin=_A;A._placeholder=_A;A._padding=_A;A._border_size=_A;A._border_style=_A;A._icon=_A;A._icon_align=_A;A._icon_size=_A;A._icon_css=_A;A._custom_icon=_A;A._border_color=_A;A._text_align=_A;A._css=_A;A._href=_A;A._target=_A;A._visible=_A;A._enabled=_A;A._preset=_A;A._true_html_structure=_A;A._children_css=_A;A._added_attrs=[];A.css_properties={};A.states_css={};A.last_tag=_A;A.uid=id_assigner.get_id();A.last_tag=C['html_tag'];A._text_type=C.get('text_type');A._text=C.get('text');A.dom=_A;A.text_dom=_A;A.block_stylesheet=True;A.stylesheets=[];A.other_stylesheet=_A;A.icon_stylesheet=_A;A.stylesheet=_A;A.children_stylesheet=_A;A.true_view=_C
		if not dom:A._create_dom(A.last_tag)
		else:A.dom=dom
		A.block_stylesheet=_C;A._update_stylesheet()
		for D in A.events:A.dom.addEventListener(events_map[D],A._global_events_handler)
		if in_designer:A.css_properties['transition']='all 0.25s ease-in-out';A.designer_name='Loading';A.form.add_event_handler('show',A._on_show_design)
		@true_view.true_view
		def E(state):A.true_view=state;A._toggle_ghost_label()
		A._add_component=B.add_component;A._remove_component=B.remove_from_parent
	def _global_events_handler(A,e):A.form.raise_event(reverse_events_map[e.type],sender=A.form,event=e)
	def _refresh_components(A):
		B=A.form.get_components();A.form.clear()
		for C in B:A.form.add_component(C)
	@property
	def html_tag(self):return self._html_tag
	@html_tag.setter
	def html_tag(self,value):
		B=value;A=self;A._html_tag=B
		if B!=A.last_tag:
			A._create_dom(B);A.last_tag=B;A.text=A._text
			if A.is_container:A.dom.innerHTML='Container children disappeared. Please add any component anywhere to see them again'
			A._update_stylesheet()
	@property
	def true_html_structure(self):return self._true_html_structure
	@true_html_structure.setter
	def true_html_structure(self,value):
		B=value;A=self;A._true_html_structure=B
		if B and(not in_designer or A.true_view):A.form.add_component=A.add_to_html_structure
		else:A.form.add_component=A._add_component
		A.children_css=A._children_css
	@property
	def alt(self):return self._alt
	@alt.setter
	def alt(self,value):self.dom.alt=value
	@property
	def href(self):return self._href
	@href.setter
	def href(self,value):self.dom.href=value
	@property
	def target(self):return self._target
	@target.setter
	def target(self,value):self.dom.target=value
	@property
	def source(self):return self._source
	@source.setter
	def source(self,value):
		A=value
		if isinstance(A,str):self.dom.src=A
		elif isinstance(A,Media):self.dom.src=window.URL.createObjectURL(window.Blob([A.get_bytes()],{type:A.content_type}))
		elif A:raise ValueError(_H)
	@property
	def display_mode(self):return self._display_mode
	@display_mode.setter
	def display_mode(self,value):self.set_property('object-fit',value)
	@property
	def source(self):return self._source
	@source.setter
	def source(self,value):
		A=value
		if isinstance(A,str):self.dom.src=A
		elif isinstance(A,Media):self.dom.src=window.URL.createObjectURL(window.Blob([A.get_bytes()],{type:A.content_type}))
		elif A:raise ValueError(_H)
	def remove_from_parent(A):
		B=A.form.parent
		if getattr(B,'true_html_structure',_C):
			A._remove_component();A.dom.remove()
			for C in A.stylesheets:C.remove()
		else:A._remove_component()
	def add_to_html_structure(B,child,**C):
		A=child
		if not hasattr(A,'is_nui'):
			if in_designer:
				if not A.parent:B.form._add_component(A,**C)
			else:B.form._add_component(A,**C)
		else:
			if in_designer:
				if not A.parent:B.form._add_component(A,**C)
			else:B.form._add_component(A,**C)
			E=B.form.get_components().index(A);G=get_dom_node(A);D=A.dom
			if D:
				for C in B.dom.querySelectorAll('[anvil-name="container-slot"]'):
					if C.contains(D):C.remove()
				B.dom.insertBefore(D,B.dom.children[E])
				for F in A.stylesheets:B.dom.appendChild(F)
	@property
	def text(self):return self._text
	@text.setter
	def text(self,value):
		B=value;A=self;A._text=B
		if not A.is_textbox:A._set_text()
		else:A.dom.value=B
	@property
	def placeholder(self):return self._placeholder
	@placeholder.setter
	def placeholder(self,value):
		B=value;A=self;A._placeholder=B;A.dom.placeholder=B
		if in_designer:A._toggle_ghost_label()
	@property
	def text_type(self):return self._text_type
	@text_type.setter
	def text_type(self,value):self._text_type=value;self._set_text()
	@property
	def type(self):return self._type
	@type.setter
	def type(self,value):A=value;self._type=A;self.dom.type=A
	def _set_text(A):
		if A.is_textbox:return
		if in_designer:A._toggle_ghost_label()
		if A.text_type!='html':A.dom.textContent=A._text
		else:A.dom.innerHTML=A._text
		if in_designer:A._toggle_ghost_label()
		A._update_icon()
	@property
	def font_size(self):return self._font_size
	@font_size.setter
	def font_size(self,value):A=value;self._font_size=A;self.set_property('font-size',px_convert.convert_to_px(A))
	@property
	def font(self):return self._font
	@font.setter
	def font(self,value):A=value;self._font=A;self.set_property('font-family',A)
	@property
	def font_weight(self):return self._font_weight
	@font_weight.setter
	def font_weight(self,value):A=value;self._font_weight=A;self.set_property('font-weight',A)
	@property
	def foreground(self):return self._foreground
	@foreground.setter
	def foreground(self,value):A=value;self._foreground=A;self.set_property('color',A.replace(_B,'_'))
	@property
	def background(self):return self._background
	@background.setter
	def background(self,value):A=value;self._background=A;self.set_property('background-color',A.replace(_B,'_'))
	@property
	def height(self):return self._height
	@height.setter
	def height(self,value):A=value;self._height=A;self.set_property('height',px_convert.convert_to_px(A))
	@property
	def width(self):return self._width
	@width.setter
	def width(self,value):A=value;self._width=A;self.set_property('width',px_convert.convert_to_px(A))
	@property
	def border_radius(self):return self._border_radius
	@border_radius.setter
	def border_radius(self,value):A=value;self._border_radius=A;A=_B.join([px_convert.convert_to_px(A)for A in A.split()])if isinstance(A,str)else px_convert.convert_to_px(A);self.set_property('border-radius',A)
	@property
	def margin(self):return self._margin
	@margin.setter
	def margin(self,value):
		A=value;self._margin=A
		if not A:return
		if isinstance(A,list):A=_B.join([px_convert.convert_to_px(str(A if A else 0))for A in A])
		else:A=_B.join([px_convert.convert_to_px(A)for A in A.split()])if isinstance(A,str)else px_convert.convert_to_px(A)
		self.set_property(_D,A)
	@property
	def padding(self):return self._padding
	@padding.setter
	def padding(self,value):
		B=self;A=value;B._padding=A
		if not A:return
		if isinstance(A,list):A=_B.join([px_convert.convert_to_px(str(A if A else 0))for A in A])
		else:A=_B.join([px_convert.convert_to_px(A)for A in A.split()])if isinstance(A,str)else px_convert.convert_to_px(A)
		B.set_property('padding',A)
		if _D in A:
			if isinstance(A[_D],list):B.margin=_B.join([str(A if A else 0)for A in A[_D]])
			else:B.margin=px_convert.convert_to_px(A[_D])
			if in_designer:
				try:update_component_properties(B.form,{_D:B.margin})
				except:pass
	@property
	def border_size(self):return self._border_size
	@border_size.setter
	def border_size(self,value):A=value;self._border_size=A;A=_B.join([px_convert.convert_to_px(A)for A in A.split()])if isinstance(A,str)else px_convert.convert_to_px(A);self.set_property('border-width',A)
	@property
	def border_style(self):return self._border_style
	@border_style.setter
	def border_style(self,value):A=value;self._border_style=A;self.set_property('border-style',A)
	@property
	def border_color(self):return self._border_color
	@border_color.setter
	def border_color(self,value):A=value;self._border_color=A;self.set_property('border-color',A.replace(_B,'_'))
	@property
	def text_align(self):return self._text_align
	@text_align.setter
	def text_align(self,value):A=value;self._text_align=A;self.set_property('text-align',A)
	@property
	def css(self):return self._css
	@css.setter
	def css(self,value):self._css=value;self._update_other_stylesheet()
	@property
	def hover_css(self):return self._hover_css
	@hover_css.setter
	def hover_css(self,value):B=value;A=self;A._hover_css=B;A.states_css['hover']=B;A._update_other_stylesheet()
	@property
	def focus_css(self):return self._focus_css
	@focus_css.setter
	def focus_css(self,value):B=value;A=self;A._focus_css=B;A.states_css[_F]=B;A._update_other_stylesheet()
	@property
	def placeholder_css(self):return self._placeholder_css
	@placeholder_css.setter
	def placeholder_css(self,value):B=value;A=self;A._placeholder_css=B;A.states_css[':placeholder']=B;A._update_other_stylesheet()
	@property
	def disabled_css(self):return self._disabled_css
	@disabled_css.setter
	def disabled_css(self,value):B=value;A=self;A._disabled_css=B;A.states_css['disabled']=B;A._update_other_stylesheet()
	@property
	def active_css(self):return self._active_css
	@active_css.setter
	def active_css(self,value):B=value;A=self;A._active_css=B;A.states_css['active']=B;A._update_other_stylesheet()
	@property
	def visible(self):return self._visible
	@visible.setter
	def visible(self,value):
		C='opacity';B=value;A=self;A._visible=B
		if not in_designer:
			if not B:A.dom.style.background='red';A.dom.style.display='none'
			else:A.dom.style.background='';A.dom.style.display=''
		elif not B:A.set_property(C,'0.3')
		else:A.set_property(C,'1')
	@property
	def enabled(self):return self._enabled
	@enabled.setter
	def enabled(self,value):A=value;self._enabled=A;self.dom.disabled=not A
	@property
	def preset(self):return self._preset
	@preset.setter
	def preset(self,value):
		D=value;A=self;B=A._preset or[];B=B.copy();A._preset=D
		for C in B:A.dom.classList.remove(C)
		for C in D:A.dom.classList.add(C)
	@property
	def icon(self):return self._icon
	@icon.setter
	def icon(self,value):
		A=self;A._icon=value
		if in_designer:A._toggle_ghost_label()
		A._update_icon()
	@property
	def custom_icon(self):return self._custom_icon
	@custom_icon.setter
	def custom_icon(self,value):self._custom_icon=value;self._update_icon()
	@property
	def icon_align(self):return self._icon_align
	@icon_align.setter
	def icon_align(self,value):self._icon_align=value;self._update_icon()
	@property
	def icon_size(self):return self._icon_size
	@icon_size.setter
	def icon_size(self,value):self._icon_size=px_convert.convert_to_px(value);self._update_icon()
	@property
	def children_css(self):return self._children_css
	@children_css.setter
	def children_css(self,value):
		B=value;A=self;A._children_css=B
		if B:
			if not A.children_stylesheet:A.children_stylesheet=document.createElement(_E);get_dom_node(A.form).appendChild(A.children_stylesheet);A.stylesheets.append(A.children_stylesheet)
			if not A.true_html_structure:A.children_stylesheet.textContent=css_parser(B,f'#{A.uid}>[anvil-name="container-slot"]')
			else:A.children_stylesheet.textContent=css_parser(B,f"#{A.uid}>*")
		elif A.children_stylesheet:A.children_stylesheet.textContent=''
	@property
	def icon_css(self):return self._icon_css
	@icon_css.setter
	def icon_css(self,value):
		B=value;A=self;A._icon_css=B
		if B:
			if not A.icon_stylesheet:A.icon_stylesheet=document.createElement(_E);get_dom_node(A.form).appendChild(A.icon_stylesheet);A.stylesheets.append(A.icon_stylesheet)
			A.icon_stylesheet.textContent=css_parser(B,f"#{A.uid} [nui-icon=true]")
		elif A.icon_stylesheet:A.icon_stylesheet.textContent=''
	@property
	def attributes(self):return self._attributes
	@attributes.setter
	def attributes(self,value):
		A=self;A._attributes=value
		for B in A._added_attrs:A.dom.removeAttribute(B)
		for B in A._attributes:print(B);C,D=B.split(':',1);C=C.strip();D=D.strip();A._added_attrs.append(C);A.dom.setAttribute(C,D)
	def _update_icon(B):
		G='bottom';F='top';A=B.dom.querySelector('[nui-icon="true"]')
		if A:A.remove()
		if B.custom_icon:A=document.createElement('i');A.innerHTML=B.custom_icon;B.dom.appendChild(A)
		elif B.icon and':'in B.icon:
			D,E=B.icon.split(':',1);A=document.createElement('i')
			if D=='bi':A.className=f"bi bi-{E}"
			elif D.startswith('fa'):A.className=f"{D} fa-{E}"
			elif D=='mi':A.className='material-icons';A.textContent=E;A.style.fontSize=B.icon_size
			else:return
			A.setAttribute('nui-icon','true');C=B.icon_align;A.style.display='inline-block'
			if C in[F,G]:A.style.display='block'
			if C=='left':B.dom.insertBefore(A,B.dom.firstChild)
			elif C=='right':B.dom.appendChild(A)
			elif C==F:B.dom.insertBefore(A,B.dom.firstChild)
			elif C==G:B.dom.appendChild(A)
	def add_event(A,event_name,event_callback):
		def B(e):event_callback(sender=A.form,event=e)
		A.dom.addEventListener(event_name,B)
	def add_attribute(A,name,value=''):
		B=name
		if B not in A._added_attrs:A._added_attrs.append(B)
		A.dom.setAttribute(B,value)
	def remove_attribute(A,name):
		B=name
		if B in A._added_attrs:A._added_attrs.remove(B)
		A.dom.removeAttribute(B)
	def set_property(A,name,value):A.css_properties[name]=value;A._update_stylesheet()
	def add_preset(A,value):
		B=value
		if B not in A.preset:A.preset=A.preset+[B]
	def remove_preset(A,value):
		B=value
		if B in A.preset:A.preset=[A for A in A.preset if A!=B]
	def toggle_preset(A,value):
		B=value
		if B in A.preset:A.remove_preset(B)
		else:A.add_preset(B)
	def _create_dom(A,tag):
		if A.dom:A.dom.remove()
		A.dom=document.createElement(tag);A.dom.id=A.uid;A.dom.classList.add('nui')
		if A.is_container and in_designer:A.dom.classList.add('nui-container')
		get_dom_node(A.form).appendChild(A.dom)
	def _update_stylesheet(A):
		if A.block_stylesheet:return
		C=A.css_properties;B='\n'.join(f"{B}: {A}"for(B,A)in C.items()if A)
		if B:
			if not A.stylesheet:A.stylesheet=document.createElement(_E);get_dom_node(A.form).appendChild(A.stylesheet);A.stylesheets.append(A.stylesheet)
			D=css_parser(B,f"#{A.uid}");A.stylesheet.textContent=D
		elif A.stylesheet:A.stylesheet.textContent=''
	def _toggle_ghost_label(A):
		if A.is_container:return
		if A.is_textbox or A.is_textarea:
			if not A.placeholder and not A.text and not A.true_view:A.dom.placeholder=A.designer_name
			else:A.dom.placeholder=A.placeholder
		elif not A.text and not A.true_view and(not A.is_textbox and not A.is_textarea and not A.icon):A.dom.textContent=A.designer_name;A.dom.style.color='#aaa'
		else:
			A.dom.style.color=''
			if A.text_type!='html':A.dom.textContent=A.text
			else:A.dom.innerHTML=A.text
	def _on_show_design(A,**B):A.designer_name=get_design_name(A.form);A._toggle_ghost_label()
	def _update_other_stylesheet(A):
		if A.block_stylesheet:return
		B=A.css or''
		for(D,C)in A.states_css.items():
			if not C:continue
			B+=f"\n:{D}\n{C}"
		if B.strip():
			if not A.other_stylesheet:A.other_stylesheet=document.createElement(_E);get_dom_node(A.form).appendChild(A.other_stylesheet);A.stylesheets.append(A.other_stylesheet)
			E=css_parser(B,f"#{A.uid}");A.other_stylesheet.textContent=E
		elif A.other_stylesheet:A.other_stylesheet.textContent=''