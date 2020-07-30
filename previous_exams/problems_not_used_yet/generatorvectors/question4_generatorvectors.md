# Question 4

You must solve this problem without using `numpy` or `scipy`.

Sometimes we need to create very large arrays in memory constrained environments.
One common trick that is sometimes applicable is to lazily evaluate the contents of the array, as it is accessed.
The point of these as that they don't allocate memory up front. 

## Part A

Write a base class `GeneratorVector` that stores the length of the array and provide the `len(v)` operation.

1. It should enforce the `__getitem__` method as abstract.
2. It should implement the method `collect()` which collects all of the vector and return a normal `list`.

## Part B

Implement a subclass `ConstantVector` which represents a vector with constant values.
The constructor should take a constant and the length as input.

1. Add support for `repr()`
2. Add support for multication with a scalar, e.g. `const_vec * 2` which should return a new `ConstantVector`.
3. Add support for addition with a scalar, e.g. `const_vec + 3.14` which should return a new `ConstantVector`.

## Part C

Implement a subclass `LinspaceVector` which represents a vector with linear increments from a start to an end value in a given number of steps.
The constructor should take `start`, `end`, and `steps` as input.

1. Add support for `repr()`
2. Add support for multication with a scalar, e.g. `linsp_vec * 2` which should return a new `LinspaceVector`.
3. Add support for addition with a scalar, e.g. `linsp_vec + 3.14` which should return a new `LinspaceVector`.

## Part D

Implement a subclass `FunctionVector` which represents a vector with values defined by a function evaluated at the index: $v_i = f(i)$.
The constructor should take function handle and a vector length as input.

1. Add support for `repr()`
2. Add support for multication with a scalar, e.g. `linsp_vec * 2` which should return a new `FunctionVector`.
3. Add support for addition with a scalar, e.g. `linsp_vec + 3.14` which should return a new `FunctionVector`.

*Hint: You can use lambdas to construct new functions when multiplying and adding.*

## Test



