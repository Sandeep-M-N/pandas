import pandas as pd
import numpy as np
data={
    "name":['alice','bob','can'],
    "math":[56,78,90],
    "evs":[23,45,67]
}
df=pd.DataFrame(data)
print("original data")
print(df)
melted_data=pd.melt(df,id_vars="name",value_vars=['math','evs'],var_name="subject",value_name='score')
print('after being reshaped that is melt')
print(melted_data)