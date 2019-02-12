def prophesize(cls):
    class AttributeProphecy:
        def __init__(self, mock, name, args, kwargs):
            self.mock = mock
            self.name = name
            self.args = args
            self.kwargs = kwargs
            self.called_times = 0

        def _will_return(self, value):
            self.return_value = value
            self.mock.add_prophecy(self)

            return self

        def _should_be_called(self):
            self.mock.should_call_prophecy(self)
            self.mock.add_prophecy(self)

        def __str__(self) -> str:
            args = [str(arg) for arg in self.args]
            kwargs = [str(kwarg) for kwarg in self.kwargs]

            return f"{self.name}, args: {args}, kwargs: {kwargs}"

    class MockedObject(cls):
        def __getattribute__(self, attr_name):
            if not callable(cls.__getattribute__(self, attr_name)):
                return cls.__getattribute__(self, attr_name)

            def wrapper(*args, **kwargs):
                for prophecy in self._prophecies:
                    if attr_name == prophecy.name and args == prophecy.args and kwargs == prophecy.kwargs:
                        prophecy.called_times += 1

                        return prophecy.return_value
                raise Exception('No return value was specified for this call')
            return wrapper
        pass

    class Mock():
        def __init__(self):
            self.__mock_object = MockedObject.__new__(MockedObject)
            self.__mock_object._prophecies = []
            self.__mock_object._prophecies_to_call = []
        pass

        def add_prophecy(self, attribute_prophecy: AttributeProphecy):
            self.__mock_object._prophecies.append(attribute_prophecy)

        def _get_existing_prophecy(self, name, args, kwargs):
            for prophecy in self.__mock_object._prophecies:
                if name == prophecy.name and args == prophecy.args and kwargs == prophecy.kwargs:
                    return prophecy

            return None

        def should_call_prophecy(self, attribute_prophecy: AttributeProphecy):
            self.__mock_object._prophecies_to_call.append(attribute_prophecy)

        def check_prophecies(self):
            for prophecy in self.__mock_object._prophecies_to_call:
                if prophecy.called_times == 0:
                    raise Exception(f"Method {str(prophecy)} should have been called but was not.")

        def _reveal(self):
            return self.__mock_object

        def __getattr__(self, attr_name):
            def wrapper(*args, **kwargs):
                existing_prophecy = self._get_existing_prophecy(
                    attr_name,
                    args,
                    kwargs
                )

                if None == existing_prophecy:
                    return AttributeProphecy(self, attr_name, args, kwargs)

                return existing_prophecy

            return wrapper

    return Mock()
