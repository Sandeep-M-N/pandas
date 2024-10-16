import pandas as pd
import numpy as np
data={
    "value":[50,100,200,300,1000]
}
df=pd.DataFrame(data)
print("original data")
print(df)
#log transformation
# df["log_value"]=np.log(df['value'])
# print("value and log value")
# print(df)

#normalization with max and min value
df["normalization"]=np.log(df['value']-df["value"].min())/(df["value"]-df["value"].max())-df["value"].min()
print("after normalization")
print(df)