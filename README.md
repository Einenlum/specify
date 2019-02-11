# spyec

A very rudimentary PHPSpec-like for Python. For fun only (for now). If you're looking for a real valid PHPSpec-like, you could check [flowp](http://pawelgalazka.github.io/flowp/testing.html) (but deprecated). [mamba](https://nestorsalceda.com/mamba/) could also interest you, even if it's not exactly what you are searching.

## Usage

You can check the [examples](examples) folder.

```python
from spyec import ObjectBehavior
from examples.calculator import Calculator

class CalculatorSpec(ObjectBehavior):
    def _let(self):
        self._describe(Calculator)
        self._be_constructed_with('lorem', id=32)

    def it_adds_the_numbers(self):
        self.add(2, 3)._should_be(5)
```

It will render a valid TAP output (hopefully).

```
TAP version 13
1..1

ok 1 - CalculatorSpec: it adds the numbers
```

To have a nice and pretty output, you can then use a TAP formatter like [faucet](https://www.npmjs.com/package/faucet).

## Builtin matchers

- `_should_be` (check with `is`)
- `_should_be_like` (check with `==`)

## Custom matchers

You can implement a `_matchers` function in your spec, to add custom matchers.

The key of the matcher is left trimmed by `should_` and the first argument
passed to your function is the value itself.

If you return false, the test will fail.

Here is an example:

```python
class CalculatorSpec(ObjectBehavior):
    # ...

    def it_adds_the_numbers(self):
        self.add(2, 3)._should_be_a_number()
        self.add(2, 3)._should_be_greater_than(10)

    def _matchers(self):
        def be_a_number(value, *args):
            return isinstance(value, int)

        def be_greater_than(value, expected_value):
            return value > expected_value

        return {
            'be_a_number': be_a_number,
            'be_greater_than': be_greater_than
        }
```

## TODO

- Add more matchers
- Add prophecy behavior to easily mock collaborators
- Publish as a package
- Make the tap output a stream as the spec say
