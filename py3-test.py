import numpy as np
import pandas as pd
import csv

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


new_df = pd.DataFrame(new_array, columns=['x','y','z'])
print()
print(new_df)
new_df.to_csv("./sample.csv", index=False)
