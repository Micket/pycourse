# DAT171 Object oriented programming in Python

* Lecturers:
    * Mikael Öhman, tel. 772 1301, <mikael.ohman@chalmers.se>
      Postdoc at Applied Mechanics
    * Thomas Svedberg, tel. 772 1522, <thomas.svedberg@chalmers.se>
* Assistant:
    * Kristoffer Carlsson, tel. 772 1492, <kristoffer.carlsson@chalmers.se>
      PhD student at Applied Mechanics

Course literature:

* C. Horstmann: Python for everyone
* Python.org tutorial
* Reference manuals



# Prerequisites
Good knowledge of basic programming structures such as variables, conditions, loops, and functions in any programming language.

+-------------------------------+-------------------------------------+
| Matlab                        | Python                      |
+===============================+=============================+
| ```matlab                     | ```python                   |
| function [r] = norm(x)        | def norm(x):                |
| s = 0;                        |     s = 0                   |
| for i = 1:length(x)           |     for i in range(len(x)): |
|    s = s + x(i)^2;            |         s += x[i]**2        |
| end                           |                             |
| r = sqrt(s);                  |     return sqrt(s)          |
| ```                           | ```                         |
+-------------------------------+-----------------------------+



# Course evaluation
* **New course: Continuous feedback is especially appreciated!**
* Course evaluated at 3 occurrences
* Course survey after exam
* Course board representatives (please stand up)



# Content
* Basic building blocks of a Python program (variables, conditional statements, loops, libraries, functions, errors)
* Data structures (trees, dictionaries, tuples)
* Object Oriented programming (classes, objects, inheritance, polymorphism, abstract classes)
* PyQt for creating graphical user interfaces
* NumPy (Matrices, vectors, linear algebra)
* SciPy (Package for numerical computations)
* Matplotlib (Plotting)
* Interactive Python (ipython)



# Learning outcome
After successfully passing the course, the student should be able to independently write object oriented software using Python.

Furthermore, the student should be able to read reference literature for the Python programming language as well as being able to use the SciPy/NumPy package for numerical computations and PySide (Qt) for writing graphical user interfaces.



# Examination
Will take place in computer rooms at 19th of March 2015 in the afternoon. The re-exam will be in august.

* Book is allowed...
* but there will also be reference materials available on the computers
* 4 hours examination
* 5 questions $\times$ 5 points per question
    * 10 points for passing grade
    * 15 points for grade 4
    * 20 points for grade 5

* Will get back to you later when rooms are booked and precisely what documents will be available.
* The exam will not contain anything on the GUI (4 hours would be insufficient)


# Assignments
3 compulsory assignments worth 1hp each which represents 26 hours of work per student.
Assignments may be done alone of in groups of 2.

Please do not cheat! Ask each other questions, but don't share sections of code directly.
_DETECTED CHEATING WILL BE REPORTED_



# Assignment 1: Creating a graph of adjacent points and finding the shortest route
From a file containing coordinates, the goal is to construct a adjacency graph of the coordinates
and find the shortest path between the given start and end point.

* Getting familiar with Python
* Reading files
* Using NumPy for numerics
* Using more advanced data structures (KDTree and sparse graph library from SciPy)
* Matplotlib



# Assignment 2: Playing card library + Game
The first part of the task is to create a library for making card games, then use it to create a simple card game.

* Creating a library
* Creating classes



# Assignment 3: Simple painting application
Create a simple drawing application from scratch.
There will be a few drawing tools required to be implemented (e.g. a rectangle tool and a freehand brush).

* Creating a GUI with PySide
* Creating classes with multiple inheritance



# Software
Software will be available on the windows machines in M and E building.

* Python 3.4
* PySide (Qt)
* NumPy, SciPy, Matplotlib
* Recommended IDE: PyCharm (community edition)
* Laptops:
    * Windows: Anaconda <http://continuum.io/downloads>
    * Linux: Use your package manager or get Anaconda for Linux
    * Mac: Try macports
    * Make sure to get version 3.4!



# Consultation
* Email is preferred before the Pingpong PM system
* 3 computer sessions per week
* Office on third floor in M building (Material & Beräkningsmekanik)



# Schedule
* L = Lectures
* CS = Computer lab session

| Time  | Mo | Tue | Wed | Thu | Fr |
|-------|----|-----|-----|-----|----|
| 8-10  |    |     |     | L   |    |
| 10-12 |    |     |     | CS  |    |
| 13-15 | L  |     |     |     | CS |
| 15-17 | CS |     |     |     |    |



# Lecture overview
| W | Content |
|---|---------|
| 1 | Introduction, lists and loops, functions, libraries |
| 2 | CA1, files and strings, NumPy and SciPy |
| 3 | Matplotlib, common data structures, writing libraries |
| 4 | CA2, Classes and object oriented design |
| 5 | More on classes, exceptions |
| 6 | CA3, GUI: PySide |
| 7 | Leftovers, reserve (if needed)|
| 8 | Repetition and questions, review of example exam |
| 9 | Exam, final deadline on assignment corrections |



# Computer session
* Bring laptops if you need help installing software
* Practice problems (not obligatory)
* First assignment is available if you want to start early



# Questionnaire

## You ...
 1. know another Object Oriented programming langauge already
 2. have tried another OO-programming langauge already
 2. thought the matlab course was easy
 3. can manage matlab decently
 4. didn't even satisfy the course prerequisites

## You will be using ...
 1. a laptop with Windows
 2. a laptop with Linux
 3. a laptop with OSX
 4. the school computers
 5. something else

# About Python

 * Garbage collected (like Matlab, Java)
 * Dynamically typed (like Matlab, unlike Java)
 * Compiles to bytecode (like Java, Matlab in some cases)
 * Object Oriented programming (like Java, unlike Matlab)
 * Has concept of references (like Java, unlike Matlab)
 * Interactive interpreter (like Matlab, unlike Java)
 * Compact syntax (like Matlab, unlike Java)
 * Scripting support in many applications



# Why Python

  * Simple syntax
  * Easy to get started on all platforms
  * Similar concepts as other popular procedural languages (Java, C++, C#)
  * Common scripting language in applications, e.g.

    `[C library] <-> [Python wrapper] <-> [GUI code]`
    `[C++ program] <-> [Evaluate python code from user]`



# Python 3 vs Python 2

  * We'll be sticking to Python 3.4
  * A few incompatible syntax changes
  * A few noteable differences:
      - Printing: `print x`{.python} $\leadsto$ `print(x)`{.python}
      - Proper unicode
      - Dictionaries: `x.has_key(y)`{.py} $\leadsto$ `y in x`{.python}
      - Iterators: `y.iteritems()`{.python} $\leadsto$ `y.items()`{.python}

        (we will get to these later in the course)


# Running Python code

  * Running a single program, once:
    `$ python myscript.py  inputarguments`
    where `inputarguments` are typically filenames or options used in command line interfaces.
    (on windows, this is what happens when you choose "open with" python.exe on a python script)
  * First time running a script will generate a `pyc` file. This is compiled bytecode that is cached (safe to remove).
  * Running only
    `$ python`
    starts an interactive interpreter.
  * More convenient to run scripts through an IDE when developing.



# Using an IDE (PyCharm)

  * An Integrated Development Environment (IDE) is a pimped up text editor that integrates the toolchain.
  * Running a script
      1. Create a small script `foobar.py`
      2. Run $\to$ Edit Configurations: Press + and select your script.
      3. Name the configuration and press OK.
      4. Run $\to$ Run 'Your script'

  * Python console at the bottom for convenience

  * PyCharm can read IPython notebooks (you need to start the notebook server on your computer)

  * Learn the [keyboard shortcuts](http://blog.jetbrains.com/pycharm/files/2010/07/PyCharm_Reference_Card.pdf)!

  * Ctrl + Mouse click for code navigation

  * You are free to use any IDE you want, but PyCharm is the best tool you will have access to during the exam. Learn it!



# Short note on VCS

  * Version control systems (VCS) is a key component when developing and collaborating on larger projects
      * Subversion (a.k.a SVN) - Common centralized VCS
      * GIT - Distributed version control system. <www.github.com> is a popular hosting service.
      * Any decent IDE will integrate support for VCS. 
      * Dropbox is not a VCS.
  * Not critical in this course
      * Your programs will mostly be short, and a learning experience
      * If you are interested, feel free to ask about it more during the computer session



# Variables and printing

  * Python tries to be smart about printing, and doesn't print on assignments

    ```python
>>> x = sqrt(3)
>>> sqrt(3)
1.7320508075688772
>>> 2**3
8
>>> print(x)
1.7320508075688772
    ```
  * Semicolons do nothing

    ```python
>>> x = sqrt(3);
>>> sqrt(3);
1.7320508075688772
    ```



# IPython

  * IPython has convenient macros outside the Python language
    * Similar to the Matlab console
    * Syntax highlighting warnings/errors (inside the console!)
      * Magic functions
```python
%timeit x = sqrt(37)
10000000 loops, best of 3: 52.4 ns per loop
```

  * IPython notebooks; "*The IPython Notebook is a web-based interactive computational environment where you can combine code execution, text, mathematics, plots and rich media into a single document*"

    [SymPy](http://nbviewer.ipython.org/github/ipython/ipython/blob/2.x/examples/Notebook/SymPy.ipynb)

    [Plotly](https://plot.ly/python/3d-plots-tutorial/)



# IPython
  * Use as a calculator
      - Using previous outputs:

        ```python
In [1]: 2**3 + 75*2 - 45/4
Out[1]: 146.75
In [2]: 31536000 / Out[1]
Out[2]: 214896.0817717206
        ```

        Like `'ans'` in Matlab but better

  * Run a script similar to Matlab console
    
    ```python
In [1]: %run myscript.py
In [2]: whos
Variable   Type    Data/Info
----------------------------
x          int     3
    ```

  * Starting a notebook session

        $ ipython cmd notebook

    Connect with web browser or using PyCharm


# Using the built in help

  * The `help()` function
```python
In [1]: help(43)
Help on int object:
...
In [2]: help(math)
Help on module math:
...
    acos(...)
```


  * Tab completion on most things (find what is available)

    ```python
In [1]: x = 'Hello World'
In [2]: x.[TAB]
x.capitalize  x.decode  x.expandtabs  x.index  ...
In [2]: foobar = 'Goodbye World'
In [3]: foo[TAB]
In [3]: foobar
    ```       



# Libraries
  * Importing libraries:

    ```python
In [1]: import math
In [2]: math.sqrt(5)
Out[2]: 2.23606797749979
    -
In [3]: import math as m
In [4]: m.sqrt(5)
Out[4]: 2.23606797749979
    -
In [5]: from math import cos, pi
In [6]: cos(1.5*pi)
Out[6]: -1.8369701987210297e-16
In [7]: sqrt(5)
        ( error message here )
In [8]: from math import *
In [9]: sqrt(5)
Out[9]: 2.23606797749979
    ```



#  Indentation

Indentation is not optional in Python.
It determines control flow scopes in Python!

+----------------------------+------------------------+-------------------------+
| C++                        | Matlab                 | Python                  |
+============================+========================+=========================+
| ```cpp                     | ```matlab              | ```python               |
| if (x) {                   | if x                   | if x:                   |
|     f();                   |     f();               |     f()                 |
| } else if (y) {            | elif y                 | elif y:                 |
|     g();                   |     g();               |     g()                 |
| }                          | end                    |                         |
| for (auto &x: y) {         | for x = y              | for x in y:             |
|     puts("foo\n");         |     disp('foo');       |     print('foo')        |
| }                          | end                    |                         |
| if (q) {                   | if q                   | if q:                   |
| }                          | end                    |     pass                |
| ```                        | ```                    | ```                     |
+--------------------------+------------------------+-------------------------+

# Basic strings and lists
  * Strings as you would expect

    ```python
In [1]: x = 'Hello\nWorld'
In [2]: x
Out[2]: 'Hello\nWorld'
In [3]: print(x)
Out[3]: 
Hello
World
    ```
  * Lists

In [1]: x = [43, 10, 15]
In [2]: len(x)
Out[2]: 3
    


# Indexing

  * Indexing uses the hard brackets
    
    ```python
In [1]: x = [43, 10, 15]
In [2]: x[1]
Out[2]: 10
    ```
  * Note that indexing starts from 0! (Index measures distance from start)

    ```python
In [1]: x = [43, 10, 15]
In [2]: x[1]
Out[2]: 10
    ```



# Common operators

  * Binary operators

    ```python
    +  -  *  //  /  %  **  <  <=  ==  !=  >=  >
    ```

    For scalars 
      * `a**b` $= a^b$
      * `a//b` $= \lfloor a/b \rfloor$
      * `a%b ` $= a \,\text{mod}\, b$

  * Extended assignments

    ```python
    +=  -=  *=  /=  //=  %=  **=
    ```

    These give the same result

      * `reallyLongName += 1`
      * `reallyLongName = reallyLongName + 1`

    but slightly different behind the scenes


# Bitwise operators

  * Binary representations of numbers:

    ```
    41 = 2^5 + 2^3 + 2^0 = 101001b
    ```

  * Binary operators

    ```python
    <<  >>  &  *  |
    ```

    ```
    41 >> 2 = 101001b >> 2 = 001010b = 10
    a >> b = a // (2**b)
    ```
  * Extended assignments
    
    ```python
    <<=  >>=  &=  ^=  |= 
    ```
  * You probably won't end up using these in the scope of this course.


# Operators acting on objects

  * Operators are not the same as in Matlab
  * Different objects work differently with operators
  * Strings
    
    ```python
In [1]: 'Hello World' * 3
Out[1]: 'Hello WorldHello WorldHello World'
In [2]: 'Hello World' + '!'
Out[2]: 'Hello World!'
    ```

  * Lists (same behavior as strings)

    ```python
In [1]: [1, 2, 3] * 3
Out[1]: [1, 2, 3, 1, 2, 3, 1, 2, 3]
In [2]: [1, 2, 3] + [4, 5]
Out[2]: [1, 2, 3, 4, 5]
    ```

  * NumPy arrays will overload operators and do different things!
    Test in the interpreter whenever you are unsure.
     

