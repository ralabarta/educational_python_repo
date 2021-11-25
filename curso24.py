import pandas as pd
data = {

    'height': [133, 120, 180, 100],

    'age': [9, 7, 16, 4]

}

df = pd.DataFrame(data)

print(df['age'].mean())


data = {

    'a': [1, 2, 3],

    'b': [5, 8, 4]

}

df = pd.DataFrame(data)

df['c'] = df['a']+df['b']

print(df.iloc[2]['c'])
