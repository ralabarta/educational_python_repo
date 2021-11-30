import numpy as np
n, p = [int(x) for x in input().split()]

X = np.empty([n, p])
for i in range(n):
    X[i,] = input().split()


y = [float(x) for x in input().split()]

Xarr = np.array(X)
yarr = np.array([y]).T

temp1 = np.linalg.inv(np.matmul(Xarr.T, Xarr))
temp2 = np.matmul(temp1, Xarr.T)
beta = np.matmul(temp2, yarr)
print(beta.flatten().round(2))