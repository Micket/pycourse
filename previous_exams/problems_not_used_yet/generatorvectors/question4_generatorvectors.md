# Question 4 (8p)

You must solve this problem without using `numpy` or `scipy`.

Sometimes we need to create very large arrays in memory constrained environments.
One common trick that is sometimes applicable is to lazily evaluate the contents of the array, as it is accessed.
The point of these as that they don't allocate memory up front. 

## Part A (2p)

Write an abstract base class `GeneratorVector` that stores the length of the array and support the builtin `len(v)` function.

1. It should enforce the `__getitem__` method as abstract.
2. It should implement a method `collect()` which returns all the vector values as a standard python `list`.

## Part B (2p)

Implement a subclass `ConstantVector` which represents a vector with same value for each index.
The constructor should take a constant and the length as input.

Implement methods to support:

1. the builtin function `repr`.
2. multication with a scalar, e.g. `const_vec * 2` which should return a new `ConstantVector`.
3. addition with a scalar, e.g. `const_vec + 3.14` which should return a new `ConstantVector`.

## Part C (2p)

Implement a subclass `LinspaceVector` which represents a vector with linear increments from a start to an end value in a given number of steps.
The constructor should take `start`, `end`, and `steps` as input.

Implement methods to support:

1. the builtin function `repr`.
2. multication with a scalar, e.g. `linsp_vec * 2` which should return a new `LinspaceVector`.
3. addition with a scalar, e.g. `linsp_vec + 3.14` which should return a new `LinspaceVector`.

## Part D (2p)

Implement a subclass `FunctionVector` which represents a vector with values defined by a function evaluated at the index: $v_i = f(i)$.
The constructor should take function handle and a vector length as input.

Implement methods to support:

1. the builtin function `repr`.
2. multication with a scalar, e.g. `fun_vec * 2` which should return a new `FunctionVector`.
3. addition with a scalar, e.g. `fun_vec + 3.14` which should return a new `FunctionVector`.

*Hint: You can use lambdas to construct new functions when multiplying and adding.*

## Test



