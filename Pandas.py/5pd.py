import pandas as pd
list=[50000,65890,56780,89000,77900]
index=['QTR1','QTR2','QTR3','QTR4','QTR5']
SQTR=pd.Series(list,index=index)
print(SQTR)