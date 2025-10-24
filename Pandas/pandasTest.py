import pandas as pd
import numpy as np
from pandas import value_counts

# Task 1
data = pd.Series([10,20,30,40,50], index = ["a","b","c","d","e"])
# print(data)

# Task 2
data2 = pd.Series([100,200,300,400,500])
# print(data2[1])

# Task 3
series1  = pd.Series([5,10,15,20], index = ['w', 'x', 'y', 'z'])
series2 = pd.Series([2,4,6,8], index = ['w', 'x', 'y', 'p'])

sum = series1.add(series2, fill_value = 0)
# print(sum)

sub = series1.sub(series2, fill_value = 0)

# print(sub)

mult = series1.multiply(series2,  fill_value = 1)
# print(mult)

div = series1.divide(series2,  fill_value = 1)
# print(div)

# Task 4
data3 = [
['Alice', 24, 'New York'],
['Bob', 27, 'Los Angeles'],
['Charlie', 22, 'Chicago'],
['David', 32, 'Houston'],
['Eva', 29, 'Phoenix']
]

df = pd.DataFrame(data3, columns = ["name", "age", "city"])
# print(df.head(3))
# print(df.tail(2))

# Task 5
series3 = pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
print(series3.nunique())
print(series3.value_counts())

# Task 6
itemData = [
    ["Iphone 17 ", 4900],
    ["Iphone 16 ", 3500],
    ["Iphone 15 ", 2500],
    ["Iphone 14 ", 2300],
    ["Iphone 13 ", 2200],
]
df2 = pd.DataFrame(itemData, columns = ['item', "price"])

df2["Tax"] = df2["price"] * 0.10

df2["Total"] = df2["price"] + df2["Tax"]

filteredDf = df2[df2["Total"] > 500]
# print(filteredDf)

# Task 7
productData = {
    'Product': ['Laptop', 'T-Shirt', 'Coffee Maker', 'Headphones', 'Desk Lamp', 'Sneakers', 'Smartphone', 'Backpack'],
    'Category': ['Electronics', 'Clothing', 'Home Appliances', 'Electronics', 'Home Decor', 'Footwear', 'Electronics', 'Accessories'],
    'Price': [1200, 25, 80, 150, 40, 90, 999, 60],
    'Stock': [15, 50, 20, 30, 25, 40, 10, 35]
}

df3 = pd.DataFrame(productData, columns = ['Product', 'Category', 'Price', 'Stock'])

# print(df3)
# print(f"{df3.isnull()} || {df3.notnull()}")
# print(df3.value_counts("Category"))
# print(df3.nlargest(3, "Price")["Price])
# print(df3.nsmallest(2, "Stock")["Stock])
# print(df3.shape)
# print(df3.ndim)

# Task 8
data6 = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Emma', 'Bob', 'Frank', 'Grace', 'Helen'],
    'Subject': ['Math', 'Science', 'English', 'History', 'Math', 'Science', 'History', 'English', 'Math', 'Science'],
    'Score': [85, 90, 78, 88, 92, 80, 75, 89, 95, 84],
    'Attendance': [95, 88, 90, 92, 97, 85, 87, 93, 98, 90]
}
df4 = pd.DataFrame(data6, columns = ['Student', 'Subject', 'Score', 'Attendance'])
df4 = df4.set_index("Student")


# print(df4.duplicated())
# print(df4.drop_duplicates())
df4_indexed = df4.set_index("Student")
print(df4_indexed.loc["John"])
print(df4.iloc[:3])
print(df4.query("Score > 80 and Attendance > 85"))
print(df4[df4["Score"].between(70,90)])
# print(df4)

