from src.object_behavior import ObjectBehavior
from examples.calculator import Calculator
from examples.displayer import Displayer
from src.prophepy import prophesize

class DisplayerSpec(ObjectBehavior):
    def _let(self):
        self._describe(Displayer)
        self.__calculator = prophesize(Calculator)
        self._be_constructed_with(self.__calculator._reveal())

    def it_displays_addition(self):
        self.__calculator.add(2, 3)._should_be_called()
        self.__calculator.add(2, 3)._will_return(5)
        self.display_addition(2, 3)._should_be_like('2 + 3 = 5')
        self.__calculator.check_prophecies()
