import numpy as np

def compute_r_squared(data, predictions):


    r_squared  = 1 - np.square(data - predictions).sum()/np.square(data - np.mean(data)).sum()

    return r_squared