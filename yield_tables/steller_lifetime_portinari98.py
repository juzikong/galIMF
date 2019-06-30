# Stellar lifetime table from Portinari+ 1998 their Table 14.
# Galactic chemical enrichment with new metallicity dependent stellar yields
# http://adsabs.harvard.edu/abs/1998A%26A...334..505P

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import math

Mass = [0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5,
        1.6, 1.7, 1.8, 1.9, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0,
        7.0, 9.0, 12., 15., 20., 30., 40., 60., 100, 120]
Metallicity = [0.0004, 0.004, 0.008, 0.02, 0.05]
Age = [[4.28E+10, 2.37E+10, 1.41E+10, 8.97E+09, 6.03E+09, 4.23E+09, 3.08E+09, 2.34E+09, 1.92E+09, 1.66E+09, 1.39E+09, 1.18E+09, 1.11E+09, 9.66E+08, 8.33E+08, 4.64E+08, 3.03E+08, 1.61E+08, 1.01E+08, 7.15E+07, 5.33E+07, 3.42E+07, 2.13E+07, 1.54E+07, 1.06E+07, 6.90E+06, 5.45E+06, 4.20E+06, 3.32E+06, 3.11E+06],
       [5.35E+10, 2.95E+10, 1.73E+10, 1.09E+10, 7.13E+09, 4.93E+09, 3.52E+09, 2.64E+09, 2.39E+09, 1.95E+09, 1.63E+09, 1.28E+09, 1.25E+09, 1.23E+09, 1.08E+09, 5.98E+08, 3.67E+08, 1.82E+08, 1.11E+08, 7.62E+07, 5.61E+07, 3.51E+07, 2.14E+07, 1.52E+07, 1.05E+07, 6.85E+06, 5.44E+06, 4.19E+06, 3.38E+06, 3.23E+06],
       [6.47E+10, 3.54E+10, 2.09E+10, 1.30E+10, 8.46E+09, 5.72E+09, 4.12E+09, 2.92E+09, 2.36E+09, 2.18E+09, 1.82E+09, 1.58E+09, 1.41E+09, 1.25E+09, 1.23E+09, 6.86E+08, 4.12E+08, 1.93E+08, 1.15E+08, 7.71E+07, 5.59E+07, 3.44E+07, 2.10E+07, 1.49E+07, 1.01E+07, 6.65E+06, 5.30E+06, 4.15E+06, 3.44E+06, 3.32E+06],
       [7.92E+10, 4.45E+10, 2.61E+10, 1.59E+10, 1.03E+10, 6.89E+09, 4.73E+09, 3.59E+09, 2.87E+09, 2.64E+09, 2.18E+09, 1.84E+09, 1.59E+09, 1.38E+09, 1.21E+09, 7.64E+08, 4.56E+08, 2.03E+08, 1.15E+08, 7.45E+07, 5.31E+07, 3.17E+07, 1.89E+07, 1.33E+07, 9.15E+06, 6.13E+06, 5.12E+06, 4.12E+06, 3.39E+06, 3.23E+06],
       [7.18E+10, 4.00E+10, 2.33E+10, 1.42E+10, 8.88E+09, 5.95E+09, 4.39E+09, 3.37E+09, 3.10E+09, 2.51E+09, 2.06E+09, 1.76E+09, 1.51E+09, 1.34E+09, 1.24E+09, 6.58E+08, 3.81E+08, 1.64E+08, 8.91E+07, 5.67E+07, 3.97E+07, 2.33E+07, 1.39E+07, 9.95E+06, 6.99E+06, 5.15E+06, 4.34E+06, 3.62E+06, 3.11E+06, 3.11E+06]]


# f = interpolate.interp2d(Mass, Metallicity, Age, kind='cubic')
#
# len_mass = len(Mass)
# log_Mass = []
# for i in range(len_mass):
#     log_Mass.append(math.log(Mass[i], 10))
#
# len_metal = len(Metallicity)
# log_Metallicity = []
# for i in range(len_metal):
#     log_Metallicity.append(math.log(Metallicity[i], 10))
#
# log_Age = []
# for i in range(len_metal):
#     log_Age.append([])
#     for j in range(len_mass):
#         log_Age[i].append(math.log(Age[i][j], 10))
#
# for i in range(len_metal):
#     plt.scatter(log_Mass, log_Age[i], s=10, edgecolors='k', linewidth='1')



# Mass_low = math.log(0.07, 10)
# Mass_high = math.log(151, 10)
# Mass_interval = (Mass_high - Mass_low) / 100
# Mass_log = np.arange(Mass_low, Mass_high, Mass_interval)
# Mass_new = 10**Mass_log
# len_mass = len(Mass_new)
#
# Age_new = []
# for i in range(len_metal):
#     Age_new.append([])
#     for j in range(len_mass):
#         Age_new[i].append(math.log(f(Mass_new[j], Metallicity[i]), 10))


# for i in range(len_metal):
#     plt.loglog(Mass, Age[i])

# Mass_low = math.log(0.07, 10)
# Mass_high = math.log(151, 10)
# Mass_interval = (Mass_high - Mass_low) / 100
#
# Mass_log = np.arange(Mass_low, Mass_high, Mass_interval)
# Metallicity_log = Metallicity
#
# Mass_log_new = 10**Mass_log
# Metallicity_log_new = Metallicity
#
# Age_new = f(Mass_log_new, Metallicity_log_new)
# # plt.plot(x, z[0, :], 'ro-', xnew, znew[0, :], 'b-')
# # plt.show()
# #
#
# Age_new_log = []
# for i in range(len(Age_new)):
#     Age_new_log.append([])
#     for j in range(len(Age_new[i])):
#         Age_new_log[i].append(math.log(Age_new[i, j], 10))


# print(Age_new_log)


# fig, ax = plt.subplots(1, 1)
#
# c = ax.pcolor(Mass, Metallicity, Age)
# fig.colorbar(c, ax=ax)
#
# # c = ax1.pcolor(Mass_log_new, Metallicity_log_new, Age_new_log, cmap='PuBu_r')
# # fig.colorbar(c, ax=ax1)
# plt.show()



###### for remnant mass ######

Mass = [9, 12, 15, 20, 30, 40, 60, 100, 120]
Metallicity = [0.0004, 0.004, 0.008, 0.02, 0.05]
Remnant_mass = [
    [1.35, 1.5, 1.8, 2.07, 6.98, 14.91, 24.58, 32.06, 30.6],
    [1.35, 1.5, 1.82, 2.04, 6.98, 12.6, 36.7, 35.2],
    [1.35, 1.48, 1.84, 2.04, 6.9, 12.5, 5.69, 9.89],
    [1.31, 1.44, 1.87, 2.11, 7.18, 2.06, 2.09, 2.12, 2.11],
    [1.31, 1.49, 1.98, 2.38, 1.55, 1.70, 1.68, 1.68]
]
