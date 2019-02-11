from .subject import Subject

class ObjectBehavior:
    def _describe(self, cls):
        obj = cls.__new__(cls)
        self.__obj = Subject(obj)

    def _be_constructed_with(self, *args, **kwargs):
        self.__obj._get_value.__init__(*args, **kwargs)

    def _get_wrapped_object(self):
        return self.__obj

    def __getattr__(self, attr_name):
        print(f'Try to access {attr_name}')
        def wrapper(*args, **kwargs):
            return getattr(self.__obj, attr_name)(*args, **kwargs)

        return wrapper

    def _let(self):
        pass

    def _let_go(self):
        pass
