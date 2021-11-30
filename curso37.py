import numpy as np


first = np.array([[0., 0.]])
second = np.array([[2., 2.]])
n = int(input())

data = []

for i in range(n):
   data.append([float(i) for i in input().split()])
  
    
data = np.array(data).reshape((-1,2))


for i in range(n):
   dist1 = np.sqrt(((data[i]-first[0])**2).sum())
 
   dist2 = np.sqrt(((data[i]-second[0])**2).sum())
   
   if (dist1) <= (dist2):
      first = np.vstack((first,data[i]))
       
   else:
      second = np.vstack((second,data[i]))
       
  
     
if first.size > 2:
   mean1 = np.mean(first[1:], axis=0)
   print(np.around(mean1, decimals=2))
else:
   print(None)
      
   
if second.size > 2:
   mean2 = np.mean(second[1:], axis=0)
   print(np.around(mean2, decimals=2))
else:
   print(None)