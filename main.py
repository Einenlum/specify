from examples.spec.calculator_spec import CalculatorSpec
from examples.spec.displayer_spec import DisplayerSpec
from runner import run_specs

run_specs([CalculatorSpec, DisplayerSpec])
