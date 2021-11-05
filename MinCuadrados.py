import math
import numpy as np
def minicua(x,y):
    sy = sum(y)
    sx = sum(x)
    x2 = sum(x*x)
    y2 = sum(y*y)
    N = x.count()
    xy = sum(x*y)

    m = (N*xy-sx*sy)/(N*x2-sx**2)
    b = (sy*x2-sx*xy)/(N*x2-sx**2)
    r = (N*xy-sx*sy)/(math.sqrt(N*x2-sx**2)*math.sqrt(N*y2-sy**2))
    beta = np.array([0]*N)
    for i in range(N):
        xi = x[i]
        yi = y[i]
        beta[i] = (b+m*xi-yi)**2
    beta2 = sum(beta)
    em = math.sqrt(N/(N*x2-sx**2)*beta2/(N-2))
    eb = math.sqrt(x2/(N*x2)*beta2/(N-2))
    return(m, b, em, eb)