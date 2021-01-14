import numpy as np
import pandas as pd

df_vert = pd.read_csv("./vert2.csv") #test volume, V = 0.58333
#df_vert = pd.read_csv("./vert3.csv")

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
            xg[i][j][k] = vert[ii][0] 
            yg[i][j][k] = vert[ii][1] 
            zg[i][j][k] = vert[ii][2] 
            
            new_array[index][0] = xg[i][j][k]
            new_array[index][1] = yg[i][j][k]
            new_array[index][2] = zg[i][j][k]

            index +=1
            
#maximum vertex count
vert_max = index;

new_df = pd.DataFrame(new_array, columns=['x','y','z'])


print("Creating connectivity for each surface")

#only for cube surface
imax = 2
jmax = 2
kmax = 2
isurface = 0 #use for surface counts
ispace = 0
xc = 0.0
yc = 0.0
zc = 0.0

isc = np.ndarray((2,3)) #i=0,1
isvertex = np.ndarray((2,4,3)) #i=0,1
iscen = np.ndarray((2,3)) # 2 surfaces; x-,y-,z-values

#vertex 2-surface for each i, 4 nodes-each-surface, 3-xyz value
vertex = np.ndarray((2,4,3) )

plane = np.ndarray((6,4,3))
centroid = np.ndarray((6,3))
normal = np.ndarray((6,3))
area = np.ndarray((6))

vec1 = np.ndarray((3))
vec2 = np.ndarray((3))

sid = 0

# i in [0,1] range
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
                vertex[i][ispace][0] = xg[i][j][k]
                vertex[i][ispace][1] = yg[i][j][k]
                vertex[i][ispace][2] = zg[i][j][k]
                                
            else:
                print(i,k,j, iii)
                                
                vertex[i][ispace][0] = xg[i][k][j]
                vertex[i][ispace][1] = yg[i][k][j]
                vertex[i][ispace][2] = zg[i][k][j]
                
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
                
                vec1[:] = vertex[i][0][:] - iscen[i][:]
                vec2[:] = vertex[i][1][:] - iscen[i][:]
                
                plane[sid][:][:] = vertex[i][:][:]
                centroid[sid][:] = iscen[i][:]
                normal[sid][:] = np.cross(vec1, vec2)
                
                surfarea = 0.0
                for iv in range(4):
                    jv = (iv+1)*np.sign(4-1-iv)
                    vec1[:] = vertex[i][iv][:] - iscen[i][:]
                    vec2[:] = vertex[i][jv][:] - iscen[i][:]
                    vnorm = np.linalg.norm( np.cross(vec1,vec2) )
                    surfarea +=vnorm

                surfarea = 0.5*surfarea
                area[sid] = surfarea
                print("Surface area: ", surfarea)
                print()
                                
                sid +=1
                xc = 0.0
                yc = 0.0
                zc = 0.0


#surface j in [0,1]
for j in [0,jmax-1]:
    for k in [0,kmax-1]:
        ii = 0+k
        jj = (kmax-1)-k
        for i in [ii,jj]:
            iii = (i*jmax + j)*kmax + k
            xc += xg[i][j][k]
            yc += yg[i][j][k]
            zc += zg[i][j][k]
            if j == 0:
                print(i,j,k, iii)
                vertex[j][ispace][0] = xg[i][j][k]
                vertex[j][ispace][1] = yg[i][j][k]
                vertex[j][ispace][2] = zg[i][j][k]
                                
            else:
                print(k,j,i, iii)
                                
                vertex[j][ispace][0] = xg[k][j][i]
                vertex[j][ispace][1] = yg[k][j][i]
                vertex[j][ispace][2] = zg[k][j][i]
                
            ispace +=1
            if ispace == 4:
                print()
                ispace = 0
                xc = 0.25*xc
                yc = 0.25*yc
                zc = 0.25*zc
                iscen[j][0] = xc
                iscen[j][1] = yc
                iscen[j][2] = zc
                
                vec1[:] = vertex[j][0][:] - iscen[j][:]
                vec2[:] = vertex[j][1][:] - iscen[j][:]
                
                plane[sid][:][:] = vertex[j][:][:]
                centroid[sid][:] = iscen[j][:]
                normal[sid][:] = np.cross(vec1, vec2)

                surfarea = 0.0
                for iv in range(4):
                    jv = (iv+1)*np.sign(4-1-iv)
                    vec1[:] = vertex[j][iv][:] - iscen[j][:]
                    vec2[:] = vertex[j][jv][:] - iscen[j][:]
                    vnorm = np.linalg.norm( np.cross(vec1,vec2) )
                    surfarea +=vnorm

                surfarea = 0.5*surfarea
                area[sid] = surfarea
                print("Surface area: ", surfarea)
                print()
                
                sid +=1
                xc = 0.0
                yc = 0.0
                zc = 0.0

#surface k in [0,1]
for k in [0,kmax-1]:
    for i in [0,imax-1]:
        ii = 0+i
        jj = (imax-1)-i
        for j in [ii,jj]:
            iii = (i*jmax + j)*kmax + k
            xc += xg[i][j][k]
            yc += yg[i][j][k]
            zc += zg[i][j][k]
            if k == 0:
                print(i,j,k, iii)
                vertex[k][ispace][0] = xg[i][j][k]
                vertex[k][ispace][1] = yg[i][j][k]
                vertex[k][ispace][2] = zg[i][j][k]
                                
            else:
                print(j,i,k, iii)
                                
                vertex[k][ispace][0] = xg[j][i][k]
                vertex[k][ispace][1] = yg[j][i][k]
                vertex[k][ispace][2] = zg[j][i][k]
                
            ispace +=1
            if ispace == 4:
                print()
                ispace = 0
                xc = 0.25*xc
                yc = 0.25*yc
                zc = 0.25*zc
                iscen[k][0] = xc
                iscen[k][1] = yc
                iscen[k][2] = zc
                
                vec1[:] = vertex[k][0][:] - iscen[k][:]
                vec2[:] = vertex[k][1][:] - iscen[k][:]
                
                plane[sid][:][:] = vertex[k][:][:]
                centroid[sid][:] = iscen[k][:]
                normal[sid][:] = np.cross(vec1, vec2)

                surfarea = 0.0
                for iv in range(4):
                    jv = (iv+1)*np.sign(4-1-iv)
                    vec1[:] = vertex[k][iv][:] - iscen[k][:]
                    vec2[:] = vertex[k][jv][:] - iscen[k][:]
                    vnorm = np.linalg.norm( np.cross(vec1,vec2) )
                    surfarea +=vnorm

                surfarea = 0.5*surfarea
                area[sid] = surfarea
                print("Surface area: ", surfarea)
                print()
                
                sid +=1
                xc = 0.0
                yc = 0.0
                zc = 0.0


print(sid)


print("Centroids:")

#print(centroid[4][:])
#print(centroid[5][:])
#print("Normals")
#print(normal[4][:])
#print(normal[5][:])

#normal vector convert to unit vector
for i in range(sid):
    vec1[:] = normal[i][:]
    vnorm = np.linalg.norm(vec1)
    normal[i][:] = normal[i][:] / vnorm

print("Centroid for all surfaces")
for i in range(sid):
	print(i, centroid[i][:])

print("Normal for all surfaces")
for i in range(sid):
	print(i, normal[i][:], area[i])


#Gauss divergence theorem for volume
volume = 0.0
for i in range(sid):
    vec1[:] = normal[i][:]
    vec2[:] = centroid[i][:]
    dotproduct = np.dot(vec1, vec2)
    volume += dotproduct * area[i]

volume = volume/3.0
print("Volume of the voxel is: ", volume)

print("Program ends.")
