from question4 import *

# Either writer should work for your logger:
use_circular = True

if use_circular:
    # We test it with a very small circular array:
    writer = CircularWriter(5, 'logfile.txt')
else:
    writer = DirectFileWriter('logfile.txt')

# We choose to store microseconds in this example since the test example is so brief:
logger = Logger('MyProgram', LogLevel.WARNING, '%Y-%m-%dT%H:%M:%S.%f', writer)

logger.log(LogLevel.DEBUG, 'This debug message should be ignored!')
for i in range(10):
    logger.log(LogLevel.WARNING, 'Testing {}'.format(i))

logger.log(LogLevel.ERROR, 'This error should be printed last in the file.')
logger.log(LogLevel.DEBUG, 'And this shouldn\'t be in the file at all.')

# Force flush the buffer before exiting to ensure everything is written to file:
writer.flush()

