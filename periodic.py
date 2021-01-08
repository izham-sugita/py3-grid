#periodic loop
import numpy as np

#imax=8
#for i in range(imax):
#    j = (i+1)*np.sign(imax-1 -i)
#    print(i,j)


#only for cube surface
for i in range(2):
    for j in range(2):
        ii = 0+j
        jj = 1-j
        step = (1-j) - (0+j)
        #print(j, ii, jj, step, np.sign(step))
        for k in range(ii,jj+step,step):
            print(i,j,k)
        
        
print()
print("Usual loop")
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i,j,k)
