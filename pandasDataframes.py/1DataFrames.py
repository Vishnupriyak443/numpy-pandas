import pandas as pd
import numpy as np
print("List:")
ls=[100,200,300]
df=pd.DataFrame(ls,columns=['ID'],index=[x for x in 'abc'])
print(df)
#Empty dataframe
d2=pd.DataFrame()
print(d2)
print("Dictionary")
dict={'ID':[100,200,300],'Dept':['Sales','Production','HR'],'Salary':[20500,28000,39000]}
d3=pd.DataFrame(dict)
print(d3)
print("array:")
arr=np.array([[10,'A'],[20,'B'],[30,'C']])
d4=pd.DataFrame(arr,columns=['no','str'])
print(d4)
print("Series")
s=pd.Series([100,200,300,400])
d5=pd.DataFrame(s)
print(d5)
print("list of dictionaries")
l=[{'ID':100,'DEPT':'Sales'},{'ID':200,'DEPT':'HR'},{'ID':300,'DEPT':'PROD'}]
d6=pd.DataFrame(l,index=[x for x in 'abc'])
print(d6)
print("Dictionary of series:")
d={ 'A':pd.Series([10,20,30]),
    'B':pd.Series([100,200,300,400,500]) }
d7=pd.DataFrame(d)
print(d7)

print()
print("Working with columns:")
df=pd.DataFrame({'a':[10,20,30,40],
                 'b':[1,2,0,4],
                 'c':[0,1,2,3]})
print(df.columns)
print(df.columns[1])
print(df.columns.tolist())
df.rename(columns={'b':'B'},inplace=True) #changing column name
print(df)
df=df.rename(columns={'B':'b'})
df['d']=[2,4,1,5]#Adding new column
print(df)
df['d']=range(len(df))
print(df)
df['d']=np.repeat(np.nan,len(df))
print(df)
df['e']=np.random.rand(len(df))
print(df)
df['d']=df['b']+df['c']
print(df)
f=pd.DataFrame({'f':[0,2,1,3]})
df=pd.concat([df,f],axis=1)
print(f)
print(df)
df[['d','e']]=df[['a','e']]
print(df)
print(df.drop('e',axis=1)) #Deleting columns
df=df.drop(['d','f'],axis=1)
print(df)
#del df['a']
#print(df.loc[:,df.columns!='b']) #Except b
d_iloc=df.iloc[:,[0,2,1]] #Selecting 0 and 2 and 1
print(d_iloc)
print(df)
#df.drop(df.columns['a'],inplace=True)
#print(df)
#df.loc[df['a']>1,'a']=999
#print(df)
df.loc[df['b']>1,'c']=999
print(df)
df['c']=np.where(df['b']>1,df['a'],999)
print(df)
df['f']=df['a'].where(df['b']>0,other=0) #Creating new column
print(df)
df['g']=np.where(df['b']>0,df['a'],df['c'])
print("COMPLEX COND:",df)
print(df.at[0,'a'])#Row-idx and column index to get an element
print(df.iat[3,3])
print(df.get('a'))
print("CONDITION:",df.loc[df['b']>1,'b'])   #Condition on columns
#print(df.at[df['f']>20,'f'])
print(df.loc[(df['a']>10)&(df['f']>10),'b'])    #Complex Condition
##########################
print(df)
print(df['e'].dtype)
print(df['a'].size)
print(df['b'].count())
sum=df['b'].sum()
print(sum)
print(df['e'].prod())
print(df['e'].min())
print(df['c'].max())
print(df['f'].mean())
print(df['b'].median())
print(df['a'].cov(df['f']))
print(df['b'].describe())
print(df['c'].value_counts()) #Count of an element
print(df['a'].idxmin())
print(df['c'].idxmax())
#Maximum velues more than 1 then 1st element will be printed
print(df['b'].isnull())
print(df['e'].notnull())
print(df['a'].astype(str))#astype-convert elements into another data type
print(df['e'].round(decimals=0))
print("diff:",df['b'].diff(periods=3))  # prints diff bw ele and 3th previous 
print("shift:",df['f'].shift(periods=2))  #Replace with 2th previous element
#print(df['b'].to_datetime())
print(df['c'].fillna(10))
print(df['b'].cumsum())
print(df['f'].cumprod())
print(df['a'].pct_change(periods=2))
print(df['a'].rolling(window=2).sum()) #sum of 2 values (1 previous value)
