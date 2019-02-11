from typing import List

class ResultLine:
    def __init__(self, spec_class, test_name, exception=None):
        self.spec_class = spec_class
        self.test_name = test_name
        self.exception = exception

class Result:
    def __init__(self, result_lines: List[ResultLine]):
        self.result_lines = result_lines

    def _prettify_test_name(self, test_name):
        return test_name.replace('_', ' ')

    def _print_line(self, num: int, line: ResultLine):
        if line.exception is None:
            prefix = 'ok'
        else:
            prefix = 'not ok'

        desc = f"{line.spec_class.__qualname__}: {self._prettify_test_name(line.test_name)}"
        text = f"{prefix} {num} - {desc}"

        if line.exception is not None:
            text = text + "\n    ---"
            text = text + "\n    " + line.exception
            text = text + "\n    ..."

        return text

    def export(self):
        text = "TAP version 13\n"
        last_elem = len(self.result_lines)
        text = text + f"1..{last_elem}\n"

        for index, line in enumerate(self.result_lines):
            text = text + "\n" + self._print_line(index+1, line)

        return text
