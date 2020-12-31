import numpy as np
import pandas as pd


df_vert = pd.read_csv("./vert.csv")

print(df_vert.to_string(index=False))
print()
print(df_vert)

vert = df_vert.to_numpy()

print(vert.shape)

#simpler format
imax = 2
jmax = 2
kmax = 2
xg = np.ndarray((imax,jmax,kmax))
yg = np.ndarray((imax,jmax,kmax))
zg = np.ndarray((imax,jmax,kmax))

new_array = np.ndarray((imax*jmax*kmax, 3) ) #for pandas, 3 is for 3-D

index =0
for i in range(imax):
    for j in range(jmax):
        for k in range(kmax):
            xg[i][j][k] = float(i)*1.0
            yg[i][j][k] = float(j)*1.0
            zg[i][j][k] = float(k)*1.0
            new_array[index][0] = xg[i][j][k]
            new_array[index][1] = yg[i][j][k]
            new_array[index][2] = zg[i][j][k]
            print(index,xg[i][j][k], yg[i][j][k], zg[i][j][k])
            index +=1


#maximum vertex count
vert_max = index;

new_df = pd.DataFrame(new_array, columns=['x','y','z'])
print()
print(vert_max)
print(new_df)
new_df.to_csv("./sample.csv", index=False)
print()

print("Creating connectivity for each surface")

'''
for i in range(imax):
    for j in range(jmax):
        for k in range(kmax):
            ii = (i*jmax + j)*kmax + k
            print(new_array[ii][:])
'''

ispace = 0

#for centroid coordinates
xc = 0.0
yc = 0.0
zc = 0.0
for i in range(imax):
    for j in range(jmax):
        for k in range(kmax):
            ii = (i*jmax + j)*kmax + k
            ispace +=1
            print(ii, xg[i][j][k], yg[i][j][k], zg[i][j][k])
            xc +=xg[i][j][k]
            yc +=yg[i][j][k]
            zc +=zg[i][j][k]
            if ispace == 4: #to create space, calculate centroid
                ispace = 0
                xc = 0.25*xc
                yc = 0.25*yc
                zc = 0.25*zc
                print("Centroid coordinates: %f, %f, %f"%(xc,yc,zc))
                #reset xc,yc,zc
                xc = 0.0
                yc = 0.0
                zc = 0.0
                print()

'''                
print()
ispace = 0
for j in range(jmax):
    for k in range(kmax):
        for i in range(imax):
            ii = (i*jmax + j)*kmax + k
            ispace +=1
            print(ii, xg[i][j][k], yg[i][j][k], zg[i][j][k])
            if ispace == 4: #to create space
                ispace = 0
                print() #reset the spacing
            
print()
ispace = 0
for k in range(kmax):
    for i in range(imax):
        for j in range(jmax):
            ii = (i*jmax + j)*kmax + k
            ispace +=1
            print(ii, xg[i][j][k], yg[i][j][k], zg[i][j][k])
            if ispace == 4: #to reset the count
                ispace = 0
                print()
'''

print("Program ends.")
