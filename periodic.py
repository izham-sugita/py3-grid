#periodic loop
import numpy as np

imax=8
for i in range(imax):
    j = (i+1)*np.sign(imax-1 -i)
    print(i,j)
