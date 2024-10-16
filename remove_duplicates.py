import pandas as pd
data={
    "Name":['alice','bob','charlie','alice','bob'],
    "Age":[23,26,27,34,45]
}

df=pd.DataFrame(data)

print(df)
df_no_duplicates=df.drop_duplicates(subset="Name") #removing duplicates based on the columns we specify in the subset
print(df_no_duplicates)

