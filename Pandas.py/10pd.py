import pandas as pd
s=pd.Series([350,200,800,150],index=["TCS","Reliance","L&T","Wipro"],name="Profits")
print(s.index[s>250])
print(s.name)
