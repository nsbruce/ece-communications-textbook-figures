import numpy as np
from scipy import signal

#RC2 time domain
def RC2_time_domain(fsym, fs):
    t = np.arange(0,2/fsym,1/fs)
    h = 0.5*(1-np.cos(np.pi*t*fsym))
    return h, t

#RC frequency domain
def RC_freq_domain(fsym, fs, num_periods, beta):
    t=np.arange(-num_periods//2, num_periods//2, 1/fs)
    h = np.sinc(t*fsym)*np.cos(np.pi*beta*t*fsym)/(1-np.power(2*beta*t*fsym,2))
    return h, t

#RRC in the frequency domain
def RRC_freq_domain(fsym, fs, num_periods, beta):
    t=np.arange(-num_periods//2,num_periods//2,1/fs)

    # This is the "otherwise" case. Do it first then overwrite with the specific cases
    h = (np.sqrt(fsym**-1)**-1)*(np.sin(np.pi*t*fsym*(1-beta))+4*beta*t*fsym*np.cos(np.pi*t*fsym*(1+beta)))/(np.pi*t*fsym*(1-(4*beta*t*fsym)**2))
    h = np.where(t==0,(np.sqrt(fsym**-1)**-1)*(1-beta+(4*beta)/np.pi),h)
    if beta != 0:
        h = np.where(t==np.abs((fsym*4*beta)**-1), (beta/np.sqrt(2*fsym**-1))*( (1+(2/np.pi))*np.sin(np.pi/(4*beta))+(1-(2/np.pi))*np.cos(np.pi/(4*beta)) ),h)
    return h, t
