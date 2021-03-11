# Question 1 (7p)

A DNA sequence is a list of nucleotides where each nucleotide can be of four variants, denoted
A, G, T, or C. The file `gene_data.dat` contains sets of such DNA sequences.
The data is structured as follows:
- Lines starting with `#` are comments and can be ignored.
- Before a DNA sequence start, the name of the sequence is denoted with a `%` and then the name, for example `% Monkey`.
- The DNA sequence can contain the characters `A`, `G`, `T`, `C` or `*`, where `*` is considered a "wildcard" (could be any of the nucleotides).
- There is an empty line before the next DNA sequence entry occurs.

## Part A, parsing (3p) 
- A.1: Create the function `parse_nucleotides(file: str)` that takes a filename and returns a dictionary with the
 name of the sequence as the keys and a list of the nucleotides as the values. The nucleotide list should contain
  strings of length 1, for example `['A', '*', 'G']`.

If you do not manage to complete Part A, you can use the following Python code to generate
data that you can then use in Part B and Part C.

```python
data = {
  "dog" : ['A', 'A', 'G', 'C', 'T', '*']*10,
  "cat" : ['A', '*', 'T', 'T']*5,
  "fish" : ['A', 'A', 'G', 'G']*3,
}
```

## Part B, analysis (2p)
- B.1: Create a function `count_nucleotides(dna)` that takes a list of nucleotides and counts the max number of each nucleotide in the sequence.
  A wildcard can count as any of the nucleotides, for example, the sequence `A*AG` could have max 3 A and max 2 G nucleotides.
  For example, using the help data given in Part A:
  ```python
  >>> count_nucleotides[data["dog"]]
  (30, 20, 20, 20) # given in the order A, G, T, C
  ```
- B.2: Create a function `count_max_nucleotides` that calculates for each of the DNA sequences in the file, which one has the highest possible
`A`, `B`, `C`, `D` nucleotides *on average* (divide the possible total with the DNA sequence length).
  ```python
  >>> count_max_nucleotides(data)
  {'A': 'dog', 'G': 'fish', 'C': 'dog', 'T': 'cat'}
  ```
  
## Part C, mRNA printing (2p)
DNA can be converted to mRNA via the nucleotide mapping
`T -> A`, `A -> U`, `G -> C` and `C -> G`. Wildcards map to wildcards (`* -> *`).

- C.1: Create a function `export_to_mRNA(file: str, data: dict)` that writes the `data`
read in Part A in the same format as `gene_data.dat` but with the DNA converted to mRNA via the mapping given above.
 For example, the sequence:
 ```
 % Name
 TAAG
 ```

 should be written as

 ```
 % Name
 AUUC
 ```
 The max length for each line of the mRNA sequence should be 40 (just like in `gene_data.dat`).
- C.2: Check that `parse_nucleotides` can read the file written by `export_to_mRNA`.
