import pandas as pd
import numpy as np


df = pd.DataFrame(columns=['S'])
df['S'] = df['S'].astype(object)
df.loc[1].at['S'] = np.array([5, 6, 7, 8])
print(df)