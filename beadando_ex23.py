import numpy as np
v=[1,2,3,4,5]
veg=0
i_index=0
for i in v:
    d=0
    j_index=0
    for j in v:
        j_index+=1
        if j>i and j_index>i_index:

            d+=1
    i_index+=1
    veg+=d
veg=veg%(10**9+7)
print(veg)
