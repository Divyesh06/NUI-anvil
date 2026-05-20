def convert_to_px(value):
	A=value
	if isinstance(A,int):return f"{A}px"
	if A.isnumeric():A=A+'px'
	return A