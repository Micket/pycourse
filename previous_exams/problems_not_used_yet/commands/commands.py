# Perhaps some way of alerting a "server" to perform various actions?
import hashlib

class BaseCommand:
    def __init__(self, log_message):
        self.message = message

    def __call__(self)
        print(f'Performing action: {self.log_message}')
        self.evaluate()

    @abc.abstractmethod
    def evaluate(self)
        pass


def CustomCommand:
    def __init__(self, message, fun):
        super().__init__(message)

    def __call__(self):
        self.fun()


class RenameFile:
    def __init__(self, ):
        super().__init__(f"renaming {src} to {dest}")
        self.old_name = old_name
        self.new_name = new_name

    def __call__(self):
        os.rename(self.old_name, self.new_name)


class VerifyChecksum:
    def __init__(self, filename, md5sum):
        super().__init__(f"verify checksum of {filename}")

    def __call__(self):
        assert hashlib.md5(filename).hexdigest() == md5sum

