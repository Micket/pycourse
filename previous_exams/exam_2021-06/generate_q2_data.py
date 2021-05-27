import csv
import numpy as np

def _read_csv_data(fn: str):
    with open(fn) as f:
        csv_reader = csv.reader(f, delimiter=";")

        polutants = []
        sectors = []

        # Read data once to get sizes
        for no, line in enumerate(csv_reader):
            if no < 2:
                continue
            elif no == 2:
                no_years = len(line) - 2
                # print("Header", line, len(line))
                years = [int(x) for x in line[2:]]
                continue

            polutant, sector = line[:2]
            if polutant in polutants:
                p_ind = polutants.index(polutant)
            else:
                p_ind = len(polutants)
                polutants.append(polutant)
            if sector in sectors:
                s_ind = sectors.index(sector)
            else:
                s_ind = len(sectors)
                sectors.append(sector)

        p_len = len(polutants)
        s_len = len(sectors)
        data = np.zeros((p_len, s_len, no_years))

    with open(fn) as f:
        csv_reader = csv.reader(f, delimiter=";")

        for no, line in enumerate(csv_reader):
            if no <= 2:
                continue

            polutant, sector = line[:2]
            p_ind = polutants.index(polutant)
            s_ind = sectors.index(sector)
            data[p_ind][s_ind] = [float(x) for x in line[2:]]

    return data, years, polutants, sectors


def _create_file(in_fn: str, out_fn: str, print_headers: bool = False):
    data, years, polutants, sectors = _read_csv_data(in_fn)
    if print_headers:
        print(years)
        print(polutants)
        print(sectors)
    print(f"Input data has shape: {data.shape}")
    np.savetxt(out_fn, data.reshape(data.shape[0] * data.shape[1], data.shape[2]))


_create_file("Polutants.csv", "polutants.txt", False)
