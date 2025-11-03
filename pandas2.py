import pandas as pd
import numpy as np

# Task 1
df = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Red', 'Green', 'Blue', 'Red', 'Green', 'Blue', 'Red', 'Green','Red','Red','Red','Red','Red','Red','Red','Red'],
    'Shape': ['Circle', 'Square', 'Circle', 'Triangle', 'Square', 'Circle', 'Triangle', 'Square', 'Circle', 'Triangle','Circle','Circle','Circle','Circle','Circle','Circle','Circle','Circle'],
    'Size': ['Small', 'Medium', 'Small', 'Large', 'Medium', 'Small', 'Large', 'Medium', 'Small', 'Large','Small','Small','Small','Small','Small','Small','Small','Small']
})

# Group by all categorical columns and count occurrences
combo_counts = df.groupby(['Color', 'Shape', 'Size']).size().reset_index(name='count')
frequent_combos = combo_counts[combo_counts['count'] >= 10]
print(frequent_combos)

# Task 2
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah'],
    'Age': [25, np.nan, 30, 22, np.nan, 28, 35, np.nan],
    'City': ['NY', 'LA', np.nan, 'NY', 'LA', np.nan, 'LA', 'NY'],
    'Score': [90, 85, np.nan, 88, 92, np.nan, 95, 89],
    'Department': ['HR', np.nan, 'IT', 'IT', 'HR', 'Finance', np.nan, 'IT']
}

df = pd.DataFrame(data)
missing_percentage = df.isna().mean() * 100
print(missing_percentage.nlargest(3))
df = df.dropna(subset = missing_percentage.nlargest(3).index)
print(df)


# Task 3
df = pd.DataFrame({
    'A': np.random.choice(['X','Y','Z'], size=100000),
    'B': np.random.randint(0,10, size=100000),
    'C': np.random.choice([True, False], size=100000)
})
most_frequent = {}
for col in df.columns:
    counts = df.groupby(col).size()
    most_frequent[col] = counts.idxmax()
    
print(most_frequent)

# Task 4
def employees_5_consecutive_days(df, emp_col='Employee ID', date_col='Date'):
    df = df.copy()
    df[date_col] = pd.date_time(df[date_col])
    df_sorted = df.sort_values([emp_col, date_col])
    df_sorted['diff'] = df_sorted.groupby(emp_col)[date_col].diff().dt.days.fillna(0)
    df_sorted['consec'] = df_sorted.groupby(emp_col)['diff'].apply(lambda x: (x == 1).cumsum())
    emp_bool = df_sorteed.groupby(emp_col)['consec'].apply(lambda x: (x.diff().fillna(0) == 1).rolling(5).sum().ge(4).any())
    
    return emp_bool[emp_bool].index.tolist()

# Task 5
dates = pd.date_range(start='2023-01-01', end='2023-06-30', freq='D')
np.random.seed(42)  # for reproducibility
values = np.random.randint(1, 10, size=len(dates))

df = pd.DataFrame({'value': values}, index=dates)
# print(df.head(31))
# montly_sum = df.resample('M').sum()
# print(montly_sum)
# print('\n')
# print(montly_sum[montly_sum.index.month.isin([1,2,3])])


# Task 6
# np.random.seed(42)
# transactions = pd.DataFrame({
#     'TransactionID': range(1, 21),
#     'Value': np.random.randint(50, 1000, size=20)
# })
# print("Original transactions:\n", transactions)
# print('\n')
# threshold = transactions['Value'].quantile(0.95)
# filtered_data = transactions[transactions['Value'] <= threshold]
# print(filtered_data)

# Task 7
dates = pd.to_datetime([
    '2023-01-01', '2023-01-02', '2023-01-05', '2023-01-07',
    '2023-01-08', '2023-01-10', '2023-01-12'
])
# np.random.seed(42)
# values = np.random.randint(10, 50, size=len(dates))

# ts = pd.Series(values, index = dates)
# print(ts)
# print('\n')
# ts_daily = ts.resample('D').mean()
# ts_filled = ts_daily.fillna(method = 'ffill')
# print(ts_filled)

# moving_avg = ts_filled.rolling('3D').mean()
# print(moving_avg)

# # Task 8
# np.random.seed(42)
# transactions = pd.DataFrame({
#     'TransactionID': range(1, 11),
#     'Amount': np.random.randint(50, 200, size=10)
# })
# print("Transactions:\n", transactions)

# threshold = 500
# transactions['CumulativeSum'] = transactions['Amount'].cumsum()
# first_exceeded_index = transactions.index[transactions['CumulativeSum'] > threshold][0]
# first_exceeded_transaction = transactions.loc[first_exceeded_index]
# print(first_exceeded_index, first_exceeded_transaction)


# # Task 9
# df = pd.DataFrame({
#     'Category': ['A','A','B','B','C','C'],
#     'Value': [10, 25, 5, 20, 7, 15],
#     'OtherInfo': ['x','y','z','w','p','q']
# })
# print("\nOriginal DataFrame:\n", df)
# grouped = df.groupby('Category')['Value']
# max_indeces = grouped.idxmax()
# max_rows = df.loc[max_indeces]
# print(max_rows)

# # Task 10
df_nested = pd.DataFrame({
    'TransactionID': [1, 2, 3],
    'Details': [
        {'price': 100, 'tax': 5},
        {'price': 200, 'tax': 10},
        {'price': 150, 'tax': 7}
    ],
    'Category': ['A','B','A']
})
print("\nOriginal nested DataFrame:\n", df_nested)
details_column = df_nested['Details']
details_df = pd.json_normalize(details_column)
df_without_details = df_nested.drop(columns = 'Details')
df_flattened = pd.concat([df_without_details, details_df], axis = 1) #axis = 1 means stack columns
print(df_flattened)
