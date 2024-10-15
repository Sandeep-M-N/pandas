import pandas as pd
data={
    # 'Date':['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-05'],
    'Date':pd.date_range(start='2024-01-01',periods=5,freq='D'),
    'Values':[10,23,32,22,56]
}
df=pd.DataFrame(data)
df['Date']=pd.to_datetime(df['Date'])
# Converting Strings to Datetime:
# This line converts the Date column from string format to datetime format using the pd.to_datetime() function.
# This conversion is important for performing date-related operations and analyses later on, as it allows Pandas to recognize the values as dates rather than plain strings.
# df.set_index(keys='Date',inplace=True)
# Setting the Index
# This line sets the Date column as the index of the DataFrame using the set_index() method.
# The parameter keys='Date' specifies that the index should be set based on the values in the Date column.
# The parameter inplace=True means that this operation modifies the original DataFrame (df) directly rather than returning a new DataFrame.
# Setting an index can improve data retrieval performance and makes it easier to work with time series data.
print(df)
# monthly_df=df.resample('M').mean()
# 1. Resampling the DataFrame
# df.resample('M'):
# This part of the code uses the resample() method on the DataFrame df.
# The argument 'M' specifies that you want to resample the data on a monthly basis. In Pandas, 'M' stands for "month-end frequency," meaning it will group all data points within each month and aggregate them.
# Resampling is particularly useful for time series data, as it allows you to change the frequency of your data (e.g., from daily to monthly).
# print(monthly_df)
df['shifted value']=df['Values'].shift(1)
print(df)

# from the dateset we creating each seperate column as year,month & day
# df['Year']=df['Date'].dt.year
# df['month']=df['Date'].dt.month
# df['day']=df['Date'].dt.day
# print(df)