#to make life easier
import numpy as np
import pandas as pd

#Task1
"""print("Task1")

ser = pd.Series([10, 20, 30, 40, 50], index = ["a","b","c","d","e"])
print(ser)

print("="*40)"""
#Task2
"""print("Task2")

ser = pd.Series([100, 200, 300, 400, 500], index = ["a","b","c","d","e"])
print(ser["c"])
print(ser.iloc[2])

print("="*40)
"""#Task3
"""print("Task3")

ser1 = pd.Series(np.array([5, 10, 15, 20]), index = ['w','x','y','z'])
ser2 = pd.Series(np.array([2, 4, 6, 8]), index = ['w','x','y','p'])

print(ser1.add(ser2).dropna())
print(ser1.sub(ser2).dropna())
print(ser1.mul(ser2).dropna())
print(ser1.div(ser2).dropna())

print("="*40)"""
#Task4
"""print("Task4")

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

print("="*40)"""
#Task5
"""print("Task5")

ser = pd.Series(np.array([15,22,15,30,22,45,30,15]))
print(f'Unique values: {ser.unique()}, there are {ser.nunique()} of them.')
print(ser.value_counts())

print("="*40)"""
#Task6
print("Task6")

data = {
    "Item": ["Apple","Banana","Orange","Pineapple","Grapes"],
    "Cost": [25.0, 46.0, 36.0, 60.0, 51.0]
}
df = pd.DataFrame(data)
Tax = (pd.Series(df["Cost"]) * 10) / 100
Total = pd.Series(df["Cost"]) + Tax

df.insert(2,"Tax",Tax)
df.insert(3,"Total",Total)
print(df)

print("="*40)
# #Task7
# print("Task7")
# #Task8
# print("Task8")
# #Task9
# print("Task9")