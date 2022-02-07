Try make the code "nice" before submitting:

- No chunks of commented out code, no big gaps with empty lines etc.
- Give a cursory glance over spelling (PyCharm helps with this).
- Keep everything in English, it's good practice and how things are done "for real".
- Make the formatting consistent with PEP 8 (https://www.python.org/dev/peps/pep-0008/). PyCharm helps with that.
- No extra random files in the submission.
- Give your variables good descriptive names
- Read through the assignment and see that everything that should be implemented is implemented.

Might seem nitpicky but it is actually important.

Some other peculiarities:

- Redundant `pass` / `continue`:

    ```python
    if r > radius
       ...
    else:
        pass
    ```
    
    ```python
    for x in coord_list
        if ...:
            ...
        else
            continue
    ```
    
- Using `enumerate` without destructuring:

    ```python
    for i in enumerate(coord_list)
        for j in enumerate(coord_list)
            if j[0] > i[0]:
                r = i[1][0] - j[1][0]...
    ```

    Should be:
    
    ```python
    for i, coord_i in enumerate(coord_list)
        for j, coord_j in enumerate(coord_list)
            if j > i
                r = coord_i[0] - coord_j[0] ...
    ```

