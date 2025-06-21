def convert_to_px(value):
    if isinstance(value, int):
        return f"{value}px"
    if value.isnumeric():
        value = value+"px"
    return value