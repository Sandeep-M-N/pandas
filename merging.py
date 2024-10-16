import pandas as pd 
import numpy as np
data1={
    "ID":[1,2,3],
    "Name":['alice','bob','charlie']
}
data2={
    "ID":[1,2,4],
    "Score":[45,56,78]
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
merged_data=pd.merge(df1,df2,on="ID")
print(merged_data)