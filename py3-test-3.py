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

            print(index,xg[i][j][k], yg[i][j][k], zg[i][j][k])
            index +=1
            
#maximum vertex count
vert_max = index;

new_df = pd.DataFrame(new_array, columns=['x','y','z'])
#print()
#print(vert_max)
#print(new_df)
new_df.to_csv("./sample.csv", index=False)
#print()

print("Creating connectivity for each surface")

#only for cube surface
imax = 2
jmax = 2
kmax = 2
for i in range(imax):
    for j in range(jmax):
        ii = 0+j
        jj = (jmax-1)-j
        step = (1-j) - (0+j)
        for k in range(ii,jj+step,step):
            print(i,j,k)


ispace = 0
xscen = np.ndarray((2,3)) # 2 surfaces; x-,y-,z-values
yscen = np.ndarray((2,3))
zscen = np.ndarray((2,3)) 

#for centroid coordinates
xc = 0.0
yc = 0.0
zc = 0.0
isurface = 0
ispace = 0
x_vertex = np.ndarray((2,4,3))
print("New indexing technique")
#only for cube surface
for i in range(imax):
    for j in range(jmax):
        ii = 0+j
        jj = (jmax-1)-j
        #produce clock-wise orientation
        for k in [ii,jj]:
            iii = (i*jmax + j)*kmax + k
            #print(i,j,k, ii)
            xc +=xg[i][j][k]
            yc +=yg[i][j][k]
            zc +=zg[i][j][k]
            x_vertex[isurface][ispace][0] = xg[i][j][k]
            x_vertex[isurface][ispace][1] = yg[i][j][k]
            x_vertex[isurface][ispace][2] = zg[i][j][k]
            ispace +=1
            if ispace == 4: #to create space, calculate centroid
                ispace = 0
                xc = 0.25*xc
                yc = 0.25*yc
                zc = 0.25*zc
                print("Centroid coordinates: %f, %f, %f"%(xc,yc,zc))
                xscen[isurface][0] = xc
                xscen[isurface][1] = yc
                xscen[isurface][2] = zc
                #reset xc,yc,zc
                xc = 0.0
                yc = 0.0
                zc = 0.0
                print(isurface, xscen[isurface][:])
                isurface +=1
                print()
                
#calculate cross product
#xscen: centroid
#x_vertex: vertex
#isurface: surface index
isurface = 0
#x_vertex[isurface][ispace][:]
vec_surf = np.ndarray((4,3))
vec1 = np.ndarray((3))
vec2 = np.ndarray((3))
for i in range(4):
    vec_surf[i][:] = x_vertex[isurface][i][:] - xscen[isurface][:]
    print(i, vec_surf[i][:])
    
#calculate cross product on surface
print("Cross product and surface area")
surface_area = 0.0
for i in range(4):
    j = (i+1)*np.sign(4-1 -i)
    vec1[:] = vec_surf[i][:]
    vec2[:] = vec_surf[j][:]
    print(i,j,np.cross(vec1,vec2), vec1,vec2)
    vec_norm = np.linalg.norm(np.cross(vec1,vec2))
    surface_area +=vec_norm;


surface_area = 0.5*surface_area
print("Surface area: ", surface_area)
print("Indexing succeed!")
#print("Checking cross product")
#vec1[:] = vec_surf[1][:]
#vec2[:] = vec_surf[2][:]
#print( np.cross(vec1,vec2) )


print()
ispace = 0
isurface = 0
xc = 0.0
yc = 0.0
zc = 0.0
for j in range(jmax):
    for k in range(kmax):
        ii = 0+k
        jj = (kmax-1)-k
        step = (1-k) - (0+k)
        for i in range(ii,jj+step, step):
            iii = (i*jmax + j)*kmax + k
            ispace +=1
            xc +=xg[i][j][k]
            yc +=yg[i][j][k]
            zc +=zg[i][j][k]
            print(iii, xg[i][j][k], yg[i][j][k], zg[i][j][k])
            if ispace == 4: #to create space
                ispace = 0
                xc = 0.25*xc
                yc = 0.25*yc
                zc = 0.25*zc
                print("Centroid coordinates: %f, %f, %f"%(xc,yc,zc))
                yscen[isurface][0] = xc
                yscen[isurface][1] = yc
                yscen[isurface][2] = zc
                #reset xc,yc,zc
                xc = 0.0
                yc = 0.0
                zc = 0.0
                #print(isurface, yscen[isurface][:])
                isurface +=1
                #print() #reset the spacing
            
print()
ispace = 0
isurface = 0
xc = 0.0
yc = 0.0
zc = 0.0
for k in range(kmax):
    for i in range(imax):
        for j in range(jmax):
            ii = (i*jmax + j)*kmax + k
            ispace +=1
            xc +=xg[i][j][k]
            yc +=yg[i][j][k]
            zc +=zg[i][j][k]
            if ispace == 4: #to reset the count
                ispace = 0
                xc = 0.25*xc
                yc = 0.25*yc
                zc = 0.25*zc
                #print("Centroid coordinates: %f, %f, %f"%(xc,yc,zc))
                zscen[isurface][0] = xc
                zscen[isurface][1] = yc
                zscen[isurface][2] = zc
                #reset xc,yc,zc
                xc = 0.0
                yc = 0.0
                zc = 0.0
                #print(isurface, zscen[isurface][:])
                isurface +=1
                print()



print("Program ends.")
