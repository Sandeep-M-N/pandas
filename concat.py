import pandas as pd
import numpy as np
df_a=pd.DataFrame({
    "name":["alice","bob","charlie"],
    "score":[23,43,54]
})
df_b=pd.DataFrame({
    "name":["sid","xavi"],
    "score":[34,56,]
})
df_concat=pd.concat([df_a,df_b])
print(df_concat)