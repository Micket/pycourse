import abc, enum
from datetime import datetime

# Part A
class Writer(metaclass=abc.ABCMeta):
    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def write_line(self, text):
        pass
    
    @abc.abstractmethod
    def flush(self):
        pass


class DirectFileWriter(Writer):
    def __init__(self, filename):
        super().__init__(filename)
        self.file = open(filename, 'w')

    def write_line(self, text):
        self.file.write(text + '\n')

    def flush(self):
        self.file.flush()


class CircularWriter(Writer):
    def __init__(self, n, filename):
        super().__init__(filename)
        self.n = n
        self.buffer = [None]*n
        self.pos = 0

    def write_line(self, text):
        if self.pos == self.n:
            self.pos = 0
        self.buffer[self.pos] = text
        self.pos += 1

    def flush(self):
        with open(self.filename, 'w') as fout:
            for i in range(self.pos, self.n):
                if self.buffer[i]:
                    fout.write(self.buffer[i] + '\n')
            for i in range(self.pos):
                fout.write(self.buffer[i] + '\n')


# Part B
class LogLevel(enum.IntEnum):
    DEBUG = 0
    WARNING = 1
    ERROR = 2


class Logger:
    def __init__(self, name, level, date_format, writer):
        self.name = name
        self.level = level
        self.date_format = date_format
        self.writer = writer

    def log(self, level, msg):
        if level >= self.level:
            now = datetime.now()
            output = '[{}] {}::{} - {}'.format(now.strftime(self.date_format), self.name, level.name, msg)
            self.writer.write_line(output)

