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

## TODO

- Add more matchers
- Add prophecy behavior to easily mock collaborators
- Publish as a package
- Make the tap output a stream as the spec say
