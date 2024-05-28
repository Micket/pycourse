import abc
import datetime
from enum import IntEnum
from typing import Sequence
import collections


class LogLevel(IntEnum):
    debug = 0
    info = 1
    warning = 2
    error = 3


class LogSink(metaclass=abc.ABCMeta):
    def __init__(self, minimum_loglevel: LogLevel):
        self.minimum_loglevel = minimum_loglevel

    def push(self, importance: LogLevel, msg: str):
        if self.minimum_loglevel <= importance:
            self._write(self.datestamp() + ' - ' + msg)

    @abc.abstractmethod
    def _write(self, entry: str):
        pass

    @staticmethod
    def datestamp() -> str:
        return '[' + datetime.datetime.now().isoformat() + ']'


class PrintSink(LogSink):
    def _write(self, entry: str):
        print(entry)


class FileSink(LogSink):
    def __init__(self, minimum_loglevel: LogLevel, filename: str):
        super().__init__(minimum_loglevel)
        # As specified in the question, for this question it's OK to leave this file handle open
        self.output = open(filename, 'w')

    def _write(self, entry: str):
        self.output.write(entry + '\n')


class MemorySink(LogSink):
    def __init__(self, minimum_loglevel: LogLevel, maxlen: int):
        super().__init__(minimum_loglevel)
        self.entries = collections.deque(maxlen=maxlen)

    def __iter__(self):
        return iter(self.entries)

    def _write(self, entry: str):
        self.entries.append(entry)


class MultiSink(LogSink):
    def __init__(self, sinks: Sequence[LogSink]):
        self.sinks = sinks

    def push(self, importance: LogLevel, msg: str):
        ds = self.datestamp()
        for sink in self.sinks:
            if sink.minimum_loglevel <= importance:
                sink._write(ds + ' - ' + msg)

    def _write(self, entry: str):
        pass


# Test
ps = PrintSink(LogLevel.info)
fs = FileSink(LogLevel.warning, 'logfile.txt')
multi = MultiSink([ps, fs])

multi.push(LogLevel.info, 'Multi-test: Stuff happened.')
multi.push(LogLevel.error, 'Multi-test: An error occurred!')

ms = MemorySink(LogLevel.warning, 5)
for test_message in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    ms.push(LogLevel.warning, test_message)

for event in ms:  # Should display C trough G
    print('MemorySink:', event)
