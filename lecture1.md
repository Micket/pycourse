# DAT171 Object oriented programming in Python

* Lecturers:
    * Mikael Öhman, tel. 772 1301, mikael.ohman@chalmers.se 
    * Thomas Svedberg, tel. 772 1522, thomas.svedberg@chalmers.se 
* Assistant:
    * Kristoffer Carlsson, tel. 772 1492, kristoffer.carlsson@chalmers.se

Course literature:

* C. Horstmann: Python for everyone
* Python.org tutorial
* Reference manuals



# Prerequisites
Good knowledge of basic programming structures such as variables, conditions, loops, and functions in any programming language.

```matlab
function [r] = norm(x)
s = 0;
for i = 1:length(x)
    s = s + x(i) * x(i);
r = sqrt(s);
```


# Course evaluation

* **New course: Continuous feedback is especially appreciated!**
* Course evaluated at 3 occurrences
* Course survey after exam.
* Course board representatives (please stand up)


# Content

* Basic building blocks of a Python program (variables, conditional statements, loops, libraries, functions, errors).
* Data structures (trees, dictionaries, tuples)
* Object Oriented programming (classes, objects, inheritance, polymorphism, abstract classes).
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
* but there will also be reference materials will be available on the computers
* 4 hours examination
* 5 questions $\times$ 5 points per question
    * 10 points for passing grade
    * 15 points for grade 4
    * 20 points for grade 5



# Assignments
3 compulsory assignments worth 1hp each which represents 26 hours of work per student.
Assignments may be done alone of in groups of 2.

### Cheating
Please do not cheat! Ask each other questions, but don't share sections of code directly.
_DETECTED CHEATING WILL BE REPORTED_

# Assignment 1: Creating a graph of adjacent points and finding the shortest route
From a file containing coordinates, the goal is to construct a adjacency graph of the coordinates and find the shortest path between the given start and end point.

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
Create a simple drawing application from scratch. There will be a few drawing tools required to be implemented (e.g. a rectangle tool and a freehand brush).

* Creating a GUI with PySide
* Creating classes with multiple inheritance



# Software
Software will be available on the windows machines in M and E building.

* Python 3.4
* PySide (Qt)
* NumPy, SciPy, Matplotlib
* Recommended IDE: PyCharm (community edition)
* Laptops:
    * Windows: Anaconda [http://continuum.io/downloads](http://continuum.io/downloads)
    * Linux: Use your package manager
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


# Lectures
