
import numpy as np


def from_txt(filename, header=None, skiprows=0, comments=[]):
    with open(filename, 'r') as file:
        text = ''
        header_found = False
        for line in file:
            if header_found: text += line
            if header is not None and header in line: header_found = True

    data = []
    for l in text.splitlines()[skiprows:]:
        if any([c in l for c in comments]): continue
        row = list(map(float, l.split()))
        if len(row) != 0: data.append(row)

    return np.array(data).T


# -- Long time data

edc_yrBP, edc_co2_ppmv = from_txt(
    filename='edc-co2-2008.txt', header='3. Composite CO2 record (0-800 kyr BP)', skiprows=11)
edc_year = 2000 - edc_yrBP


# -- Intermediate time data

law_year, law_co2_ppmv = from_txt(
    filename='lawdome.combined.dat', header=' Mean Air Age,    CO2, 20 Year Smoothed', comments=['Mean', 'year'])

sidx = np.argsort(law_year)
law_year, law_co2_ppmv = law_year[sidx], law_co2_ppmv[sidx]


# -- Atmospheric measurments from present day

_, _, au_year, au_co2_ppm, _ = from_txt(
    filename='cfa_02D0_mm.co2', header='YYYY MM    Dec Date   CO2 (ppm)       SD')

idx = np.argwhere(au_co2_ppm != -999.)
au_year, au_co2_ppm = au_year[idx], au_co2_ppm[idx]


# -- Plot result

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 3))

def scale_year(year): return (2020 - year) / 1000.

plt.plot(scale_year(edc_year), edc_co2_ppmv, label='Composite ice core record')
plt.plot(scale_year(law_year), law_co2_ppmv, label='Law Dome ice core record')
plt.plot(scale_year(au_year), au_co2_ppm, label=r'Monthly mean of CO$_2$, Cape Ferguson, Australia')

plt.ylabel('Concentration CO$_2$ (ppmv)')
plt.xlabel('Thousand years before present (year 2020)')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()

plt.savefig('figure_co2_concentration.png', dpi=600)

plt.show()

