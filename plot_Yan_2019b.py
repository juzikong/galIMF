import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import lognorm
from matplotlib.collections import LineCollection

def plot_galaxy_evol():

    # Figure 1 mass_ratio

    galaxy_sfr = [-2, -1, 0, 1, 2, 3, 4]
    length_of_galaxy_sfr = len(galaxy_sfr)

    alive_stellar_mass = []
    alive_plus_remnant_mass = []
    alive_plus_remnant_mass_over_alive_mass = []

    i = 0
    while i < length_of_galaxy_sfr:
        file = open('plot_data_SFEN100_flat/plotting_data_from_galaxy_evol_LSFR{}/mass_ratio.txt'.format(galaxy_sfr[i]), 'r')
        mass_ratio = file.readlines()
        file.close()
        alive_stellar_mass.append(float(mass_ratio[1]))
        alive_plus_remnant_mass.append(float(mass_ratio[3]))
        alive_plus_remnant_mass_over_alive_mass.append(10 ** float(mass_ratio[5]))
        (i) = (i + 1)


    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    fig = plt.figure(1, figsize=(4, 3))
    ax1 = fig.add_subplot(1, 1, 1)
    color = 'tab:red'
    plt.plot(galaxy_sfr, alive_stellar_mass, lw=2, label='a: alive stars', color=color)
    plt.plot(galaxy_sfr, alive_plus_remnant_mass, lw=3, ls='dotted', label='b: alive+remnant', color=color)
    plt.plot([], [], lw=2, ls='dashed', label='a / b', color='tab:blue')
    plt.legend(prop={'size': 7}, loc='upper left')
    plt.xlabel(r'log$_{10}$(SFR [M$_\odot$/yr])')
    plt.ylabel(r'log$_{10}({M_{\rm Final}} [{\rm M}_\odot$])', color=color)  # within 10 Gyr, per stellar mass formed
    plt.tick_params(axis='y', labelcolor=color)
    # plt.ylim(0, 0.005)
    ax2 = ax1.twinx()
    color = 'tab:blue'
    plt.ylabel(r'Mass ratio', color=color)
    plt.plot(galaxy_sfr, alive_plus_remnant_mass_over_alive_mass, lw=2, label='ratio', ls='dashed', color=color)
    plt.tick_params(axis='y', labelcolor=color)
    plt.ylim(1, 2.3)
    plt.xlim(-2.3, 4.3)
    plt.tight_layout()
    plt.savefig('../paper_plots2/mass_ratio.pdf', dpi=250)




    # Figure 2 SN_number_mass

    galaxy_sfr = [-2, -1, 0, 1, 2, 3, 4]
    length_of_galaxy_sfr = len(galaxy_sfr)

    SNIa_number_per_stellar_mass_formed = []
    SNII_number_per_stellar_mass_formed = []

    i = 0
    while i < length_of_galaxy_sfr:
        file = open('plot_data_SFEN100_flat/plotting_data_from_galaxy_evol_LSFR{}/SN_number_mass.txt'.format(galaxy_sfr[i]), 'r')
        mass_ratio = file.readlines()
        file.close()
        SNIa_number_per_stellar_mass_formed.append(float(mass_ratio[1]))
        SNII_number_per_stellar_mass_formed.append(float(mass_ratio[3]))
        (i) = (i + 1)

    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    fig = plt.figure(2, figsize=(4, 3))
    ax1 = fig.add_subplot(1, 1, 1)
    color = 'tab:red'
    plt.plot(galaxy_sfr, SNIa_number_per_stellar_mass_formed, lw=2, color=color)
    plt.xlabel(r'log$_{10}$(SFR [M$_\odot$/yr])')
    plt.ylabel(r'SNIa #', color=color)  # within 10 Gyr, per stellar mass formed
    plt.tick_params(axis='y', labelcolor=color)
    plt.ylim(0, 0.005)
    ax2 = ax1.twinx()
    color = 'tab:blue'
    plt.ylabel(r'SNII #', color=color)
    plt.plot(galaxy_sfr, SNII_number_per_stellar_mass_formed, lw=2, label='SNII', ls='dashed', color=color)
    plt.plot([], [], lw=2, label='SNIa', color='tab:red')
    plt.tick_params(axis='y', labelcolor=color)
    plt.ylim(0, 1)
    plt.legend(prop={'size': 7}, loc='upper left')
    plt.xlim(-2.3, 4.3)
    plt.tight_layout()
    plt.savefig('../paper_plots2/SN_number_mass.pdf', dpi=250)



    # Figure 3 energy_evolution

    file = open('simulation_results_from_galaxy_evol/plots/energy_evolution.txt', 'r')
    energy_evolution = file.readlines()
    file.close()

    time_axis = [float(x) for x in energy_evolution[1].split()]
    SN_energy_per_current_crossing_time_list = [float(x) for x in energy_evolution[7].split()]
    SN_energy_per_final_crossing_time_list = [float(x) for x in energy_evolution[9].split()]
    total_energy_release_list = [float(x) for x in energy_evolution[11].split()]
    binding_energy_list = [float(x) for x in energy_evolution[13].split()]
    total_gas_kinetic_energy_list = [float(x) for x in energy_evolution[15].split()]

    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    fig = plt.figure(3, figsize=(4, 3.5))
    fig.add_subplot(1, 1, 1)
    plt.loglog(time_axis, SN_energy_per_current_crossing_time_list, label='SN/CC')
    plt.loglog(time_axis, SN_energy_per_final_crossing_time_list, label='SN/FC')
    plt.loglog(time_axis, total_energy_release_list, label='Total SN')
    plt.loglog(time_axis, binding_energy_list, ls="dashed", label='Gravitational binding')
    plt.loglog(time_axis, total_gas_kinetic_energy_list, ls="dotted", label='Gas kinetic')
    plt.xlabel(r'time [yr]')
    plt.ylabel(r'Energy [erg]')
    plt.legend(prop={'size': 6}, loc='best')
    plt.tight_layout()



    # Figure 4 energy_mass

    galaxy_sfr = [-2, -1, 0, 1, 2, 3, 4]
    length_of_galaxy_sfr = len(galaxy_sfr)

    Log_SN_energy_release = []
    Log_binding_energy = []
    Log_gas_kinetic_energy = []
    Log_SN_energy_release1 = []
    Log_binding_energy1 = []
    Log_gas_kinetic_energy1 = []

    i = 0
    while i < length_of_galaxy_sfr:
        file = open('plot_data_SFEN100_flat/plotting_data_from_galaxy_evol_LSFR{}/energy_evolution.txt'.format(galaxy_sfr[i]), 'r')
        energy_evolution = file.readlines()
        file.close()

        total_energy_release_list = [float(x) for x in energy_evolution[7].split()]
        binding_energy_list = [float(x) for x in energy_evolution[9].split()]
        total_gas_kinetic_energy_list = [float(x) for x in energy_evolution[11].split()]

        Log_SN_energy_release1.append(math.log(total_energy_release_list[-2], 10))
        Log_binding_energy1.append(math.log(binding_energy_list[-2], 10))
        Log_gas_kinetic_energy1.append(math.log(total_gas_kinetic_energy_list[-2], 10))
        (i) = (i + 1)

    i = 0
    while i < length_of_galaxy_sfr:
        file = open('plot_data_SFEN100_flat/plotting_data_from_galaxy_evol_LSFR{}/energy_mass.txt'.format(galaxy_sfr[i]), 'r')
        energy_mass = file.readlines()
        file.close()
        Log_SN_energy_release.append(math.log(float(energy_mass[1]), 10))
        Log_binding_energy.append(math.log(float(energy_mass[3]), 10))
        Log_gas_kinetic_energy.append(math.log(float(energy_mass[5]), 10))
        (i) = (i + 1)

    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    fig = plt.figure(4, figsize=(4, 3.5))
    ax = fig.add_subplot(1, 1, 1)
    plt.plot(galaxy_sfr, Log_SN_energy_release, lw=2, label='Total SN')
    plt.plot(galaxy_sfr, Log_binding_energy, lw=2, ls="dashed", label='Gravitational binding')
    plt.plot(galaxy_sfr, Log_gas_kinetic_energy, lw=2, ls="dotted", label='Gas kinetic')
    plt.plot(galaxy_sfr, Log_SN_energy_release1, lw=2, label='Total SN 1Gyr')
    plt.plot(galaxy_sfr, Log_binding_energy1, lw=2, ls="dashed", label='Gravitational binding 1Gyr')
    plt.plot(galaxy_sfr, Log_gas_kinetic_energy1, lw=2, ls="dotted", label='Gas kinetic 1Gyr')
    plt.xlabel(r'log$_{10}$(SFR [M$_\odot$/yr])')
    plt.ylabel(r'log$_{10}$(Final energy [erg])')
    plt.xlim(-2.3, 4.3)
    # plt.ylim(8.5, 11.6)
    plt.legend(prop={'size': 7}, loc='best')
    plt.tight_layout()
    plt.savefig('../paper_plots2/energy_mass.pdf', dpi=250)


    # Figure 5 expansion_factor

    file = open('simulation_results_from_galaxy_evol/plots_extended/expansion_factor.txt', 'r')
    expansion_factor = file.readlines()
    file.close()

    time_axis = [float(x) for x in expansion_factor[1].split()]
    expansion_factor_list = [math.log(float(x), 10) for x in expansion_factor[3].split()]
    expansion_factor_instantaneous_list = [math.log(float(x), 10) for x in expansion_factor[5].split()]
    expansion_factor_adiabatic_list = [math.log(float(x), 10) for x in expansion_factor[7].split()]

    file = open('simulation_results_from_galaxy_evol/plots_IGIMF/expansion_factor.txt', 'r')
    expansion_factor0 = file.readlines()
    file.close()

    time_axis0 = [float(x) for x in expansion_factor0[1].split()]
    expansion_factor0_list = [math.log(float(x), 10) for x in expansion_factor0[3].split()]
    expansion_factor0_instantaneous_list = [math.log(float(x), 10) for x in expansion_factor0[5].split()]
    expansion_factor0_adiabatic_list = [math.log(float(x), 10) for x in expansion_factor0[7].split()]


    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    fig = plt.figure(5, figsize=(4, 3.5))
    fig.add_subplot(1, 1, 1)
    plt.plot(time_axis, expansion_factor_list, color="tab:red")
    plt.plot(time_axis0, expansion_factor0_list, color="tab:blue")
    plt.plot([], [], label='Log-average', color="k")
    plt.plot(time_axis, expansion_factor_instantaneous_list, ls="dashed", color="tab:red")
    plt.plot(time_axis0, expansion_factor0_instantaneous_list, ls="dashed", color="tab:blue")
    plt.plot([], [], ls="dashed", label='Instantaneous', color="k")
    plt.plot(time_axis, expansion_factor_adiabatic_list, ls="dotted", color="tab:red")
    plt.plot(time_axis0, expansion_factor0_adiabatic_list, ls="dotted", color="tab:blue")
    plt.plot([], [], ls="dotted", label='Adiabatic', color="k")
    plt.plot([], [], lw=3, label=r'SFR=10$^3$ M$_\odot$/yr', color="tab:red")
    plt.plot([], [], lw=3, label=r'SFR=1 M$_\odot$/yr', color="tab:blue")
    plt.xlabel(r'log$_{10}$(time [yr])')
    plt.ylabel(r'log$_{10}$(Expansion factor)')
    plt.xlim(7, time_axis[-1])
    plt.legend(prop={'size': 7}, loc='best')
    plt.tight_layout()






    # Figure 6 Z_over_X_mass

    galaxy_sfr = [-2, -1, 0, 1, 2, 3, 4]
    length_of_galaxy_sfr = len(galaxy_sfr)

    gas_Z_over_X = []
    stellar_Z_over_X = []

    i = 0
    while i < length_of_galaxy_sfr:
        file = open('plot_data_SFEN100_flat/plotting_data_from_galaxy_evol_LSFR{}/Z_over_X_mass.txt'.format(galaxy_sfr[i]), 'r')
        Z_over_X_mass = file.readlines()
        file.close()
        gas_Z_over_X.append(float(Z_over_X_mass[1]))
        stellar_Z_over_X.append(float(Z_over_X_mass[3]))
        (i) = (i + 1)

    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    fig = plt.figure(6, figsize=(4, 3.5))
    ax1 = fig.add_subplot(1, 1, 1)
    plt.plot(galaxy_sfr, gas_Z_over_X, lw=2, label='gas', color='k', ls='dashed')
    plt.plot(galaxy_sfr, stellar_Z_over_X, lw=2, label='stellar', color='k')
    plt.ylabel(r'[Z/X]')
    plt.xlabel(r'log$_{10}$(SFR [M$_\odot$/yr])')
    plt.xlim(-2.3, 4.3)
    plt.plot([], [], ls='dotted', c='r', lw=2, label='data')
    ax2 = ax1.twiny()
    plt.xlabel(r'log$_{10}(\sigma$ [km/s])', color='r')
    plt.tick_params(axis='x', labelcolor='r')
    plt.plot([2, 2.5], [0.76 * 2 - 0.73 - 0.87, 0.76 * 2.5 - 0.73 - 0.87], ls='dotted', c='r', lw=2, label='data')  # Trager 2000 assuming a fixed t=10Gyr
    plt.plot([2.1, 2.5], [0.05, 0.36], ls='dotted', c='r', lw=2)  # Thomas 621:673–694, 2005
    plt.plot([1.935, 2.088, 2.173, 2.257, 2.386], [0.05, 0.11, 0.15, 0.18, 0.24], ls='dotted', c='r', lw=2)  # Nelan ApJ 632:137 2005 Table 8
    plt.plot([2.0, 2.4], [-0.168, 0.1984], ls='dotted', c='r', lw=2)  # Graves et al. 671:243-271, 2007. Assuming [O/Fe] = [Mg/Fe]
    plt.plot([1.9, 2.35], [-0.105, 0.1875], ls='dotted', c='r', lw=2)  # Thomas 404, 1775–1789 (2010)
    plt.plot([1.8, 2.4], [0.016, 0.148], ls='dotted', c='r', lw=2)  # Johansson 2012 421-1908
    plt.errorbar([2.49, 2.52], [0.35, 0.38], xerr=[0.0042, 0.0039], yerr=[0.02, 0.02], c="r", ls='none')  # LaBarbera MNRAS 464, 3597–3616 (2017)
    plt.plot([], [], lw=2, label='gas', color='k', ls='dashed')
    plt.plot([], [], lw=2, label='stellar', color='k')
    plt.xlim(1.252, 2.548)
    # plt.ylim(8.5, 11.6)
    plt.legend(prop={'size': 7}, loc='upper left')
    plt.tight_layout()
    plt.savefig('../paper_plots2/Z_over_X_mass.pdf', dpi=250)

    # Figure 19 Fe_over_H_mass

    galaxy_sfr = [-2, -1, 0, 1, 2, 3, 4]
    length_of_galaxy_sfr = len(galaxy_sfr)

    gas_Fe_over_H = []
    stellar_Fe_over_H = []

    i = 0
    while i < length_of_galaxy_sfr:
        file = open('plot_data_SFEN100_flat/plotting_data_from_galaxy_evol_LSFR{}/Fe_over_H_mass.txt'.format(galaxy_sfr[i]), 'r')
        Fe_over_H_mass = file.readlines()
        file.close()
        gas_Fe_over_H.append(float(Fe_over_H_mass[1]))
        stellar_Fe_over_H.append(float(Fe_over_H_mass[3]))
        (i) = (i + 1)

    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    fig = plt.figure(19, figsize=(4, 3.5))
    ax1 = fig.add_subplot(1, 1, 1)
    plt.plot(galaxy_sfr, gas_Fe_over_H, label='gas', lw=2, color='k', ls='dashed')
    plt.plot(galaxy_sfr, stellar_Fe_over_H, label='stellar', lw=2, color='k')
    plt.xlabel(r'log$_{10}$(SFR [M$_\odot$/yr])')
    plt.ylabel(r'[Fe/H]')
    plt.xlim(-2.3, 4.3)
    plt.plot([], [], ls='dotted', c='r', lw=2, label='data')
    plt.legend(prop={'size': 7}, loc='best')
    ax2 = ax1.twiny()
    plt.xlabel(r'log$_{10}(\sigma$ [km/s])', color='r')
    plt.tick_params(axis='x', labelcolor='r')
    plt.plot([2, 2.5], [0.48 * 2 - 0.74 - 0.4, 0.48 * 2.5 - 0.74 - 0.4], ls='dotted', c='r', lw=2, label='data')  # Trager 2000 assuming a fixed t=10Gyr  # recalibrated [Fe/H] with [Fe/H] = [Z/H] - A[Mg/Fe] where A=0.94
    plt.plot([2.1, 2.5], [0.05 - 0.94 * 0.15, 0.36 - 0.94 * 0.31], ls='dotted', c='r', lw=2)  # Thomas 621:673–694, 2005  # recalibrated [Fe/H] with [Fe/H] = [Z/H] - A[Mg/Fe] where A=0.94
    plt.plot([2, 2.5], [-0.24, 0], ls='dotted', c='r', lw=2)  # Graves et al. 671:243-271, 2007
    plt.plot([1.9, 2.5], [-0.17, 0.03], ls='dotted', c='r', lw=2)  # Graves & Schiavon 2008
    plt.plot([1.9, 2.35], [-0.105 - 0.94 * 0.077, 0.1875 - 0.94 * 0.2255], ls='dotted', c='r', lw=2)  # Thomas 404, 1775–1789 2010  # recalibrated [Fe/H] with [Fe/H] = [Z/H] - A[Mg/Fe] where A=0.94
    plt.plot([1, 1.7, 2.5], [-1.5, 0, 0], ls='dotted', c='r', lw=2)  # Koleva et al. 417, 1643–1671 (2011)
    plt.plot([1.8, 2.4], [-0.074, -0.092], ls='dotted', c='r', lw=2)  # Johansson 2012
    plt.plot([1.7, 2.48], [0, 0], ls='dotted', c='r', lw=2)  # Eigenthaler & Zeilinger  A&A 553, A99 (2013)
    plt.plot([1.94, 2.48], [-0.07, 0], ls='dotted', c='r', lw=2)  # Conroy 2014 780-33
    plt.plot([], [], lw=2, label='gas', color='k', ls='dashed')
    plt.plot([], [], lw=2, label='stellar', color='k')
    plt.xlim(1.252, 2.548)
    plt.ylim(-1, 0.5)
    # plt.legend(prop={'size': 7}, loc='best')
    plt.tight_layout()
    plt.savefig('../paper_plots2/Fe_over_H_mass.pdf', dpi=250)



    # Figure 7 Mg_over_Fe_mass

    galaxy_sfr = [-2, -1, 0, 1, 2, 3, 4]
    length_of_galaxy_sfr = len(galaxy_sfr)

    gas_Mg_over_Fe = []
    stellar_Mg_over_Fe = []

    i = 0
    while i < length_of_galaxy_sfr:
        file = open('plot_data_SFEN100_flat/plotting_data_from_galaxy_evol_LSFR{}/Mg_over_Fe_mass.txt'.format(galaxy_sfr[i]), 'r')
        Mg_over_Fe_mass = file.readlines()
        file.close()
        gas_Mg_over_Fe.append(float(Mg_over_Fe_mass[1]))
        stellar_Mg_over_Fe.append(float(Mg_over_Fe_mass[3]))
        (i) = (i + 1)

    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    fig = plt.figure(7, figsize=(4, 3.5))
    ax1 = fig.add_subplot(1, 1, 1)
    plt.plot(galaxy_sfr, gas_Mg_over_Fe, label='gas', lw=2, color='k', ls='dashed')
    plt.plot(galaxy_sfr, stellar_Mg_over_Fe, label='stellar', lw=2, color='k')
    plt.ylabel(r'[Mg/Fe]')
    plt.xlabel(r'log$_{10}$(SFR [M$_\odot$/yr])')
    plt.xlim(-2.3, 4.3)
    plt.plot([], [], ls='dotted', c='r', lw=2, label='data')
    # plt.legend(prop={'size': 7}, loc='best')
    ax2 = ax1.twiny()
    plt.xlabel(r'log$_{10}(\sigma$ [km/s])', color='r')
    plt.tick_params(axis='x', labelcolor='r')
    plt.plot([2, 2.5], [0.33 * 2 - 0.58, 0.33 * 2.5 - 0.58], ls='dotted', c='r', lw=2, label='data')  # Trager 2000
    plt.plot([2.1, 2.5], [0.15, 0.31], ls='dotted', c='r', lw=2)  # Thomas 621:673–694, 2005
    plt.plot([1.935, 2.088, 2.173, 2.257, 2.386], [0.13, 0.18, 0.20, 0.24, 0.28], ls='dotted', c='r', lw=2)  # Nelan ApJ 632:137 2005 Table 8
    plt.plot([1.94, 2.48], [0.12, 0.27], ls='dotted', c='r', lw=2)  # Graves 2007
    plt.plot([1.94, 2.48], [0.12, 0.27], ls='dotted', c='r', lw=2)  # Graves & Schiavon 2008
    plt.plot([1.5, 2, 2.48], [-0.24, 0.1, 0.34], ls='dotted', c='r', lw=2)  # Recchi 2009
    plt.plot([1.9, 2.35], [0.077, 0.2255], ls='dotted', c='r', lw=2)  # Thomas 404, 1775–1789 2010
    plt.plot([1.8, 2.4], [0.13, 0.31], ls='dotted', c='r', lw=2)  # Johansson 2012
    plt.plot([1.94, 2.48], [0.05, 0.22], ls='dotted', c='r', lw=2)  # Conroy 2014 780-33
    plt.errorbar([2.49, 2.52], [0.27, 0.38], xerr=[0.0042, 0.0039], yerr=[0.03, 0.03], lw=2, c="r", ls='none')  # LaBarbera MNRAS 464, 3597–3616 (2017)
    plt.plot([], [], lw=2, label='gas', color='k', ls='dashed')
    plt.plot([], [], lw=2, label='stellar', color='k')
    plt.xlim(1.252, 2.548)
    plt.legend(prop={'size': 7}, loc='best')
    plt.tight_layout()
    plt.savefig('../paper_plots2/Mg_over_Fe_mass.pdf', dpi=250)


    return

if __name__ == '__main__':
    # plots for two different set of simulations, i.e., boxy SFH and lognormal SFH:
    plot_galaxy_evol()
    # plot_galaxy_evol_extended()
    plt.show()
