import numpy as np
import pandas as pd

#Task1
data=np.arange(10,51,10)
ser1=pd.Series(data, index=["A","B","C","D","E"])
print(ser1)

#Task2
ser2=pd.Series([100,200,300,400,500], index=["A","B","C","D","E"])
print(ser2["B"])


#Task3
a=pd.Series( [5, 10, 15, 20] , index= ['w', 'x', 'y', 'z'])
b=pd.Series([2, 4, 6, 8] , index= ['w', 'x', 'y', 'p'])
add=a.add(b, fill_value=0)
sub=a.sub(b, fill_value=0)
mul=a.mul(b, fill_value=0)
div=a.div(b, fill_value=0)
print(add, sub, mul, div)



#Task4

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Ella'],
    'Age': [25, 30, 22, 28, 26],
    'City': ['London', 'Paris', 'Berlin', 'Rome', 'Madrid']
}


df4=pd.DataFrame(data)
print(f" first 3 rows: {df4.head(3)}")
print(f" last 2rows: {df4.tail(2)}")
print(f" removes last 2: {df4.head(-2)}")


#Task5

series=pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
print(f"Unique values: {series.unique()}")
print(f"Count of unique values: {series.nunique()}")
print(f"frequency: {series.value_counts()}")


#Task6

shop=[["Phone",1000],
      ["Laptop",2000],
      ["Earphones",50],
      ["Charger",20],
      ["Case",15]
      ]

df6=pd.DataFrame(shop, columns=["Items","Cost"])
df6.insert(2, "Tax",df6["Cost"]*0.10)
df6.insert(3, "Total", df6["Cost"]+df6["Tax"])

print(df6[df6["Total"]>50])



#Task7

data7 = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Shoes', 'Watch', 'Bag', 'Camera'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Fashion', 'Accessories', 'Fashion', 'Electronics'],
    'Price': [1200, 800, 400, 100, 90, 250, 60, 950],
    'Stock': [10, 25, 15, 50, 100, 20, 30, 5]
}

df = pd.DataFrame(data7)



print(df.isnull())
print(df.notnull())
print(f"Quantity of products in each category: {df['Category'].value_counts()}")
print(f"Top 3 most expensive products: {df.nlargest(3, 'Price')}")
print(f"Top 2 lowest stock products: {df.nsmallest(2, 'Stock')}")
print(f"Shape: {df.shape}, number of dimensions: {df.ndim}")


#Task 8

data8= {
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Eva', 'Frank', 'Bob', 'Grace', 'Helen'],
    'Subject': ['Math', 'Science', 'English', 'History', 'Math', 'Science', 'English', 'Math', 'History', 'Math'],
    'Score': [85, 78, 92, 88, 70, 95, 60, 82, 77, 89],
    'Attendance': [90, 80, 95, 85, 75, 100, 60, 88, 82, 91]
}

df8=pd.DataFrame(data8)

print(df8['Student'].duplicated())

#Removing duplicated names
df_new=df8.drop_duplicates(subset=['Student'], keep='first')
print(df_new)

df_indexed=df8.set_index('Student')
print(df_indexed.loc['Charlie'])
#Retrieving first 3 rows
print(df8.iloc[:3])

query = df8.query("Score > 80 and Attendance > 85")
print(query)

#students whose scores are between 70 and 90
score_range=df8[df8['Score'].between(70,90)]
print(score_range)




