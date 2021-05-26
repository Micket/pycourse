import csv
import numpy as np
import matplotlib.pyplot as plt


# Extra method and code to create input file starts here
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
# Extra method and code to create input file ends here


data = np.loadtxt("polutants.txt")
print(f"Loaded shape: {data.shape}")
data = data.reshape(26, 11, 30)

years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
         2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

polutants = ['Kväveoxider (NOx) (t)', 'Flyktiga organiska ämnen, exkl. metan (NMVOC) (t)', 'Svaveldioxid (SO2) (t)',
             'Ammoniak (NH3) (t)', 'PM2.5 (t)', 'PM10 (t)', 'TSP (t)', 'Sot (BC) (t)', 'Kolmonoxid (CO) (t)',
             'Bly (Pb) (kg)', 'Kadmium (Cd) (kg)', 'Kvicksilver (Hg) (kg)', 'Arsenik (As) (kg)', 'Krom (Cr) (kg)',
             'Koppar (Cu) (kg)', 'Nickel (Ni) (kg)', 'Selen (Se) (kg)', 'Zink (Zn) (kg)', 'Dioxin (g I-Teq)',
             'benso(a)pyren (kg)', 'benso(b)fluoranten (kg)', 'benso(k)fluoranten (kg)', 'Indeno(1,2,3-cd)pyren (kg)',
             'PAH 1-4 (kg)', 'HCB (kg)', 'PCB  (kg)']
sectors = ['NATIONELL TOTAL (exklusive internationella transporter)',
           'NATIONELL TOTAL (inklusive internationella transporter)', 'ARBETSMASKINER, TOTALT', 'AVFALL, TOTALT',
           'EL OCH FJÄRRVÄRME, TOTALT', 'INDUSTRI, TOTALT', 'UTRIKES TRANSPORTER, TOTALT', 'JORDBRUK, TOTALT',
           'LÖSNINGSMEDEL OCH ÖVRIG PRODUKTANVÄNDNING, TOTALT', 'INRIKES TRANSPORTER, TOTALT',
           'EGEN UPPVÄRMNING AV BOSTÄDER OCH LOKALER, TOTALT']


pol_mean = np.sum(data, axis=1)
print(f"pol_mean shape: {pol_mean.shape}")

kg_items = []
t_items = []
o_items = []
for i, label in enumerate(polutants):
    if "(kg)" in label:
        kg_items.append(i)
    elif "(t)" in label:
        t_items.append(i)
    else:
        o_items.append(i)

fig, axs = plt.subplots(2, 3)
for i, label in enumerate(polutants):
    if "(kg)" in label:
        axs[0, 0].plot(years, pol_mean[i], label=label)
    elif "(t)" in label:
        axs[0, 1].plot(years, pol_mean[i], label=label)
    else:
        axs[0, 2].plot(years, pol_mean[i], label=label)

sec_mean_kg = np.mean(data[kg_items,:,:], axis=0)
sec_mean_t = np.mean(data[t_items,:,:], axis=0)
sec_mean_o = np.mean(data[o_items,:,:], axis=0)
print(f"sec_mean shapes: {sec_mean_kg.shape}, {sec_mean_t.shape}, {sec_mean_o.shape}")

for i, label in enumerate(sectors):
    axs[1, 0].plot(years, sec_mean_kg[i], label=label)
    axs[1, 1].plot(years, sec_mean_t[i], label=label)
    axs[1, 2].plot(years, sec_mean_o[i], label=label)

for ax in axs.flat:
    ax.legend()
    ax.grid()
    ax.set(xlabel='year')
for i in range(2):
    for j in range(3):
        axs[i, j].legend()
        axs[i, j].grid()
        axs[i, j].set(xlabel='year')
        if j == 0:
            axs[i, j].set(ylabel='kg')
        elif j == 1:
            axs[i, j].set(ylabel='ton')
        else:
            axs[i, j].set(ylabel='g')

plt.show()
