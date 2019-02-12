from .calculator import Calculator

class Displayer:
    '''
    A really simple class to give examples to spec
    '''
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def display_addition(self, *args) -> str:
        total = str(self.calculator.add(*args))
        args = [str(arg) for arg in args]

        return f"{' + '.join(args)} = {total}"
