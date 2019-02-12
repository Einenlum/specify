class MatcherError(AssertionError):
    pass

class CustomMatcherError(AssertionError):
    pass

class MatcherNotFoundError(NotImplementedError):
    pass

class UndefinedMockBehaviorError(Exception):
    pass
