# Python3 code

# An example


import galevo

print("\n    ================================\n"
      "    === example_galaxy_evolution ===\n"
      "    ================================\n")
print("    This test code serves as an example, "
      "explaining (see comments in the code) the input parameters of the galaxy chemical evolution model.\n")


Log_SFR = float(input(
    "    Please input the logarithmic star formation rate in the unit of solar mass per yr "
    "and ended the input with the return key.\n"
    "    A typical input SFR is from -4 to 4. "
    "Note that the code does not support extremely low SFR "
    "as the IMF integration error is significant for very top-light gwIMFs.\n\n"
    "    log_{10}(SFR [M_sun/yr]) = "))

SFH_shape = input(
    "\n\n    Please input the shape of the SFH "
    "and ended the input with the return key.\n"
    "    The input can only be: 1 for a flat SFH or 2 for a skewnorm SFH, where the latter cost more calculation time.\n\n"
    "    ")
if SFH_shape == '1':
    SFH_shape = 'flat'
elif SFH_shape == '2':
    SFH_shape = 'skewnorm'

# Other SFH shape parameters
location = 0
skewness = 10
sfr_tail = 0

SFEN = round(float(input(
    "\n\n    Please input the characteristic star formation timescale in the unit of 10 Myr (integer only) "
    "and ended the input with the return key.\n"
    "    We recommend a value smaller than 10 for 'flat' SFH and smaller than 3 for 'skewnorm' SFH for the first run, "
    "as longer timescale calculations take more time.\n\n"
    "    SFT [10Myr] = ")))
if SFEN < 1:
    print("\n\n### Warning: Wrong input 'SFEN' smaller than 1! Correct SFEN to 1. ###\n\n")
    SFEN = 1


print('\nGenerating new SFH...')
galevo.generate_SFH(SFH_shape, Log_SFR, SFEN, sfr_tail, skewness, location)

galevo.galaxy_evol(
    imf='igimf',
    STF=0.3,  # can be larger than 1 since gas is recycled from dying stars but if set too high
    # unrealistic results may generated if, at a later time step, more star are forming than the available gas mass.
    SFH_model='provided', SFE=0.013, SFEN=SFEN,  # Parameter "SFE" and "SFEN" is not applied when SFH_model='provided'.
    # printout_galevo_info=True,
    plot_show=True,
    # high_time_resolution=True,
    # plot_save=True,
    SNIa_ON=True,
    )