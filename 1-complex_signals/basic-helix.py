import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fs=100 #Hz
fc=1 #Hz
t=2 # duration, seconds
phi = 0 # Phase, radians

t_arr = np.arange(0,t,fs**-1) # The array of time samples

basic_exp = np.exp(1j*(2*np.pi*fc*t_arr+phi))

x=t_arr
y=np.real(basic_exp)
z=np.imag(basic_exp)

csvDF=pd.DataFrame()
x_pd = pd.DataFrame({'t':x})
y_pd = pd.DataFrame({'real':y})
z_pd = pd.DataFrame({'imag':z})

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.plot(x, y, z)

csvDF=pd.concat([x_pd, y_pd, z_pd], axis=1)
csvDF.to_csv("basic-helix.csv", index=False)

plt.show()
