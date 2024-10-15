import pandas as pd
data={
    "name":['albert','frank','vihar'],
    "age":[22,23,24],
    "location":['London','ramapuram','mumbai']
}
df=pd.DataFrame(data)
print("before adding data frame :")
print(df)
print("after adding data frame :")
df.loc[len(df)]=['david',25,'sydney']
print(df)
# removing the data from the set
df=df[df['name']!="albert"]
print("after removing charlie")
print(df)
#updating the data set
df.loc[df['name']=="frank",['name','age']]=["sandeep",30]
print("updating the frank name")
print(df)