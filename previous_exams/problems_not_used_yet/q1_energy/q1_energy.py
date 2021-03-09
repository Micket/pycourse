from collections import defaultdict


def read_data(filename: str) -> (dict, dict):
    by_period = defaultdict(dict)
    by_label = defaultdict(dict)

    with open(filename) as fp:
        fp.readline()  # Skip header
        for line in fp:
            parts = line.strip().split()
            amount = parts.pop()
            if amount == "..":
                continue
            else:
                amount = float(amount)

            period = parts.pop()
            label = " ".join(parts)

            by_period[period][label] = amount
            by_label[label][period] = amount

    return dict(by_period), dict(by_label)


def compute_total(data: dict):
    for label in data:
        total = 0
        for amount in data[label].values():
            total += amount

        data[label]["total"] = total


def sum_for_year(data: dict) -> dict:
    result = defaultdict(lambda: defaultdict(int))
    for ym, items in data.items():
        year = ym[:4]
        for label, amount in items.items():
            result[year][label] += amount

    return dict(result)


def print_summary(data: dict):
    # Print by label: label, total production
    label_width = 0
    for label in data:
        label_width = max(len(label), label_width)
    heading = head + " " * label_width
    heading = heading[:label_width] + " " * (12 - len(unit)) + unit
    print(heading)
    print("-" * (label_width + 12))

    for label, items in data.items():
        print(f"{label:{label_width}}  {items['total']:10}")


def print_yearly(data: dict):
    # Print by year: year, total energy production per kind
    labels = set()
    for year, l in data.items():
        for label in l:
            labels.add(label)
    labels = list(labels)
    labels.sort()

    label_width = 0
    for label in labels:
        label_width = max(len(label), label_width)

    print(" " + unit + " " * (label_width - len(unit) - 1), end="")
    for year in data:
        print(f"{year:>9}", end="")
    print()

    print("-" * (label_width + 9 * len(by_year)))
    for label in labels:
        print(f"{label:{label_width}}", end="")
        for year, items in by_year.items():
            print(f"{items[label]:>9}", end="")
        print()

    print("-" * (label_width + 9 * len(by_year)))
    print(" TOTAL" + " " * (label_width - 6), end="")
    for year, items in by_year.items():
        print(f"{items['total']:>9}", end="")


fn = "Energy.txt"
head = "Produktionsslag"
unit = "GWh"
#head = "Type"
#fn = "test-data.txt"
#unit = "No."

by_period, by_label = read_data(fn)

compute_total(by_period)
compute_total(by_label)

by_year = sum_for_year(by_period)

print_summary(by_label)
print()

print_yearly(by_year)
print()
