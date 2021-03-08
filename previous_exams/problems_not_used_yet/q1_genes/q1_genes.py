from typing import Dict, List
import enum
import random
import textwrap
import inspect

def generate_dat_file():
    random.seed(1337)
    names = ["Cat", "Mouse", "Aligator", "Pikachu"]
    sequence_lengths = [700, 500, 220, 1000]
    comments = [
        """
        # Entry 1
        # Created by : Emil and Emilia
        # Date: 2020-02-10
        """,

        """
        # Field excursion
        # Created by: Ada and Beda
        # Date: 1989-06-22
        """,

        """
        # Author: Ötzi
        # Date: 3400 BC
        """,

        """
        # Pallet Town
        # Author: Ash Ketchum
        # Date: 1996-01-01
        """
    ]
    line_length = 40
    wildcard_probability = 0.10
    bases = ['A', 'G', 'T', 'C']
    with open("gene_data.dat", "w") as f:
        for name, sequence_length, comment in zip(names, sequence_lengths, comments):
            f.write(inspect.cleandoc(comment))
            f.write(f"\n% {name}\n")
            for n in range(sequence_length):
                if random.random() < wildcard_probability:
                    f.write('*')
                else:
                    f.write(random.choice(bases))
                if (n+1) % line_length == 0:
                    f.write('\n')
                    n = 0
            f.write("\n\n")


# Start of solution

class Nucleotide(enum.Enum):
    A = 0
    G = 1
    C = 2
    T = 3
    U = 4
    WIlDCARD = 5


def parse_data(file: str) -> Dict[str, List[Nucleotide]]:
    def to_enum(x):
        if x == 'A':
            return Nucleotide.A
        elif x == 'G':
            return Nucleotide.G
        elif x == 'C':
            return Nucleotide.C
        elif x == 'T':
            return Nucleotide.T
        elif x == 'U':
            return Nucleotide.U
        elif x == '*':
            return Nucleotide.WIlDCARD
        else:
            raise Exception(f"unknown nucleotide {x}")

    data = {}
    with open(file, "r") as f:
        while True:
            l = f.readline().strip()
            if l == "":
                break # Reached end of file

            # Read the comments
            while True:
                if not l.startswith('#'):
                    break
                l = f.readline().strip()

            # Read the name
            name = l.split("% ")[1]

            # Readh the nucleotide data
            nucleotides = []
            while True:
                l = f.readline().strip()
                if l == "":
                    break
                nucleotides.extend(map(to_enum, l))
            data[name] = nucleotides
    return data


def count_nucleotides(dna: List[Nucleotide]):
    n_wildcards = dna.count(Nucleotide.WIlDCARD)
    n_A = dna.count(Nucleotide.A) + n_wildcards
    n_G = dna.count(Nucleotide.G) + n_wildcards
    n_C = dna.count(Nucleotide.C) + n_wildcards
    n_T = dna.count(Nucleotide.A) + n_wildcards
    return n_A, n_G, n_C, n_T


def count_max(data):
    results = {"A": {}, "G": {}, "C": {}, "T": {}}
    for name, dna in data.items():
        n_A, n_G, n_C, n_T = count_nucleotides(dna)
        l = len(dna)
        results["A"][name] = n_A / l
        results["G"][name] = n_G / l
        results["C"][name] = n_C / l
        results["T"][name] = n_T / l

    for nucleotide, result in results.items():
        k = max(result, key=result.get)
        print(f"Sequence {k} had max average for {nucleotide}")

mRNA_mapping = {
    Nucleotide.T: 'A',
    Nucleotide.A: 'U',
    Nucleotide.G: 'C',
    Nucleotide.C: 'G',
    Nucleotide.WIlDCARD: '*',
}

def export_to_mRNA(file: str, data: Dict[str, List[Nucleotide]]):
    with open(file, "w") as f:
        for name, dna in data.items():
            f.write(f"% {name}\n")
            for i, c in enumerate(dna):
                f.write(mRNA_mapping[c])
                if (i+1) % 40 == 0:
                    f.write("\n")
            f.write("\n\n")


if __name__ == "__main__":
    # generate_dat_file()
    d = parse_data("gene_data.dat")
    count_max(d)
    export_to_mRNA("gene_data_mrna.dat", d)
    d2 = parse_data("gene_data_mrna.dat")