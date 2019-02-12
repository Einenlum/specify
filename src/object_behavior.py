from .subject import Subject

class ObjectBehavior:
    def _describe(self, cls):
        obj = cls.__new__(cls)
        self.__obj = Subject(obj, self)

    def _be_constructed_with(self, *args, **kwargs):
        self.__obj._get_value().__init__(*args, **kwargs)

    def _get_wrapped_object(self):
        return self.__obj

    def __getattr__(self, attr_name):
        matcher_prefix = '_should_'

        if attr_name.startswith(matcher_prefix):
            matchers_keys = self.matchers.keys()
            key = attr_name[len(prefix):]
            if key in matchers_keys:
                custom_matcher = self.matchers()[key]
                def custom_matcher_wrapper(*args):
                    return self.__obj.match_with_custom_matcher(
                        key,
                        custom_matcher,
                        *args
                    )
                return custom_matcher_wrapper

        def subject_wrapper(*args, **kwargs):
            return getattr(self.__obj, attr_name)(*args, **kwargs)

        return subject_wrapper

    def _matchers(self):
        return {}

    def _let(self):
        pass

    def _let_go(self):
        pass
