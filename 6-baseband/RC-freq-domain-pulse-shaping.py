import numpy as np
import impulse_responses as IR
from scipy.signal import lfilter
import matplotlib.pyplot as plt
import pandas as pd

# First set simulation frequencies and a bitstream
samp_rate = 100
symbol_rate = 1
bits=np.array([1,1,0,0,0,1,0,1])
num_periods=6 # from -3T to 3T
beta=0 # an ideal (although in this case truncated) filter

# make the bits range from -1 to 1 instead of 0 to 1
bits=2*bits-1

# Create a stream of impulses separated by T (in time) and fsT-1 (in samples)
impulses = np.zeros(len(bits)*samp_rate//symbol_rate)
impulses[::samp_rate//symbol_rate]=bits
# Append some zeros in order to let the filter "finish"
impulses=np.append(impulses,np.zeros(5*samp_rate//symbol_rate))

# Create the sinc shape
RC2_pulse, Tarr = IR.RC_freq_domain(symbol_rate,samp_rate,num_periods,beta)

# Convolve the sinc shape with the stream of impulses
filtered=lfilter(RC2_pulse,1,impulses)


# Make T arrays for each waveform
impulses_Ts= np.arange(0,len(impulses)/(samp_rate//symbol_rate),samp_rate**-1)
filtered_Ts = np.arange(0,len(filtered)/(samp_rate//symbol_rate),samp_rate**-1)

# Plot everything in case you're interested
plt.plot(impulses_Ts,impulses)
plt.plot(filtered_Ts,filtered)
plt.show()


# Put it all into pandas and export to CSV
im = pd.DataFrame({'imT':impulses_Ts,'im':impulses})
fil = pd.DataFrame({'filT':filtered_Ts,'fil':filtered})
# To plot overlapping pulses in TikZ we also need the pulse shape starting at time 0 (not -3T)
h=pd.DataFrame({'hT':Tarr+num_periods//2, 'h':RC2_pulse})
# Concatenate everything
csvDF = pd.concat([im,fil,h], axis=1)
csvDF.to_csv("impulses-shaped-by-RC-freq-domain-pulse.csv", index=False)