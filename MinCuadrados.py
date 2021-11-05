import math
import numpy as np
import pandas as pd
file = pd.read_csv('/home/dantron/Desktop/datoslentes.csv')
x = file['S']
y = file['S1']
sy = sum(y)
sx = sum(x)
x2 = sum(x*x)
y2 = sum(y*y)
N = x.count()
xy = sum(x*y)

m = (N*xy-sx*sy)/(N*x2-sx**2)
b = (sy*x2-sx*xy)/(N*x2-sx**2)
r = (N*xy-sx*sy)/(math.sqrt(N*x2-sx**2)*math.sqrt(N*y2-sy**2))

print(r)