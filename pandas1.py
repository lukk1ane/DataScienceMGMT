import pandas as pd

# Task 1
data = [10, 20, 30, 40, 50]
ser = pd.Series(data, index = ['a', 'b', 'c', 'd', 'e'])
print(ser)

# Task 2
data = [100, 200, 300, 400, 500]
ser = pd.Series(data)
print(ser[2])
ser = pd.Series(data, index = ['a', 'b', 'c', 'd', 'e'])
print(ser['c'])

# Task 3
s1 = pd.Series([5, 10, 15, 20], index=['w', 'x', 'y', 'z'])
s2 = pd.Series([2, 4, 6, 8], index=['w', 'x', 'y', 'p'])

add = s1.add(s2)
sub = s1.sub(s2)
mul = s1.mul(s2)
div = s1.div(s2)

add_clean = add.dropna()
sub_clean = sub.dropna()
mul_clean = mul.dropna()
div_clean = div.dropna()

print("Addition:\n", add_clean, "\n")
print("Subtraction :\n", sub_clean, "\n")
print("Multiplication:\n", mul_clean, "\n")
print("Division:\n", div_clean, "\n")

# Task 4
data = [
    ['Alice', 24, 'NY'],
    ['Bob', 27, 'LA'],
    ['Charlie', 22, 'Chicago'],
    ['David', 32, 'Houston'],
    ['Eva', 29, 'Phoenix'],
    ['Maria', 20, 'Georgia'],
    ['Kimberley', 26, 'Texas'],
    ['George', 35, 'San Francisco']
    ]

df = pd.DataFrame(data)
print(df.head(3))
print(df.tail(2))
print(df.head())
print(df.tail())
print(df.head(-2))  # This returns every row except the last 2
print(df.tail(-2))  # This returns every row except the first 2


# Task 5
data = [15, 22, 15, 30, 22, 45, 30, 15]
ser = pd.Series(data)
print(ser.unique())
print(ser.nunique())
print(ser.value_counts())


# Task 6
data = {
    'Item': ['TV', 'Phone', 'Laptop', 'Chair', 'Desk'],
    'Cost':[1000, 500, 2600, 20, 340]
}

df = pd.DataFrame(data)
df['Tax'] = df['Cost'] * 0.1    
df['Total'] = df['Cost'] + df['Tax']

filtered = df[df['Total'] > 50]
print(filtered)


# Task 7
df = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Phone', 'Tablet', 'Charger', 'Camera'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics', 'Electronics', 'Accessories', 'Electronics'],
    'Price': [1000, 25, 50, 200, 800, 400, 20, 600],
    'Stock': [5, 50, 30, 10, 15, 8, 100, 6]
})
print(df.isnull())
print(df.notnull())
print(df['Category'].value_counts())
print(df['Price'].nlargest(3)) #By default returns top 5
print(df['Price'].nsmallest(2)) #By default returns smallest 5
print(df.shape)
print(df.ndim)

# Task 8
df = pd.DataFrame({
    'Student': ['Anna', 'Ben', 'Cara', 'David', 'Anna', 'Eli', 'Fiona', 'George', 'Hannah', 'Ivan'],
    'Subject': ['Math', 'Science', 'Math', 'English', 'History', 'Math', 'Science', 'English', 'History', 'Science'],
    'Score': [85, 90, 75, 88, 92, 70, 95, 60, 89, 78],
    'Attendance': [95, 80, 88, 90, 86, 70, 98, 65, 92, 75]
})

print(df.duplicated(subset = 'Student'))
print(df.drop_duplicates(subset = 'Student'))
df = df.set_index('Student')
print(df)
print('\n')
print(df.loc['David'])
print('\n')
print(df.iloc[:3])
print('\n')
print(df.query('Score > 80 and Attendance > 85'))
print('\n')
print(df[df['Score'].between(70, 90)])
print('\n')
print(df['Score'].between(70, 90))