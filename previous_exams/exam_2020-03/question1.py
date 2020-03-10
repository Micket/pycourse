
""" Question 1 """


# Part A


import numpy as np

filename = 'scb_degrees_per_year.csv'

with open(filename, 'r', encoding='ISO-8859-1') as file:

    title = file.readline()
    _ = file.readline()
    header = file.readline().strip().replace('"','').split(',')
    header, years = header[:4], header[4:]
    
    degrees = {}
    
    for line in file:
        row = line.strip().replace('"','').split(',')

        school, degree, gender, age = row[:4]
        no_degrees = np.array([ int(x) for x in row[4:] ])

        key = 'CTH' if 'Chalmers' in school else 'KTH'
        degrees[key] = no_degrees + degrees[key] if key in degrees else no_degrees


print('{:7s} | {:>5s}, {:>5s}'.format('Year', *degrees.keys()))
print('-'*24)
for item in zip(years, *degrees.values()):
    year, numbers = item[0], item[1:]
    print('{:>7s} | {:5d}, {:5d}'.format(year, *numbers))


# Part B


import matplotlib.pyplot as plt

for school, values in degrees.items():
    plt.plot(values, 'o-', label=school)

plt.ylabel('Number of awarded degrees')
plt.xlabel('Academic year')
plt.xticks(np.arange(len(years)), years, rotation=90, fontsize=7)
plt.legend(loc='best')
plt.ylim(bottom=0)
plt.tight_layout()
plt.show()
    
