import pandas as pd
data={
    "name":['alice','bob','gavi','xavi'],
    "age":[22,23,24,25],
    "salary":[22000,45000,35000,60000]
}
df=pd.DataFrame(data)
print(df)
#filtering specific data
print("filtering age greater than 23")
print(df[df['age']>23])
#sorting the data
sorted_data=df.sort_values(by='age',ascending=False)
print("sorting based on the age in descending order")
print(sorted_data)
#grouping the data
df["department"]=['hr','finance','finance','hr']
grouped_data=df.groupby("department")['salary'].mean()
print(grouped_data)