import pandas as pd
data={
    "name":['alice','bob','xavi'],
    "age":[22,None,34],
    "location":["uk","us",None]

}
df=pd.DataFrame(data)
print("original data")
print(df)
missing_data=df.isnull()
print(missing_data)
# to drop the missing data
# drop_df=df.dropna()
# print(drop_df)

# to fill the missing data
filled_missing_data=df.fillna({"age":df['age'].mean(),"location":'unknown'})
print("after filling the missing data")
print(filled_missing_data)