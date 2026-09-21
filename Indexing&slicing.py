import numpy as np
arr=np.array([10,20,30,40,50])
for i in range(0,len(arr)):

    print(arr[i])
#Indexing
print(arr[1:5])
print(arr[::-1])

#Fancy Indeximg
print(arr[[0,2,4]])

#Boolean Masking
print(arr[arr>25])
