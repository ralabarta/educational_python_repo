import numpy as np
r = int(input()) 
lst = [float(x) for x in input().split()]

arr_ABD = np.array(lst)
arr_ABD = arr_ABD.reshape(r,int(len(lst)/r))
print(arr_ABD.round(2))