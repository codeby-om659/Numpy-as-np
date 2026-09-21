#array have fixed size ,to apka insert karna hai to ,new array banan hoga
#np.insert(array,index,value,axis=)
#axis=o for row,axis=1 for column
import numpy as np
arr=np.array([10,20,30,40,50,60])
new_arr=np.insert(arr,2,80,axis=0)
print(new_arr)

arr_2d=np.array([[1,2,3],
                 [4,5,6]])
new_ar=np.insert(arr_2d,1,[5,6],axis=1)
print(new_ar)
