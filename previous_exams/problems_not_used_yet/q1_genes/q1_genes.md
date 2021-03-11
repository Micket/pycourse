# Question 1 (8p)

A DNA sequence is a list of nucleotides where each nucleotide can be of four variants, denoted
A, G, T, or C. The file `gene_data.dat` contains sets of such DNA sequences.
The data is structured as follows:
- Lines starting with `#` are comments and can be ignored.
- Before a DNA sequence start, the name of the sequence is denoted with a `%` and then the name, for example `% Monkey`.
- The DNA sequence can contain the characters `A`, `G`, `T`, `C` or `*`, where `*` is considered a "wildcard" (could be any of the nucleotides).
- There is an empty line before the next DNA sequence entry occurs.

## Part A, parsing (3p) 
- A.1: Create the function `parse_nucleotides(file: str) -> dict[str, List[chr]]` that takes a filename and returns a dictionary with the
 name of the sequence as the keys and a list of the nucleotides (using characters, `chr`) as the values.

If you do not manage to complete Part A, use the following for the rest of the questions:

```python
data = {
  "animal1" : ['A', 'A', 'G', 'C', 'T' '*']*10,
  "animal2" : ['A', '*', '*', 'T', 'T']*5,
}
```

## Part B, analysis (2p)
- B.1: Create a function `count_nucleotides(dna: list[chr])` that takes a list of nucleotides and counts the max number of each nucleotide in the sequence.
  A wildcard can count as any of the nucleotides, for example, the sequence `A*AG` could have max 3 A and max 2 G nucleotides.
- B.2: Create a function that calculates for each of the DNA sequences in the file, which one has the highest possible
`A`, `B`, `C`, `D` nucleotides *on average* (divide the possible total with the DNA sequence length).

## Part C, mRNA printing (3p)
DNA can be converted to mRNA via the nucleotide mapping
`T -> A`, `A -> U`, `G -> C` and `C -> G`. 

- C.1: Create a function `export_to_mRNA(file: str, data: dict[str, List[chr])` that writes the `data`
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
