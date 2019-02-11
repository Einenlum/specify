from typing import List
from src.object_behavior import ObjectBehavior

def run_spec(spec_class: ObjectBehavior):
    spec = spec_class()
    tests = [func for func in dir(spec) if func.startswith('it_') and callable(getattr(spec, func))]
    for test in tests:
        spec._let()
        getattr(spec, test)()
        spec._let_go()

def run_specs(specs: List[ObjectBehavior]):
    for spec in specs:
        run_spec(spec)
