from specify import ObjectBehavior, mock
from examples.calculator import Calculator
from examples.displayer import Displayer

class DisplayerSpec(ObjectBehavior):

    @mock(Calculator)
    def _let(self, calculator):
        self._describe(Displayer)
        self._be_constructed_with(calculator)
        self.__calculator = calculator

    def it_displays_addition(self):
        self.__calculator.add(2, 3)._should_be_called()
        self.__calculator.add(2, 3)._will_return(5)
        self.display_addition(2, 3)._should_be_like('2 + 3 = 5')
