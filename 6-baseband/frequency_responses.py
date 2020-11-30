import numpy as np

def RC(T,beta):
    """
    Will only generatre for -1/T to 1/T
    """
    farr = np.linspace(-1/T,1/T,1000)
    
    # 0 handling for ZeroDivisionErrorAvoidance
    zero_idices = np.where(farr==0)
    farr[zero_idices]=10
    if beta==0:
        H = np.where(np.abs(farr) <= (1/(2*T)),T,0)

    else:
        # Course Notes eq.6.6 (eq. no. will probably change)
        # H = np.where(np.abs(farr) <= (1-beta)/(2*T),T,farr)
        # H = np.where((np.abs(farr)>((1-beta)/(2*T))) | (np.abs(farr)<=(1+beta)/(2*T)),(T/2)*(1+np.cos((np.pi*T/beta)*(np.abs(farr)-(1-beta)/(2*T)))),H)
        # H = np.where(np.abs(farr)>(1+beta)/(2*T),0,H)
        H = np.where((np.abs(farr)>((1-beta)/(2*T))) | (np.abs(farr)<=(1+beta)/(2*T)),(T/2)*(1+np.cos((np.pi*T/beta)*(np.abs(farr)-(1-beta)/(2*T)))),farr)
        H = np.where(np.abs(farr) <= (1-beta)/(2*T),T,H)
        H = np.where(np.abs(farr)>(1+beta)/(2*T),0,H)
    
    # I think this is always true
    H[zero_idices]=T

    return H,farr

def RRC(T, beta):
    RC,farr=RC(T,beta)
    RRC = np.sqrt(RC)

    return RRC, farr