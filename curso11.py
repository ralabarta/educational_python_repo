import numpy as np
x = np.arange(1, 8, 3)

z = x.reshape(3, 1)

print(z[1][0])
