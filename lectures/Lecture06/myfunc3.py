from typing import Union


def myfunc3(p1: Union[float, int], p2: Union[float, int]) -> Union[float, int]:
    """
    My very special function to add 2 numbers.
    
    Parameters:
    -----------
    :param p1: First number to add
    :param p2: Second number to add
    
    Returns:
    --------
    :return: The sum of the given numbers
    """
    
    return p1 + p2


a = myfunc3("12", 3)
b = "banana"
c = a + b
