import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fs=500 # sample rate, Hz
fm=1 # message frequency, Hz
t=2 # duration, seconds
fc=20 # carrier frequency, Hz (zero for baseband)

t_arr = np.arange(0,t,fs**-1) # The array of time samples

m_t = np.cos(2*np.pi*fm*t_arr)
k_a = 1
phi = 0
a_t = 1+k_a*m_t

c_t = np.cos(2*np.pi*fc*t_arr)

s_t = a_t*c_t

fig, ax = plt.subplots(3,1, sharex=True, sharey=True)
ax[0].plot(t_arr, m_t)
ax[0].set_title(r'm(t)')
ax[1].plot(t_arr, c_t)
ax[1].set_title(r'c(t)')
ax[2].plot(t_arr, s_t)
ax[2].set_title(r's(t)')
ax[2].set_ylim([-2,2])
ax[2].set_xlim([0,2])

plt.show()

csvDF=pd.DataFrame()

t_pd = pd.DataFrame({'t':t_arr})
m_pd = pd.DataFrame({'m_t':m_t})
c_pd = pd.DataFrame({'c_t':c_t})
s_pd = pd.DataFrame({'s_t':s_t})

csvDF=pd.concat([t_pd, m_pd, c_pd, s_pd], axis=1)
csvDF.to_csv("passband-AM.csv", index=False)

