def be(value, expected):
    if value is not expected:
        raise Exception(f"Expected {value} to be {expected}")

def be_like(value, expected):
    if value != expected:
        raise Exception(f"Expected {value} to be like {expected}")

def get_matcher(type):
    items = {
        'be': be,
        'be_like': be_like
    }

    if type not in items:
        raise Exception(f'No builtin matcher exists with type "{type}"')

    return items[type]
