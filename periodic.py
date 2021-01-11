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
#only for cube surface
print("Clockwise")
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


#only for cube surface
print("Voxel specific indexing")
print("Counter-clockwise and clockwise")
print("Surface i=0 and 1")
node_counter = 0
for i in [0,1]:
    for j in [0,1]:
        ii = 0+j
        jj = 1-j
        for k in [ii,jj]: #a much concise solution
            if i ==0:
                print(i,j,k)
            else:
                print(i,k,j)
            node_counter +=1
            if node_counter == 4:
                print()

node_counter=0
print("Surface j=0 and 1")
for j in [0,1]:
    for k in [0,1]:
        ii = 0+k
        jj = 1-k
        for i in [ii,jj]:
            if j == 0:
                print(i,j,k)
            else:
                print(k,j,i)

            node_counter +=1
            if node_counter == 4:
                print()


node_counter=0
print("Surface k=0 and 1")
for k in [0,1]:
    for i in [0,1]:
        ii = 0+i
        jj = 1-i
        for j in [ii,jj]:
            if k == 0:
                print(i,j,k)
            else:
                print(j,i,k)

            node_counter +=1
            if node_counter == 4:
                print()
            
