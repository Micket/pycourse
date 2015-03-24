# Style guide for code and comments for DAD171

This document contain the style guide that we want you to adhere to when
writing the code and the comments for the computer assignments. The points
in this document are a condensed version of the official Python style guide
which can be found here: https://www.python.org/dev/peps/pep-0008/. PySide
which is the IDE we recommend you to use will usually warn you with a yellow
line if you break the guide (but not always).


## Code style guide

- [ ] Indentation should be made using four spaces.

- [ ] Variables should be written with lowercase letters with underscores
separating words, i.e. `variable_name`

- [ ] Class names should be written in CamelCase where each new word
starts with a capital letter, i.e. `ClassName`

- [ ] Constants defined in a module should be written at the top of the file and be
in all capital letters with underscores separating words, i.e. `CONSTANT_NAME`

- [ ] Variables and classes should have descriptive English names.

- [ ] Each line should have a maximum of 80 characters.

- [ ] Imports should only be made at the top of the file.

- [ ] Modules should have short all-lowercase names.

- [ ] Do not use what is known as *Yoda conditions*. This is when the constant in a
conditional statement is placed to the left side, i.e:
 ```python
 if (10 < self.value)
 ```

- [ ] A function definition should have one empty line above it
and a class definition should have two.

## Comments style guide

- [ ] Comments should be written in English.

- [ ] Do not overcomment. A comment that is simply restating what a piece
of code is doing in a human language is only distracting. An example of overcommenting is
 ```python
 x = x + 1  # Add 1 to x
 ```
 If most of your lines of code has a an associated comment you are
 either over commenting or writing too complicated code.

