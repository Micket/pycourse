# Question 1: Listing files and sizes

# Part A (1.5p)
Write a function `read_directory` that takes a directory path as input and returns a dictionary with all files and their corresponding file size in bytes.

*Hint: Look for useful functions in `os` and `os.path`.*

**Example:**
```python3
path = 'example'  # Could also be '../path/to/directory'
dinfo = read_directory(path)
print(dinfo)
```
**Output:**
```text
todo example
```

# Part B (2p)
Sizes of computer files are typically listed in terms of "Kibi"-, "Mibi"- and "Gibi"-bytes. Shortened as "KiB", "MiB", "GiB" respectively.
- 1 KiB = 1024 B
- 1 MiB = 1024 KiB = $1024^2$ B
- 1 GiB = 1024 MiB = $1024^3$ B
I.e. simply using 1024 instead of 1000 (like with Kilo, Mega, Giga)

Write a helper function `format_bytes` that takes a number of bytes Kibi, Mibi, Gibi prefixes when the values are larger than 1024, $1024^2$, $1024^3$ respectively.
It must avoid showing decimals when the number is an integer (see examples), and show maximum of 2 decimals.

**Example:**
```python3
print(format_bytes(42))
print(format_bytes(1024))
print(format_bytes(10240))
print(format_bytes(200000))
print(format_bytes(1234567890))
```

**Output:**
```text
42B
1KiB
12KiB
195.31KiB
1.15GiB
```

# Part C (2.5p)

Write a function `show_directory_info` that takes the path and directory info from part A and displays all the sizes like in the example below.
- The total size should be printed next to the path on the first line.
- For readability, the directory content should be displayed with a indentation using `├── ` and  `└── ` on the last line.
- Sort the files according to size (largest to smallest).

**Example:**
```python3
show_directory_info(path, dinfo)
```
**Example:**
```text
todo example
```

