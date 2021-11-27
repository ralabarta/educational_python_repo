import numpy as np
x = np.array([2, 4, 2])

r = x.cumprod()

print(r)

sum = 0

for x in range(3, 6):

  sum = sum + x



print(sum)
