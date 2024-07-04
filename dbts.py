import pandas as pd
import numpy as np

df=pd.DataFrame({'a':[10,20,30,40],
                 'b':[1,np.nan,0,4],
                 'c':[9,1,2,3]})

#print(df['c'].to_timestamp(freq='y'))
df['d']=range(0,7,2)
print(df)
df.at()
print(df)

