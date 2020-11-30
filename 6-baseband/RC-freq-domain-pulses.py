import numpy as np
import impulse_responses as IR
import frequency_responses as FR
from scipy.signal import lfilter, freqz
import matplotlib.pyplot as plt
import pandas as pd

# First set simulation frequencies and other parameters
samp_rate = 100
symbol_rate = 1 
num_periods = 6 # from -3T to 3T

# For the first part of this file we're going to
# plot the impulse response of the frequency domain
# RC shape. In the second part of the file we'll
# plot its frequency response.

# Impulse response
# pulseTs=np.arange(-num_periods//2,num_periods//2,samp_rate**-1)
csvDF=pd.DataFrame()#({'Ts':pulseTs})
fig, ax = plt.subplots()
for beta in [0,0.5,1]:
    RC_freq_pulse, Ts = IR.RC_freq_domain(symbol_rate,samp_rate,6, beta)
    RCx = pd.DataFrame({'b{}'.format(beta):RC_freq_pulse})
    csvDF=pd.concat([csvDF,RCx],axis=1)
#     plt.plot(RC_freq_pulse, label=beta)
# plt.legend()
# plt.show()
Ts = pd.DataFrame({'Ts':Ts})
csvDF=pd.concat([Ts, csvDF],axis=1)
csvDF.to_csv("freq-domain-RC-impulse-responses.csv", index=False)



# Frequency response
csvDF=pd.DataFrame()
fig,ax=plt.subplots()
for beta in [0,0.5,1]:
    RC_freq_pulse, farr = FR.RC(1,beta)
    RCx = pd.DataFrame({'b{}'.format(beta):RC_freq_pulse})
    csvDF=pd.concat([csvDF,RCx], axis=1)
#     plt.plot(farr, RC_freq_pulse,label=beta)
# plt.legend()
# plt.show()
Fs = pd.DataFrame({"farr":farr})
csvDF = pd.concat([Fs, csvDF],axis=1)
csvDF.to_csv("freq-domain-frequency-responses.csv",index=False)
