import numpy as np
import pandas as pd

df_vert = pd.read_csv("./vert3.csv")

#print(df_vert.to_string(index=False))
#print()
#print(df_vert)

vert = df_vert.to_numpy()

#print(vert.shape)
#print(vert[0][:])
#print()

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


#modify xg-coordinate at z=0 surface
#xg[0][0][0] = 0.25
#xg[1][0][0] = 0.75
#xg[0][1][0] = 0.25
#xg[1][1][0] = 0.75
            
#maximum vertex count
vert_max = index;

new_df = pd.DataFrame(new_array, columns=['x','y','z'])
#print()
#print(vert_max)
#print(new_df)
new_df.to_csv("./sample.csv", index=False)
#print()

print("Creating connectivity for each surface")

ispace = 0

xscen = np.ndarray((2,3)) # 2 surfaces; x-,y-,z-values
yscen = np.ndarray((2,3))
zscen = np.ndarray((2,3)) 

#for centroid coordinates
xc = 0.0
yc = 0.0
zc = 0.0
isurface = 0

x_vertex = np.ndarray((2,4,3))

#focus on i-index; xi-axis
print("xi-axis surface")
for i in range(imax):
    for j in range(jmax):
        for k in range(kmax):
            ii = (i*jmax + j)*kmax + k
            print(ii, xg[i][j][k], yg[i][j][k], zg[i][j][k])
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

#
    
#calculate cross product on surface
print("Cross product and surface area")
surface_area = 0.0
'''
for i in range(4):
    j = (i+1)*np.sign(4-1 -i)
    vec1[:] = vec_surf[i][:]
    vec2[:] = vec_surf[j][:]
    print(i,j,np.cross(vec1,vec2), vec1,vec2)
    vec_norm = np.linalg.norm(np.cross(vec1,vec2))
    surface_area +=vec_norm;
'''

surface_area = 0.5*surface_area
print("Surface area: ", surface_area)

print("Checking cross product")
vec1[:] = vec_surf[1][:]
vec2[:] = vec_surf[2][:]
print( np.cross(vec1,vec2) )

print()
ispace = 0
isurface = 0
xc = 0.0
yc = 0.0
zc = 0.0
for j in range(jmax):
    for k in range(kmax):
        for i in range(imax):
            ii = (i*jmax + j)*kmax + k
            ispace +=1
            xc +=xg[i][j][k]
            yc +=yg[i][j][k]
            zc +=zg[i][j][k]
            print(ii, xg[i][j][k], yg[i][j][k], zg[i][j][k])
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
                print(isurface, yscen[isurface][:])
                isurface +=1
                print() #reset the spacing
            
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
            print(ii, xg[i][j][k], yg[i][j][k], zg[i][j][k])
            if ispace == 4: #to reset the count
                ispace = 0
                xc = 0.25*xc
                yc = 0.25*yc
                zc = 0.25*zc
                print("Centroid coordinates: %f, %f, %f"%(xc,yc,zc))
                zscen[isurface][0] = xc
                zscen[isurface][1] = yc
                zscen[isurface][2] = zc
                #reset xc,yc,zc
                xc = 0.0
                yc = 0.0
                zc = 0.0
                print(isurface, zscen[isurface][:])
                isurface +=1
                print()


print("Calculating metrics from centroid location")

d_xi = np.ndarray((3))
d_eta = np.ndarray((3))
d_theta = np.ndarray((3))

d_xi[:] = xscen[1][:] - xscen[0][:]
d_eta[:] = yscen[1][:] - yscen[0][:]
d_theta[:] = zscen[1][:] - zscen[0][:]

print(d_xi)
print(d_eta)
print(d_theta)


Jmatrix = np.array([d_xi,d_eta,d_theta])

Jtrans = Jmatrix.transpose()
print(Jtrans)

det = np.linalg.det(Jtrans)
print(det)


print()
print("Caculating metrics")

ii = 1; jj = 1; kk = 1;
i = 0; j = 0; k = 0;

x_xi = xg[ii][j][k] - xg[i][j][k]
x_eta = xg[i][jj][k] - xg[i][j][k]
x_theta = xg[i][j][kk] - xg[i][j][k]

y_xi = yg[ii][j][k] - yg[i][j][k]
y_eta = yg[i][jj][k] - yg[i][j][k]
y_theta = yg[i][j][kk] - yg[i][j][k]

z_xi = zg[ii][j][k] - zg[i][j][k]
z_eta = zg[i][jj][k] - zg[i][j][k]
z_theta = zg[i][j][kk] - zg[i][j][k]

#Jacobian
J = x_xi*y_eta*z_theta + \
    x_eta*y_theta*z_xi + \
    x_theta*y_xi*z_eta

J = J - \
    ( x_theta*y_eta*z_xi + x_eta*y_xi*z_theta + x_xi*y_theta*z_eta )

print("Jacobian, J = ", J)


print("Program ends.")
