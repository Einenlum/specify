class Calculator:
    def __init__(self, name, **kwargs):
        self.name = name
        self.values = kwargs

    def add(self, *args):
        return sum(args)
