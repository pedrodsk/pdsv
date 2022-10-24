import numpy as np 
from numpy import cumsum, log, polyfit, sqrt, std, subtract

####################################################
# ARQUIVO DE FUNÇÕES #
####################################################

#---------------------------------------------------
# FUNÇÃO energia
#---------------------------------------------------
def energia(x):
    "" 'Calcula a energia de um sinal'
    ""
    a=x**2
    e=np.sum(a)
    edB=10*np.log10(e)
    return e, edB

#---------------------------------------------------
# FUNÇÃO TCZ
#---------------------------------------------------
def ZCR(x):
    x=np.array(x)
    county=np.sum(np.abs(np.diff(x>0)))
    y=county/len(x)
    return y, county

#---------------------------------------------------
# FUNÇÃO expoente de Hurst
#---------------------------------------------------
def hurst(ts):
    """Returns the Hurst Exponent of the time series vector ts"""
    # Create the range of lag values
    lags = range(2, 100)

    # Calculate the array of the variances of the lagged differences
    tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]

    # Use a linear fit to estimate the Hurst Exponent
    poly = polyfit(log(lags), log(tau), 1)

    # Return the Hurst exponent from the polyfit output
    return poly[0]*2.0