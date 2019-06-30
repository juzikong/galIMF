def custom_imf(mass, time):  # there is no time dependence for Kroupa IMF
    if mass < 0.08:
        return 0
    elif mass < 0.5:
        return 2*mass**(-1.3)
    elif mass < 150:
        return mass**(-2.3)
    else:
        return 0


# def mass_function(mass):
#     m = custom_imf(mass)*mass
#     return m
#
# from scipy.integrate import quad
#
# m1 = quad(mass_function, 0.08, 10, limit=50)[0]
# m2 = quad(mass_function, 10, 150, limit=50)[0]
# print(m1)
# print(m2)
# print(m1/m2)


# # for star + brown dwarf:
# def custom_imf_pbd(mass):  # there is no time dependence for Kroupa IMF
#     if mass < 0.01:
#         return 0
#     elif mass < 0.08:
#         return (2/0.08)*mass**(-0.3)
#     elif mass < 0.5:
#         return 2*mass**(-1.3)
#     elif mass < 150:
#         return mass**(-2.3)
#     else:
#         return 0





###  plot the mass fraction of low mass stars
#
from scipy.integrate import quad
import matplotlib.pyplot as plt


# def custom_imf_pbd(mass):  # there is no time dependence for Kroupa IMF
#     if mass < 0.08:
#         return (2/0.08)*mass**(-0.3)*mass
#     elif mass < 0.5:
#         return 2*mass**(-1.3)*mass
#     elif mass < 150:
#         return mass**(-2.3)*mass
#     else:
#         return 0
#
# def mass_ratio(limit):
#     a = quad(custom_imf_pbd, 0.00000001, 200, limit=100)[0]
#     b = quad(custom_imf_pbd, 0.00000001, limit, limit=100)[0]
#     ratio = b / a * 100
#     return ratio
#
# limit_list = []
# ratio_list = []
# limit = 0.001
# while limit < 200:
#     limit_list.append(limit)
#     ratio = mass_ratio(limit)
#     ratio_list.append(ratio)
#     (limit) = (limit*1.1)
#
# # print(limit_list)
# # print(ratio_list)
#
# plt.plot(limit_list, ratio_list)
#
# plt.xlabel(r'Mass limit [M$_\odot$]')
# plt.ylabel('Ratio [%]')
# plt.title('Mass fraction of the stars with mass smaller than given limit')
# plt.tight_layout()
# plt.show()
#

# a = quad(custom_imf_pbd, 0.2, 0.5, limit=100)[0]
# b = quad(custom_imf_pbd, 0.2, 1, limit=100)[0]
# print(a / b)
