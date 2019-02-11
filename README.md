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
        self._be_constructed_with('caca', id=32)

    def it_adds_correctly_the_numbers(self):
        self._get_wrapped_object()
        print(self.add(2, 3)._should_be(5))
```

## TODO

- Add more matchers
- Add prophecy behavior to easily mock collaborators
- Publish as a package
- Add a TAP output
