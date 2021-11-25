import pandas as pd
import matplotlib.pyplot as plt

data = {

    'sport': ["Soccer", "Tennis", "Soccer", "Hockey"],

    'players': [5, 4, 8, 20]

}

df = pd.DataFrame(data)

df.groupby('sport')['players'].sum().plot(kind="pie")
