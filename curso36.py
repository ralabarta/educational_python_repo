y_true = [int(x) for x in input().split()]
y_pred =  [int(x) for x in input().split()]

import numpy as np

y_true=np.array(y_true )
y_true= y_true.astype(str)  
y_pred=np.array(y_pred )
y_pred=y_pred.astype(str) 
#y_true = y_true.reshape(-1, 1)
#y_pred = y_pred.reshape(-1, 1)
#print(y_true.shape)

from sklearn.metrics import confusion_matrix

print((confusion_matrix(y_pred, y_true, labels=['1', '0']))/1)