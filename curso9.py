import numpy as np

x = np.arange(2, 8, 2)

x = np.append(x, x.size)

x = np.sort(x)

print(x[1])
