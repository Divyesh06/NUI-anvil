from anvil.js import window
import re
anvil_theme_vars=window.anvilThemeVars
def css_parser(raw_css,main_selector):
	J=':';I=' ';F=raw_css;B=main_selector
	if not F:return''
	F=F.replace('{','').replace('}','');L=[A.lstrip()for A in re.split('[;\\n]+',F)if A.strip()];K=[];C=B;G=None;D=[]
	def M(value):
		D='theme:';B=value
		if D not in B:return B
		C=B.split()
		for(G,E)in enumerate(C):
			if E.startswith(D):
				F=E[len(D):].strip();A=anvil_theme_vars.get(F.replace('_',I))
				if not A:A=anvil_theme_vars.get(F)
				if A:C[G]=f"var({A})"
		return I.join(C)
	def H():
		if not D:return
		A=[]
		for F in D:
			if J not in F:continue
			H,B=map(str.strip,F.split(J,1));B=M(B);A.append(f"{H}: {B}")
		if not A:return
		I='; '.join(A);E=f"{C} {{\n  {I};\n}}"
		if G:E=f"{G} {{\n  {E}\n}}"
		K.append(E)
	def N(line):return re.match('^[\\w-]+\\s*:',line)
	for E in L:
		if N(E):D.append(E)
		elif E.startswith('@'):H();G=E;C=B;D=[]
		else:
			H();A=E.rstrip()
			if A.startswith('&'):C=A.replace('&',B)
			elif A[:1]in('>','+','~','[',J,'.','#')or A.startswith(I):C=f"{B}{A}"
			else:C=f"{B} {A}"
			D=[]
	H();return'\n\n'.join(K)
from.import default_presets