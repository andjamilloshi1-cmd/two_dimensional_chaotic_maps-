import numpy as np
def standard_map(x, p, K=0.9):
    # Logjika e Standard Map
    p_new = p + K * np.sin(x)
    x_new = x + p_new
    return x_new % (2 * np.pi), p_new
