#total number of element after reshaping is same

import numpy as np
arr=np.array([1,2,3,4,5,6])
reshaped_arr=arr.reshape(3,2)
reshapedarr=arr.reshape(2,3)
print(reshaped_arr)
print(reshapedarr)
