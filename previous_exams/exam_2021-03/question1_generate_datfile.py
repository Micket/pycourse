import inspect
import random

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
                if (n + 1) % line_length == 0:
                    f.write('\n')
                    n = 0
            f.write("\n\n")


if __name__ == "__main__":
    generate_dat_file()
