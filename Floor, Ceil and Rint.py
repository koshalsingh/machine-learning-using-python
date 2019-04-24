import numpy as np

arr = input().strip().split(' ')
arr=np.array(arr, dtype='float64')
np.set_printoptions(legacy='1.13')
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
