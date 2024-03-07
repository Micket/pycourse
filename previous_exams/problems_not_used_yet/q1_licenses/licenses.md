---
header-includes:
        - \usepackage[a4paper,left=1.9cm, right=1.9cm, top=1.5cm, bottom=1.9cm]{geometry}
---

# Question 1: License log (6.5p)

We have a license server that logs each license checkout with the username and version.
In order to save on license costs, we will investigate which versions we need to keep paying for based on the log.

The server logs the lines in the following format: `"YEAR-MONTH-DAY user=USERNAME version=VERSIONSTRING"`
where `VERSIONSTRING` has the format `MAJOR.MINOR.PATCH`.

## Part A: Parse log line (1p)

Write a function `parse_line(line: str)` which parses a single log line and returns a date, username, and the version (as a 3-valued tuple)

**Example**:
```python
x = parse_line('2023-01-12 user=ohmanm version=1.0.1')
print(x)
```

**Output**:
```python
(datetime.date(2023, 1, 12), 'ohmanm', (1, 0, 1))
```


## Part B: Parse the entire log file (3p)

Write the function `collect_license_data(filename: str)` which parses the entire log file and constructs two dictionaries:

- a mapping from versions to their most recent use
- a mapping from usernames to a dictionary of versions and how many times (that user) has requested it.

```python
users_use, last_use = collect_license_data('example.txt')
print("Philip used v1.2.4", users_use['philip'][(1, 2, 4)], "times")
print("Conrad used v1.2.4", users_use['conrad'][(1, 2, 4)], "times")
print("0.1.4 was last used", last_use[(0, 1, 4)])
```

**Output**

```
Philip used v1.2.4 6 times
Conrad used v1.2.4 9 times
0.1.4 was last used 2021-12-30
```

*Hint* `collections` has the useful `Counter` and `defaultdict` classes.

## Part C: Check usage (1.5p)

Write the function `check_usage(version, last_use, user_use)` which looks up the given `version` and prints:

- that the version has not ever been used (if it hasn't)
- when the version was last used and a formatted list of users and the times they have used it. You may assume names are no longer than 10 characters and no one used the software more than 99 times. 

**Example**
```python
check_usage((1, 2, 3), last_use, users_use)
check_usage((1, 2, 4), last_use, users_use)
```
**Output**
```
v1.2.3 has not been used
v1.2.4 was used as recently as 2022-12-29
turanga   : 11 times
john      :  8 times
conrad    :  9 times
hubert    : 10 times
philip    :  6 times
rodriquez :  9 times
wong      :  6 times
```

## Part D: Check major version (1p)

Write the function `check_major_version(major_version, last_use)` which prints a table with the latest usage for all versions matching the given `major_version`.
It must be sorted based on the full version number.

**Example**
```python3
check_major(1, last_use)
```
**Output**
```
v1.1.0: 2022-12-18
v1.1.4: 2022-12-17
v1.2.0: 2022-12-17
v1.2.4: 2022-12-29
v1.3.0: 2022-12-29
v1.3.4: 2022-12-14
```
