import numpy as np
import impulse_responses as IR
import frequency_responses as FR
import matplotlib.pyplot as plt
import pandas as pd

# First set simulation frequencies and other parameters
samp_rate = 100
symbol_rate = 1 
num_periods = 6 # from -3T to 3T
beta=0

# Impulse responses
RC=IR.RC_freq_domain(symbol_rate,samp_rate,num_periods,beta)

# Impulse response
csvDF=pd.DataFrame()
fig, ax = plt.subplots()
for beta in [0,0.5,1]:
    RC, Ts = IR.RC_freq_domain(symbol_rate, samp_rate, num_periods, beta)
    RRC, _ = IR.RRC_freq_domain(symbol_rate, samp_rate, num_periods, beta)
    RCx = pd.DataFrame({'RCb{}'.format(beta):RC})
    RRCx = pd.DataFrame({'RRCb{}'.format(beta):RRC})
    csvDF=pd.concat([csvDF,RCx,RRCx],axis=1)
    plt.plot(Ts,RRC, label=beta)
plt.legend()
plt.show()
Ts = pd.DataFrame({'Ts':Ts})
csvDF=pd.concat([Ts, csvDF],axis=1)
csvDF.to_csv("RC-and-RRC-impulse-responses.csv", index=False)



# Frequency response
# The frequency response is not as exciting to compare. Especially in the beta=0 case 
# where RC is a "box" of magnitude T while RRC is a "box" of magnitude sqrt(T)