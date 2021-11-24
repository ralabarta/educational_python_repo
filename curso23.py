import pandas as pd

data = {

   'ages': [14, 18, 24, 42],

   'heights': [165, 180, 176, 184]

}
df=pd.DataFrame(data)
print (df)


x = {

'a': [1, 2],

'b': [3, 4],

'c': [5, 6]

}

df = pd.DataFrame(x)

print(df)
