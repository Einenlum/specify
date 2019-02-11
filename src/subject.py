from .builtin_matchers import get_matcher

class Subject:
    def __init__(self, value):
        self.__value = value

    def _get_value(self):
        return self.__value

    def __getattr__(self, attr_name):
        if attr_name.startswith('_should_'):
            matcher_type = attr_name[len('_should_'):]
            matcher = get_matcher(matcher_type)
            def checker_wrapper(expected_value):
                return matcher(self.__value, expected_value)
            return checker_wrapper

        def action_wrapper(*args, **kwargs):
            return Subject(getattr(self.__value, attr_name)(*args, **kwargs))

        return action_wrapper
