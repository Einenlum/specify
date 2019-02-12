def prophesize(cls):
    class AttributeProphecy:
        def __init__(self, mock, name, args, kwargs):
            self.mock = mock
            self.name = name
            self.args = args
            self.kwargs = kwargs

        def _will_return(self, value):
            self.return_value = value
            self.mock.add_prophecy(self)

            return self

    class MockedObject(cls):
        def __getattribute__(self, attr_name):
            if not callable(cls.__getattribute__(self, attr_name)):
                return cls.__getattribute__(self, attr_name)

            def wrapper(*args, **kwargs):
                for prophecy in self._prophecies:
                    print(prophecy)
                    if attr_name == prophecy.name and args == prophecy.args and kwargs == prophecy.kwargs:
                        return prophecy.return_value
                raise Exception('No return value was specified for this call')
            return wrapper
        pass

    class Mock():
        def __init__(self):
            self.__mock_object = MockedObject.__new__(MockedObject)
            self.__mock_object._prophecies = []
        pass

        def add_prophecy(self, attribute_prophecy):
            self.__mock_object._prophecies.append(attribute_prophecy)

        def _reveal(self):
            return self.__mock_object

        def __getattr__(self, attr_name):
            def wrapper(*args, **kwargs):
                return AttributeProphecy(self, attr_name, args, kwargs)

            return wrapper

    return Mock()
