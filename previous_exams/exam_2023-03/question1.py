# Question 1 2023-03-14
from random import randint
import numpy as np


def parse_line(line: str) -> tuple:
    items = []

    for item in line.strip().split("  "):
        item = item.strip()
        if item != "":              # Do not add empty strings
            if item == "---":       # Handle non existing forms
                items.append(None)
            else:
                items.append(item)

    return tuple(items)


def read_file(filename: str) -> list[tuple]:
    verbs = []

    with open(filename) as file:
        for line in file:
            verb = parse_line(line)
            if verb:                    # Handle empty lines
                verbs.append(verb)
    
    return verbs


def select_verbs(count: int, verbs: list[tuple]) -> list[tuple]:
    max = len(verbs)

    indices = set()

    while len(indices) < count:
        indices.add(randint(0 , max - 1))

    my_verbs = []
    for index in indices:
        my_verbs.append(verbs[index])

    return my_verbs


def select_form(verb: tuple) -> int:
    index = randint(0, 4)

    while verb[index] == None:
        index = randint(0, 4)

    return index


def print_practice_sheet(verbs: str) -> None:
    # First select verb forms
    indices = []
    for verb in verbs:
        indices.append(select_form(verb))

    # Now find max column width, min width = 8 characters
    widths = [8] * 5
    for verb, index in zip(verbs, indices):
        if len(verb[index]) > widths[index]:
           widths[index] = len(verb[index])

    print("=" * (np.sum(widths) + 6 + 5*2)) # Total width of words, plus separators "|", plus one empty space around each word
    for verb, index in zip(verbs, indices):
        print("|", end="")
        for pos in range(0, 5):
            if pos == index:
                print(f" {verb[pos]:{widths[pos]}s} ", end="")
            else:
                print(f" {'':{widths[pos]}s} ", end="")
            if pos < 4:
                print("|", end="")
            else:
                print("|")
    print("=" * (np.sum(widths) + 6 + 5*2)) # Total width of words, plus separators "|", plus one empty space around each word


def print_sheet(verbs: str) -> None:
    # Now find max column width, min width = 8 characters
    widths = [8] * 5
    for verb in verbs:
        for pos in range(0,5):
            if verb[pos] != None and len(verb[pos]) > widths[pos]:
                widths[pos] = len(verb[pos])

    print("=" * (np.sum(widths) + 6 + 5*2)) # Total width of words, plus separators "|", plus one empty space around each word
    for verb in verbs:
        print("|", end="")
        for pos in range(0, 5):
            if verb[pos] != None:
                print(f" {verb[pos]:{widths[pos]}s} ", end="")
            else:
                print(f" {'':{widths[pos]}s} ", end="")
            if pos < 4:
                print("|", end="")
            else:
                print("|")
    print("=" * (np.sum(widths) + 6 + 5*2)) # Total width of words, plus separators "|", plus one empty space around each word


filename = "verblista.txt"

verbs = read_file(filename)

my_verbs = select_verbs(10, verbs)
print_practice_sheet(my_verbs)
print_sheet(my_verbs)
