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


def sum_for_year(data: defaultdict) -> dict:
    result = defaultdict(lambda: defaultdict(int))
    for ym, items in data.items():
        year = ym[:4]
        for label, amount in items.items():
            result[year][label] += amount

    return dict(result)


fn = "Energy.txt"
#fn = "Polutants.txt"

by_period, by_label = read_data(fn)

compute_total(by_period)
compute_total(by_label)

by_year = sum_for_year(by_period)

# Print by label: label, total production
label_width = 0
for label in by_label:
    label_width = max(len(label), label_width)
heading = "Production type" + " " * label_width
heading = heading[:label_width] + "         GWh"
print(heading)
print("-" * (label_width + 12))

for label, items in by_label.items():
    print(f"{label:{label_width}}  {items['total']:10}")
print()

# Print by year: year, total energy production per kind
labels = set()
for year in by_year:
    for label in by_label:
        labels.add(label)
labels = list(labels)
labels.sort()

print(" GWh" + " " * (label_width - 4), end="")
for year in by_year:
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
print()
