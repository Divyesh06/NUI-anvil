_D='change'
_C='focus'
_B=' '
_A=None
from anvil.js.window import document
from anvil.js import get_dom_node
from.utils import px_convert,id_assigner
from.css_parser import css_parser
from anvil.designer import in_designer,get_design_name
events_map={'hover':'mouseenter','hover_out':'mouseleave','click':'click',_D:_D,'input':'input',_C:_C,'lost_focus':'blur'}
reverse_events_map={B:A for(A,B)in events_map.items()}
class SuperComponent:
	def __init__(A,form,dom=_A,events=[],**E):
		D='style';C=False;B=form;A.form=B;A.events=events;A.is_container=C;A.is_textbox=C;A.is_textarea=C;A._html_tag=_A;A._text=_A;A._hover_css=_A;A._active_css=_A;A._focus_css=_A;A._placeholder_css=_A;A._disabled_css=_A;A._text_type=_A;A._font_size=_A;A._font=_A;A._type=_A;A._font_weight=_A;A._foreground=_A;A._background=_A;A._border_radius=_A;A._margin=_A;A._placeholder=_A;A._padding=_A;A._border_size=_A;A._border_style=_A;A._icon=_A;A._icon_align=_A;A._icon_size=_A;A._icon_css=_A;A._custom_icon=_A;A._border_color=_A;A._text_align=_A;A._css=_A;A._visible=_A;A._enabled=_A;A._preset=_A;A._children_css=_A;A.css_properties={};A.states_css={};A.last_tag=_A;A.uid=id_assigner.get_id();A.last_tag=E['html_tag'];A._text_type=E.get('text_type');A._text=E.get('text');A.dom=_A;A.text_dom=_A;A.block_stylesheet=True;A.other_stylesheet=document.createElement(D);get_dom_node(B).appendChild(A.other_stylesheet);A.icon_stylesheet=document.createElement(D);get_dom_node(B).appendChild(A.icon_stylesheet);A.stylesheet=document.createElement(D);get_dom_node(B).appendChild(A.stylesheet);A.children_stylesheet=document.createElement(D);get_dom_node(B).appendChild(A.children_stylesheet)
		if not dom:A._create_dom(A.last_tag)
		else:A.dom=dom
		A.block_stylesheet=C;A._update_stylesheet()
		for F in A.events:A.dom.addEventListener(events_map[F],A._global_events_handler)
		if in_designer:A.css_properties['transition']='all 0.25s ease-in-out';A.designer_name='Loading';A.form.add_event_handler('show',A._on_show_design)
	def _global_events_handler(A,e):A.form.raise_event(reverse_events_map[e.type],sender=A.form,event=e)
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
		if A._text_type=='plain':A.dom.innerText=A._text
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
	def margin(self,value):A=value;self._margin=A;A=_B.join([px_convert.convert_to_px(A)for A in A.split()])if isinstance(A,str)else px_convert.convert_to_px(A);self.set_property('margin',A)
	@property
	def padding(self):return self._padding
	@padding.setter
	def padding(self,value):A=value;self._padding=A;A=_B.join([px_convert.convert_to_px(A)for A in A.split()])if isinstance(A,str)else px_convert.convert_to_px(A);self.set_property('padding',A)
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
	def focus_css(self,value):B=value;A=self;A._focus_css=B;A.states_css[_C]=B;A._update_other_stylesheet()
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
		D='opacity';C='display';B=value;A=self;A._visible=B
		if not in_designer:
			if not B:A.set_property(C,'none')
			else:A.set_property(C,'')
		elif not B:A.set_property(D,'0.3')
		else:A.set_property(D,'1')
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
	def icon(self,value):self._icon=value;self._update_icon()
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
	def children_css(self,value):B=value;A=self;A._children_css=B;A.children_stylesheet.textContent=css_parser(B,f'#{A.uid} [anvil-name="container-slot"]')
	@property
	def icon_css(self):return self._icon_css
	@icon_css.setter
	def icon_css(self,value):B=value;A=self;A._icon_css=B;A.icon_stylesheet.textContent=css_parser(B,f"#{A.uid} [nui-icon=true]")
	def _update_icon(B):
		G='bottom';F='top';A=B.dom.querySelector('[nui-icon="true"]')
		if A:A.remove()
		if B.custom_icon:A=document.createElement('i');A.innerHTML=B.custom_icon;B.dom.appendChild(A)
		elif B.icon and':'in B.icon:
			D,E=B.icon.split(':',1);A=document.createElement('i')
			if D=='bi':A.className=f"bi bi-{E}"
			elif D.startswith('fa'):A.className=f"{D} fa-{E}"
			elif D=='mi':A.className='material-icons';A.textContent=E
			A.style.fontSize=B.icon_size
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
	def set_property(A,name,value):A.css_properties[name]=value;A._update_stylesheet()
	def add_preset(A,value):
		B=value
		if B not in A.preset:A.preset=A.preset+[B]
	def remove_preset(A,value):
		B=value
		if B in A.preset:A.preset=[i for i in A.preset if i!=B]
	def toggle_preset(A,value):
		B=value
		if B in A.preset:A.remove_preset(B)
		else:A.add_preset(B)
	def _create_dom(A,tag):
		if A.dom:A.dom.remove()
		A.dom=document.createElement(tag);A.dom.id=A.uid;get_dom_node(A.form).appendChild(A.dom)
	def _update_stylesheet(A):
		if A.block_stylesheet:return
		C=A.css_properties;B='\n'.join(f"{A}: {B}"for(A,B)in C.items());B+='\n'+(A.css or'');D=css_parser(B,f"#{A.uid}");A.stylesheet.textContent=D
	def _toggle_ghost_label(A):
		if A.is_container:return
		if A.is_textbox or A.is_textarea:
			if not A.placeholder and not A.text:A.dom.placeholder=A.designer_name
			else:A.dom.placeholder=A.placeholder
		elif not A.text:A.dom.innerText=A.designer_name;A.dom.style.color='#aaa'
		else:A.dom.style.color=''
	def _on_show_design(A,**B):A.designer_name=get_design_name(A.form);A._toggle_ghost_label()
	def _update_other_stylesheet(A):
		if A.block_stylesheet:return
		B=A.css or''
		for(D,C)in A.states_css.items():
			if not C:continue
			B+=f"\n:{D}\n{C}"
		E=css_parser(B,f"#{A.uid}");A.other_stylesheet.textContent=E