import pandas as pd
import numpy as np

data={
    'A':[12,13,np.nan,14],
    'B':[21,np.nan,np.nan,25],
    'C':[np.nan,32,np.nan,np.nan]
}
df=pd.DataFrame(data)
print("missing data")
print(df)
filled_missing_data=df.fillna(value=0)
print("filling the missing data")
print(filled_missing_data)