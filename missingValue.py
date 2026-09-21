"""
np.isnan()= detect missing value
np.nan_tonum()
np.isinf()=detect infinite value"""

import numpy as np
arr=np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))#jaha nan hoga vaha true print hoha
print(np.nan_to_num(arr,nan=5))# nan ki jagah 5 
