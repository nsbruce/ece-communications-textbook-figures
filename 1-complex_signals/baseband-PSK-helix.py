import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import square

fs=100 # sample rate, Hz
fm=1 # message frequency, Hz
t=2 # duration, seconds
fc=0 # carrier frequency, Hz (zero for baseband)

t_arr = np.arange(0,t,fs**-1) # The array of time samples

phi = square(2*np.pi*fm*t_arr) # message
signal = np.exp(1j*phi) * np.exp(1j*-np.pi/4)

x=t_arr
y=np.real(signal)
z=np.imag(signal)

csvDF=pd.DataFrame()
x_pd = pd.DataFrame({'t':x})
y_pd = pd.DataFrame({'real':y})
z_pd = pd.DataFrame({'imag':z})

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.plot(x, y, z)

csvDF=pd.concat([x_pd, y_pd, z_pd], axis=1)
csvDF.to_csv("baseband-PSK-helix.csv", index=False)

plt.show()
