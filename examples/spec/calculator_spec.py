from src.object_behavior import ObjectBehavior
from examples.calculator import Calculator

class CalculatorSpec(ObjectBehavior):
    def _let(self):
        self._describe(Calculator)
        self._be_constructed_with('lorem', id=32)

    def it_adds_the_numbers(self):
        self.add(2, 3)._should_be(5)
