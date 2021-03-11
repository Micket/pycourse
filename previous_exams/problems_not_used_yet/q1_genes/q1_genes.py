from typing import Dict, List


def parse_data(file: str) -> Dict[str, List[str]]:
    data = {}
    with open(file, "r") as f:
        while True:
            l = f.readline().strip()
            if l == "":
                break  # Reached end of file

            # Read the comments
            while True:
                if not l.startswith('#'):
                    break
                l = f.readline().strip()

            # Read the name
            name = l.split("% ")[1]

            # Read the nucleotide data
            nucleotides = []
            while True:
                l = f.readline().strip()
                if l == "":
                    break
                nucleotides.extend(list(l))

            data[name] = nucleotides
    return data


def count_nucleotides(dna: List[str]):
    n_wildcards = dna.count('*')
    return [dna.count(c) + n_wildcards for c in ('A', 'G', 'T', 'C')]


def count_max_nucleotides(data: Dict[str, List[str]]) -> Dict[str, str]:
    results : Dict[str, dict[str, str]]
    results = {"A": {}, "G": {}, "T": {}, "C": {}}
    for name, dna in data.items():
        counts = count_nucleotides(dna)
        l = len(dna)
        for (i, c) in enumerate(('A', 'G', 'T', 'C')):
            results[c][name] = counts[i] / l
    max_n = {}
    for nucleotide, result in results.items():
        k = max(result, key=result.get)
        max_n[nucleotide] = k

    return max_n


mRNA_mapping = {
    'T': 'A',
    'A': 'U',
    'G': 'C',
    'C': 'G',
    '*': '*',
}


def export_to_mRNA(file: str, data: Dict[str, List[str]]):
    with open(file, "w") as f:
        for name, dna in data.items():
            f.write(f"% {name}\n")
            for i, c in enumerate(dna):
                f.write(mRNA_mapping[c])
                if (i + 1) % 40 == 0:
                    f.write("\n")
            f.write("\n\n")


if __name__ == "__main__":
    d = parse_data("gene_data.dat")
    maxes = count_max_nucleotides(d)
    print(maxes)
    export_to_mRNA("gene_data_mrna.dat", d)
    d2 = parse_data("gene_data_mrna.dat")
