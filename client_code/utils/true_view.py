from anvil.designer import in_designer

true_view_funcs = []

def true_view(func):
    true_view_funcs.append(func)
    return func

def raise_all(state):
    if in_designer:
        for func in true_view_funcs:
            func(state)