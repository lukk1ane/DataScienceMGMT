#to make life easier
import numpy as np
import pandas as pd

#Task1
print("="*40)
print("Task1")

ser = pd.Series([10, 20, 30, 40, 50], index = ["a","b","c","d","e"])
print(ser)

print("="*40)
#Task2
print("Task2")

ser = pd.Series([100, 200, 300, 400, 500], index = ["a","b","c","d","e"])
print(ser["c"])
print(ser.iloc[2])

print("="*40)
#Task3
print("Task3")

ser1 = pd.Series(np.array([5, 10, 15, 20]), index = ['w','x','y','z'])
ser2 = pd.Series(np.array([2, 4, 6, 8]), index = ['w','x','y','p'])

print(ser1.add(ser2).dropna())
print(ser1.sub(ser2).dropna())
print(ser1.mul(ser2).dropna())
print(ser1.div(ser2).dropna())

print("="*40)
#Task4
print("Task4")

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'Age': [25, 30, 22, 28, 35],
    'Country': ['USA', 'UK', 'Canada', 'Germany', 'Australia']
}
df = pd.DataFrame(data)

print(df.head(3))
print(df.tail(2))
print(df.head()) #default value (prints everything)
print(df.head(-2)) #negative value (prints everything except last 2)
print(df.head(6)) #out of range value (as range is bigger then the data it simply prints out everything)

print("="*40)
#Task5
print("Task5")

ser = pd.Series(np.array([15,22,15,30,22,45,30,15]))
print(f'Unique values: {ser.unique()}, there are {ser.nunique()} of them.')
print(ser.value_counts())

print("="*40)
#Task6
print("Task6")

data = {
    "Item": ["Apple","Banana","Orange","Pineapple","Grapes"],
    "Cost": [25.0, 46.0, 36.0, 60.0, 51.0]
}
df = pd.DataFrame(data)
Tax = (pd.Series(df["Cost"]) * 10) / 100 #Calculating Tax for each product's Cost

df.insert(2, "Tax", Tax)
df.insert(3, "Total", pd.Series(df["Cost"]) + Tax)
print(df)

print("="*40)
#Task7
print("Task7")

data = {
    "Product": ['Laptop', 'Smartphone', 'Headphones', 'Office Chair', 'Desk Lamp', 'Mouse', 'Backpack', 'Monitor'],
    "Category": ['Electronics', 'Electronics', 'Electronics', 'Furniture', 'Furniture', 'Electronics', 'Accessories', 'Electronics'],
    "Price": [1200, 800, 150, 250, 60, 40, 70, 300],
    "Stock": [15, 30, 50, 12, 25, 60, 40, 20]
}
df = pd.DataFrame(data)

print(df.isnull()) # false so it is not null
print(df.notnull()) # True so not null statement is true
print(df["Category"].value_counts()) #to find products in each Category
print(df.nlargest(3,"Price")) #to find top 3 products by price
print(df.nsmallest(2,"Stock")) #to find least 2 products by stock
print(f'This is {df.shape} dataframe with {df.ndim} dimensions') # basic info about dataframe

print("="*40)
#Task8
print("Task8")

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Alice', 'Bob', 'Fiona', 'George', 'Hannah'],
    'Subject': ['Math', 'Science', 'History', 'Math', 'English', 'Science', 'History', 'Math', 'Science', 'English'],
    'Score': [88, 75, 92, 85, 78, 90, 81, 95, 73, 89],
    'Attendance': [95, 88, 92, 85, 90, 98, 80, 99, 84, 93]
}

df = pd.DataFrame(data)
print(df[df.duplicated(subset=['Student'], keep=False)]['Student'].unique())
print(df.drop_duplicates(subset=['Student'], keep='first'))
print(df.drop_duplicates(subset=['Student'], keep='first').set_index('Student', inplace=True))
print(df["Student"].loc[0])
print(df["Student"].iloc[:3])
print(df.query("Score > 80 and Attendance > 85"))
print(df[df['Score'].between(70, 90)])
print("="*40)