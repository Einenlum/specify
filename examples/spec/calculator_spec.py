from specify.object_behavior import ObjectBehavior
from examples.calculator import Calculator

class CalculatorSpec(ObjectBehavior):
    def _let(self):
        self._describe(Calculator)
        self._be_constructed_with('lorem', id=32)

    def it_adds_the_numbers(self):
        self.add(2, 3)._should_be(5)
        self.add(2, 3)._should_be_a_number()._should_be_greater_than(0)

    def _matchers(self):
        def be_a_number(value, *args):
            return isinstance(value, int)

        def be_greater_than(value, expected_value):
            return value > expected_value

        return {
            'be_a_number': be_a_number,
            'be_greater_than': be_greater_than
        }
