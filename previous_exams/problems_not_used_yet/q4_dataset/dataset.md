# Dataset hierarchy (xp)

In machine learning we often need to train models where the data is stored in many different ways, for example in memory, files on disk, or a database.
Here we will write a class hierarchy that unifies access to those different methods.

## Part A: (1.5p)

Write an abstract base class `Dataset` which stores a `name` as an instance variable and implements the method `rand` for fetching a random element from the dataset.
It should enforce the abstract methods for computing the `len(dataset)` and getting an item using with `dataset[i]`

*Hint: `random.randrange` is useful here.*

## Part B: (1p)

Implement the subclass `ListDataset` which takes a `name` and list of `data` as input.
Add a nice `repr` method.

## Part C: (1.5p)

Implement the subclass `DirectoryDataset` which only takes a path to a directory as input.
It's name should be the last directory in the given path: `examples/limerick` should produce the name `limerick`.
Add a nice `repr` method.

The examples are small, but the idea here is to read the `i`-th file accessing `dataset[i]` as it's to large to fit in all of it in memory.

*Hint: `os.listdir` is useful here.*

## Part C: (1.5p)

We often need to split a dataset into parts for training and validation. 
Implement the subclass `SubsetDataset` which takes another `dataset` and a `subrange` (like `range(1, 3)`)
It should not make any copies of the input data.
The name of the subset should be the same as the dataset it captures.
Add a nice `repr` method.

## Part D: (1p)

For testing behaviour its often useful to have random data.
Implement the subclass `RandomDataset` which takes takes a `name` as input.
It should just report `1` as the length of the dataset and getting an item with `dataset[0]` should generate a random lowercase string with 10 characters.

*Hint: random.choice is useful here*


