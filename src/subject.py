class Subject:
    def __init__(self, value):
        self.__value = value

    def _get_value(self):
        return value

    def __getattr__(self, attr_name):
        if attr_name == '_should_be':
            def checker_wrapper(expected_value):
                if self.__value != expected_value:
                    raise Exception(f"Expected value: {expected_value}, got {self.__value}")
            return checker_wrapper

        def action_wrapper(*args, **kwargs):
            return Subject(getattr(self.__value, attr_name)(*args, **kwargs))

        return action_wrapper
