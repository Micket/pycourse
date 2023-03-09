import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, optimize


# test data
rng = np.random.default_rng()
n = 100
study_time = rng.random(n)
exam_score = 25*np.minimum(np.arctan(study_time*3)*2/np.pi + rng.random(n)/(2+study_time*2), 1)

# data = np.loadtxt('grades.txt')


slope, intercept, r, p, se = stats.linregress(study_time, exam_score)

plt.scatter(study_time, exam_score)
x = np.linspace(0,1)
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
print(r, p, se)

# Maybe something with curve_fit
def func(x, a, b, c):
    return a*x + b*x**c

popt, pcov = optimize.curve_fit(func, study_time, exam_score)

ss_res = np.sum((exam_score - func(study_time, *popt))**2)
ss_tot = np.sum((exam_score - np.mean(exam_score))**2)
r2 = 1 - (ss_res / ss_tot)
print(r, r2)

plt.plot(x, func(x, *popt))


plt.show()
