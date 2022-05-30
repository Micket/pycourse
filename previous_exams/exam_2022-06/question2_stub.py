import numpy as np


data = np.loadtxt("pollutants.txt")
data = data.reshape(26, 11, 30)

years = np.arange(1990, 2020)

pollutants = ['Kväveoxider (t)', 'Flyktiga organiska ämnen, exkl. metan (t)', 'Svaveldioxid (t)',
              'Ammoniak (t)', 'PM2.5 (t)', 'PM10 (t)', 'TSP (t)', 'Sot (BC) (t)', 'Kolmonoxid (CO) (t)',
              'Bly (kg)', 'Kadmium (kg)', 'Kvicksilver (kg)', 'Arsenik (kg)', 'Krom (kg)',
              'Koppar (kg)', 'Nickel (kg)', 'Selen (kg)', 'Zink (kg)', 'Dioxin (g I-Teq)',
              'benso(a)pyren (kg)', 'benso(b)fluoranten (kg)', 'benso(k)fluoranten (kg)', 'Indeno(1,2,3-cd)pyren (kg)',
              'PAH 1-4 (kg)', 'HCB (kg)', 'PCB  (kg)']

sectors = ['Nationell total (exkl. utrikes transporter)', 'Nationell total',
           'Arbetsmaskiner', 'Avfall', 'El och fjärrvärme', 'Industri', 'Utrikes transporter', 'Jordbruk',
           'Lösningsmedel etc.', 'Inrikes transporter', 'Egen uppvärmning']
