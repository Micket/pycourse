class AuthenticationError(Exception):
    # Not sure what methods one would really want to add to exceptions..
    @abc.abstractmethod
    def user_suggestion(self) -> str:
        pass

class BannedError(AuthenticationError):
    pass


class ServerProblem(Enum):
    Timeout = 0
    Maintenance = 1
    Unknown = 2

class ServerError(AuthenticationError):
    def __init__(self, reason):
        self.reason = reason

class UnknownUserError(AuthenticationError):
    pass

class BadUserOrPasswordError(AuthenticationError):
    pass
