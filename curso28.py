import numpy as np
import numpy_financial as npf

#price for 2018-2021
bitcoin = [3869.47, 7188.46, 22203.31, 29391.78]
print(np.std(bitcoin))


res = npf.fv(rate=1, nper=1, pmt=0, pv=-100)

print(res)

cf = [-1, 1]

print(npf.irr(cf))

print(npf.fv(rate=0, nper=3, pmt=0, pv=-100))
