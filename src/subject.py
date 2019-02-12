from .builtin_matchers import get_matcher
from .exceptions import CustomMatcherError

class Subject:
    def __init__(self, value, object_behavior):
        self.__value = value
        self.__object_behavior = object_behavior

    def _get_value(self):
        return self.__value

    def match_with_custom_matcher(self, matcher_name, matcher, *args):
        if not matcher(self.__value, *args):
            raise CustomMatcherError(f'Custom matcher "{matcher_name}" failed.')

        return self.__value

    def __getattr__(self, attr_name):
        if attr_name.startswith('_should_'):
            matcher_type = attr_name[len('_should_'):]

            # custom matcher
            if matcher_type in self.__object_behavior._matchers().keys():
                matcher = self.__object_behavior._matchers()[matcher_type]
                def custom_matcher_wrapper(*args):
                    return Subject(
                        self.match_with_custom_matcher(matcher_type, matcher, *args),
                        self.__object_behavior
                    )
                return custom_matcher_wrapper

            # builtin matcher
            matcher = get_matcher(matcher_type)
            def checker_wrapper(expected_value):
                return Subject(
                    matcher(self.__value, expected_value),
                    self.__object_behavior
                )
            return checker_wrapper

        def action_wrapper(*args, **kwargs):
            return Subject(
                getattr(self.__value, attr_name)(*args, **kwargs),
                self.__object_behavior
            )

        return action_wrapper
