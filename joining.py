import pandas as pd
import numpy as np
df_left=pd.DataFrame({
    'name':['alice','bob','charlie'],
    'age':[22,32,43]
},index=[1,2,3])
df_right=pd.DataFrame({
    'salary':[22000,34000,56000]
},index=[1,2,4])
joined_data=df_left.join(df_right,how='inner')#this is joining 2 data using inner join
print(joined_data)