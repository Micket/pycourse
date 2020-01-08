"""
My own library for printing stuff!

More documentation here...
"""

WIDTH = 10


def funcA(data1, data2):
    """
    funcA: print two objects.

    :param data1: Any object that can be printed
    :param data2: Any object that can be printed
    """
    
    print(f'My data is: "{data1}", "{data2}"')


def funcB():
    """funcB: indicate that task is done."""
    print('Task done: "{}"'.format(__name__))


if __name__ == '__main__':
    funcA("Testing", "funcA")
    funcB()
