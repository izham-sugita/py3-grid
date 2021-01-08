#periodic loop
import numpy as np

#imax=8
#for i in range(imax):
#    j = (i+1)*np.sign(imax-1 -i)
#    print(i,j)

#for i in [0,1]:
#    print(i)

#only for cube surface
print("Counter-clockwise")
node_counter = 0
for i in range(2):
    for j in range(2):
        ii = 0+j
        jj = 1-j
        step = (1-j) - (0+j)
        #print(j, ii, jj, step, np.sign(step))
        #for k in range(ii,jj+step,step):
        for k in [ii,jj]: #a much concise solution
            print(i,j,k)
            node_counter +=1
            if node_counter == 4:
                print()
        
        
print()
print("Usual loop")
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i,j,k)
