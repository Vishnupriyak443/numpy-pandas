#create series 1 and double the series1 then store in series2
import pandas as pd
series1=pd.Series([100,200,300,400,500],index=['A','B','C','D','E'])
series2=series1*2
print(series2)
