import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("pollutants.txt")
print(f"Loaded shape: {data.shape}")
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


# A 0.5p
pol_sum = np.sum(data, axis=1)
print(f"pol_sum shape: {pol_sum.shape}")

# B 2p
# Looping is over pollutants would be fine here, but numpy has many tools:
t_items = np.char.find(pollutants, '(t)')  != -1 # -1 denotes no substring was found
kg_items = np.char.find(pollutants, '(kg)') != -1
o_items = np.logical_not(t_items | kg_items)

pollutants = np.array(pollutants)

fig, axs = plt.subplots(2, 3)
axs[0, 0].plot(years, pol_sum[t_items].T, label=pollutants[t_items])
axs[0, 1].plot(years, pol_sum[kg_items].T, label=pollutants[kg_items])
axs[0, 2].plot(years, pol_sum[o_items].T, label=pollutants[o_items])

# C 2.5p
sec_sum_t = np.sum(data[t_items], axis=0)
sec_sum_kg = np.sum(data[kg_items], axis=0)
sec_sum_o = np.sum(data[o_items], axis=0)
print(f"sec_sum shapes: {sec_sum_t.shape}, {sec_sum_kg.shape}, {sec_sum_o.shape}")

axs[1, 0].plot(years, sec_sum_t.T, label=sectors)
axs[1, 1].plot(years, sec_sum_kg.T, label=sectors)
axs[1, 2].plot(years, sec_sum_o.T, label=sectors)

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
            axs[i, j].set(ylabel='ton')
        elif j == 1:
            axs[i, j].set(ylabel='kg')
        else:
            axs[i, j].set(ylabel='g')

plt.show()
