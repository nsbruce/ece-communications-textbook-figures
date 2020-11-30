import numpy as np
import impulse_responses as IR
from scipy.signal import lfilter, freqz
import matplotlib.pyplot as plt
import pandas as pd

# First set simulation frequencies and a bitstream
samp_rate = 100
symbol_rate = 1
bits=np.array([1,1,0,0,0,1,0,1])

# make them go from -1 to 1 instead of 0 to 1
bits=2*bits-1
# Repeat for square bits
square_bits=np.repeat(bits,samp_rate//symbol_rate)

# When dealing with square pulses in this section of the
# textbook we're not trying to learn about the Bessel filter
# so it is sufficient to enforce that the output be an RC2 pulse

impulses = np.zeros(len(bits)*samp_rate//symbol_rate)
impulses[::samp_rate//symbol_rate]=bits
impulses=np.append(impulses,np.zeros(samp_rate//symbol_rate))
RC2_pulse, _ = IR.RC2_time_domain(symbol_rate,samp_rate)
filtered=lfilter(RC2_pulse,1,impulses)


# Make T arrays for each waveform
square_wave_Ts = np.arange(0,len(square_bits)/(samp_rate//symbol_rate),samp_rate**-1)
impulses_Ts= np.arange(0,len(impulses)/(samp_rate//symbol_rate),samp_rate**-1)
filtered_Ts = np.arange(0,len(filtered)/(samp_rate//symbol_rate),samp_rate**-1)

# # Plot everything in case you're interested
plt.plot(square_wave_Ts,square_bits)
plt.plot(impulses_Ts,impulses)
plt.plot(filtered_Ts,filtered)
plt.show()


# Put it all into pandas and export to CSV
sq = pd.DataFrame({'sqT':square_wave_Ts,'sq':square_bits})
im = pd.DataFrame({'imT':impulses_Ts,'im':impulses})
fil = pd.DataFrame({'filT':filtered_Ts,'fil':filtered})
csvDF = pd.concat([sq,im,fil], axis=1)
csvDF.to_csv("square-pulses-shaped-by-bessel-filter.csv", index=False)