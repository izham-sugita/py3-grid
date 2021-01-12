import numpy as np
import pandas as pd

df_vert = pd.read_csv("./vert3.csv")

vert = df_vert.to_numpy()

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
            ii = (i*jmax + j)*kmax + k
            xg[i][j][k] = vert[ii][0] #float(i)*1.0
            yg[i][j][k] = vert[ii][1] #float(j)*1.0
            zg[i][j][k] = vert[ii][2] #float(k)*1.0
            
            new_array[index][0] = xg[i][j][k]
            new_array[index][1] = yg[i][j][k]
            new_array[index][2] = zg[i][j][k]

            #print(index,xg[i][j][k], yg[i][j][k], zg[i][j][k])
            index +=1
            
#maximum vertex count
vert_max = index;

new_df = pd.DataFrame(new_array, columns=['x','y','z'])
#print()
#print(vert_max)
#print(new_df)
#new_df.to_csv("./sample.csv", index=False)
#print()

print("Creating connectivity for each surface")

#only for cube surface
imax = 2
jmax = 2
kmax = 2
isurface = 0
ispace = 0
xc = 0.0
yc = 0.0
zc = 0.0
isc = np.ndarray((2,3)) #i=0,1
isvertex = np.ndarray((2,4,3)) #i=0,1
iscen = np.ndarray((2,3)) # 2 surfaces; x-,y-,z-values
for i in [0,imax-1]:
    for j in [0,jmax-1]:
        ii = 0+j
        jj = (jmax-1)-j
        for k in [ii,jj]:
            iii = (i*jmax + j)*kmax + k
            xc += xg[i][j][k]
            yc += yg[i][j][k]
            zc += zg[i][j][k]
            if i == 0:
                print(i,j,k, iii)
                isvertex[i][ispace][0] = xg[i][j][k]
                isvertex[i][ispace][1] = yg[i][j][k]
                isvertex[i][ispace][2] = zg[i][j][k]
                
            else:
                print(i,k,j, iii)
                isvertex[i][ispace][0] = xg[i][k][j]
                isvertex[i][ispace][1] = yg[i][k][j]
                isvertex[i][ispace][2] = zg[i][k][j]

            ispace +=1
            if ispace == 4:
                print()
                ispace = 0
                xc = 0.25*xc
                yc = 0.25*yc
                zc = 0.25*zc
                iscen[i][0] = xc
                iscen[i][1] = yc
                iscen[i][2] = zc
                xc = 0.0
                yc = 0.0
                zc = 0.0


print("Vertex coordinates")
for i in [0,1]:
    print()
    for j in range(4):
        print( isvertex[i][j][:] )

print("Centroid coordinates")
for i in [0,1]:
    print( i, iscen[i][:] )

print()
print("Calculate cross product")
vecsurf = np.ndarray( (4,3) )
vec1 = np.ndarray((3))
vec2 = np.ndarray((3))
nvec = np.ndarray( (6, 3) ) #for 6 surface

isurface = 0
# 4 vertex
for i in range(4):
    vecsurf[i][:] = isvertex[isurface][i][:] - iscen[isurface][:]
    print(i, vecsurf[i][:] )

#normal vector: the orientation is correct; 0->1 is ok
print("Normal vector")
vec1[:] = vecsurf[0][:]
vec2[:] = vecsurf[1][:]
nvec[0][:] = np.cross(vec1,vec2)
print( nvec[0][:] )

surfarea = 0.0
for i in range(4):
    j = (i+1)*np.sign(4-1 - i)
    vec1[:] = vecsurf[i][:]
    vec2[:] = vecsurf[j][:]
    vnorm = np.linalg.norm( np.cross(vec1,vec2) )
    surfarea +=vnorm

surfarea = 0.5*surfarea
print("Surface area : ", surfarea)

print("Program ends.")
