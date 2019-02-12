class Calculator:
    '''
    A really simple class to give examples to spec
    '''
    def __init__(self, name, **kwargs):
        self.name = name
        self.values = kwargs

    def multiply(self, *args):
        product = 1
        for arg in args:
            product = product * arg

        return product

    def add(self, *args):
        return sum(args)
