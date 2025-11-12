#  E-Commerce Data Analysis
# Nino Abramishvili
# 12/11/2025
# I completed this work independently


import pandas as pd
import numpy as np

# task 3, part A
customers = pd.read_csv('customers.csv')
products = pd.read_csv('products.csv')
transactions = pd.read_csv('transactions.csv')

print("Data loaded successfully!")

# Make copies to preserve original data
original_customers = customers.copy()
original_products = products.copy()
original_transactions = transactions.copy()

# displaying basic information for customers
print("Customers basic info")
# Number of rows and columns
print(f"Number of rows: {customers.shape[0]}")
print(f"Number of columns: {customers.shape[1]}")
# Column names
print("\nColumn names:")
print(customers.columns.tolist())
# First 5 rows
print("\nFirst 5 rows:")
print(customers.head())
print()

# Displaying basic information for products
print("Products basic info:")
# Number of rows and columns
print(f"Number of rows: {products.shape[0]}")
print(f"Number of columns: {products.shape[1]}")
# Column names
print("\nColumn names:")
print(products.columns.tolist())
# First five rows
print("\nFirst 5 rows:")
print(products.head())

# Displaying basic information for transactions:
print("\nTransactions basic info:")
# Number of rows and columns
print(f"Number of rows: {transactions.shape[0]}")
print(f"Number of column: {transactions.shape[1]}")
# Column names
print("\n Column names:")
print(transactions.columns.tolist())
# First 5 rows
print("\nFirst 5 rows:")
print(transactions.head())
print("\n" + "="*60)

# Part B: Explore Customer Data

# 1. How many customers do we have?
num_customers = customers.shape[0]
print(f"\nTotal number of customers: {num_customers}")

# 2. What countries are our customers from? How many from each country?
# so we need to count how many unique countries do we have and how many times each opf them repeat
country_counts = customers['country'].value_counts()
print("\nCustomers by country:")
print(country_counts)

# 3.  What is the age range of our customers (minimum, maximum, average)?
# Some values are strings with " years" appended so  we cannot directly calculate min, max, or mean.
# First of all, we need to convert age to numeric
# Use regex to remove all non-digit characters, this will remove year and leaves only numbers
customers['age_numeric'] = customers['age'].replace(regex=r'\D', value='').astype('float')

age_min = customers['age_numeric'].min()
age_max = customers['age_numeric'].max()
age_average = customers['age_numeric'].mean()

print("\nAge range of customers:")
print(f"Minimum age: {age_min}")
print(f"Maximum age: {age_max}")
print(f"Average age: {age_average:.2f}")

# 4.  How many customer records have missing email addresses?
missing_emails = customers['email'].isna().sum()
print(f"\nNumber of missing emails: {missing_emails}")

# 5. Are there any duplicate customer records?
duplicate_customers = customers.duplicated().sum()
print(f"\nNumber of duplicate customer records: {duplicate_customers}")
print("\n" + "="*60)


# Part C: Explore Product Data
# 1. How many products do we sell?
num_products = products.shape[0]
print(f"Total number of products: {num_products}")

# 2. What product categories do we have?
categories = products['category'].unique()
print("\nProduct categories")
print(categories)

# 3.  How many products in each category?
category_counts = products['category'].value_counts()
print("\nNumber of products in each category")
print(category_counts)

# 4. What is the price range (cheapest to most expensive)?
# Some prices are missing and some of them have negative values
# So it is necessary to excludee null values and negative prices to have valid data and calculate correctly min and max prices

valid_prices = products['price'][products['price']>0]
price_min = valid_prices.min()
price_max = valid_prices.max()

print("\nPrice range of products:")
print(f"Cheapest price of the product: {price_min}")
print(f"The price of most expensive product: {price_max}")

# 5. Which products are out of stock (stock = 0)
out_of_stock = products[products['stock']==0]
print("\nproducts that are out of stock:")
print(out_of_stock[['product_id', 'product_name', 'category', 'stock']])

# 6. Are there any data quality issues you notice?
print("\nData quality issues notices:")

# In the data we have missing prices, so I will check missing prices
missing_prices = products['price'].isna().sum()
print(f"Number of missing prices: {missing_prices}")

# Also, there I noticed that there are negative prices
negative_prices = (products['price']<0).sum()
print(f"Number of negative prices: {negative_prices}")

# Some of the stock quantity is unrealistic, in some cases quantity is greater than 10000
unrealistic_stock = (products['stock']>1000).sum()
print(f"Unrealistic stock values (values are greater than 1000): {unrealistic_stock}")

# In product names there are extra spaces
space_names = products['product_name'].str.contains(r'^\s+|\s+$').sum()
print(f"Product names with trailing spaces: {space_names}")

# In categories some of them are upper cased, some of them lower cased
mixed_case_categories = products['category'].str.islower().sum()
print(f"Categories with lowercase letters: {mixed_case_categories}")
print("\n" + "="*60)


#  Part D: Explore Transaction Data
print("Explore transactions data")
# 1.  How many transactions occurred?
num_transactions = transactions.shape[0]
print(f"Number of transactions: {num_transactions}")

# 2. What payment methods are used? How many transactions per method?
print("\nPayment methods that are used:")
print(transactions['payment_method'].unique())

# count how many transaction are with each method
transactions_per_method = transactions['payment_method'].value_counts()
print("\nNumber of transactions per method:")
print(transactions_per_method)

# 3. What is the date range of transactions?
# Convert 'transaction_date' to datetime
transactions['transaction_date'] = pd.to_datetime(transactions['transaction_date'], errors='coerce')

# Get earliest and latest transaction dates
date_min = transactions['transaction_date'].min()
date_max = transactions['transaction_date'].max()

print(f"\nDate range of transactions:")
print(f"Earliest transaction: {date_min.date()}")
print(f"Latest transaction: {date_max.date()}")

# Are there any missing values in the quantity column?
missing_quantities = transactions['quantity'].isna().sum()
print(f"\nNumber of transactions with missing quantities {missing_quantities}")

# Are there any duplicate transaction IDs?
duplicated_transactions = transactions['transaction_id'].duplicated().sum()
print(f"\nNumber of duplicated transaction ids: {duplicated_transactions}")
print("\n" + "="*60)

###################################################################
# Task 2 Data Cleaning
print("Data Cleaning")

# Part A: Clean customer data
print("Cleaning Customer Data")

# 1. Handle missing emails
# How many customers have missing emails
missing_emails = customers['email'].isna().sum()
print(f"\nNumber of customers with missing emails: {missing_emails}")

# Remove customers with missing emails (business rule: email required)
customers = customers.dropna(subset=['email'])

# Report how many customers were removed
print(f"\nRemoved {missing_emails} customers with missing emails")

# 2. Remove duplicate customers
# Identify duplicate customer records
duplicate_customers = customers[customers['customer_id'].duplicated()]
print("Duplicated customers record:")
print(duplicate_customers[['customer_id', 'name']])

# Keep the first occurrence, remove others
customers = customers.drop_duplicates(subset='customer_id', keep = 'first')

# Reporting how many duplicates were found
num_duplicated = duplicate_customers.shape[0]
print(f"\nRemoved {num_duplicated} duplicate customer records.")

# 3. Standardize country names:
# Changing US and USA to United States

# Understand how many US and USA do we have
number_of_changed = customers['country'].isin(['USA', 'US']).sum()

# Standardise to have only United States
customers['country'] = customers['country'].replace(['US', 'USA'], 'United States')

# Report how many records were changed
print(f"\n{number_of_changed} records were changed to United States")

# 4. Verify the cleaned data:
print("\nVerification after cleaning:")

# Confirm no missing emails remain
print(f"number of missing customers emails: {customers['email'].isna().sum()}")

# confirm no duplicates remain
print(f"Number of duplicated records: {customers.duplicated().sum()}")

# Show final customer count
print(f"Final number of customers: {customers.shape[0]}")
print("\n" + "="*60)

########################################################
# Part B: Clean Products data
print("Cleaning Products Data")

# 1. Handle missing prices
#  Identify products with missing prices
missing_prices = products[products['price'].isna()]
print('products with missing prices')
print(missing_prices[['product_id', 'product_name', 'category', 'price']])

#  Fill missing prices with the median price of the same category
median_price = products.groupby('category')['price'].transform('median')
products['price'] = products['price'].fillna(median_price)

# Median is used because it’s less affected by extreme outliers than mean


# 2. Fix negative prices:
#  Find products with negative prices (data entry errors)
negative_prices = products[products['price'] < 0]
print("\nProducts with negative prices:")
print(negative_prices[['product_id', 'product_name', 'category', 'price']])

#  Convert negative prices to positive (remove minus sign)
products.loc[products['price']<0, 'price'] = products['price'].abs()

# Understand how many were fixed:
num_negative = negative_prices.shape[0]
print(f"\n{num_negative} prices were fixed (converted to positive).")

#3. Clean product names:
#  Remove extra spaces from product names
products['product_name'] = products['product_name'].str.strip()
print("\nRemoved extra spaces from product names.")

# 4. Verify the cleaned data:
print("\nVerification after cleaning:")
# Confirm no missing prices
print(f"Number of missing prices: {products['price'].isna().sum()}")
# Confirm no negative prices
print(f"Number of negative prices: {(products['price']<0).sum()}")
# Show sample of cleaned products
print("Sample of cleaned product data:")
print(products.head())

############################################################################################
# Part C: Clean Transaction Data

# 1. Handle missing quantities:
#  Identify transactions with missing quantity
missing_quantity = transactions[transactions['quantity'].isna()]
print("\nTransactions with missing quantities:")
print(missing_quantity[['transaction_id', 'customer_id', 'product_id', 'quantity']])

# Fill with 1 (most common single-item purchase)
transactions['quantity'] = transactions['quantity'].fillna(1)

# Report how many were filled
num_missing_quantity = missing_quantity.shape[0]
print(f"\nfilled {num_missing_quantity} missing quantities with 1")

# Remove duplicate transactions
# Find duplicate transaction IDs
duplicate_transactions = transactions[transactions.duplicated(subset='transaction_id', keep='first')]
print("Duplicate transactions found:")
print(duplicate_transactions[['transaction_id', 'customer_id', 'product_id', 'quantity']])

# remove duplicate transactions id
transactions = transactions.drop_duplicates(subset='transaction_id', keep='first')

# count number of duplicates
num_duplicates = duplicate_transactions.shape[0]
print(f"\n{num_duplicates} duplicate transactions were removed.")

# cleaning summary

# calculating rows of original data and changed data
original_customers_rows = original_customers.shape[0]
original_products_rows = original_products.shape[0]
original_transactions_rows = original_transactions.shape[0]

final_customers = customers.shape[0]
final_products = products.shape[0]
final_transactions = transactions.shape[0]

# Calculate how many rows changed
removed_customers = original_customers_rows - final_customers
removed_products = original_products_rows - final_products
removed_transactions = original_transactions_rows - final_transactions

print("\n" + "="*60)
print("Cleaning Summary")
print(f"Customers - original customers: {original_customers_rows}, final customers: {final_customers}, removed customers: {removed_customers}")
print(f"Products - original products: {original_products_rows}, final products: {final_products}, removed products: {removed_products}")
print(f"Transactions - original transactions: {original_transactions_rows}, final transactions: {final_transactions}, removed transactions: {removed_transactions}")
print(f"Total records removed across all datasets: {removed_customers + removed_products + removed_transactions}")

print("\n" + "="*60)

#######################################################################
# task 3:  Business Analysis & Reporting

# Part A: Merge the Datasets
# 1: Merge transactions with customers (on customer_id)
sales_data = pd.merge(customers, transactions, on = 'customer_id')

# merge with products
sales_data = pd.merge(sales_data, products, on = 'product_id')

# keep essential rows
sales_data = sales_data[['transaction_id', 'transaction_date', 'quantity', 'payment_method',
    'customer_id', 'name', 'country', 'age_numeric',
    'product_id', 'product_name', 'category', 'price']]

# 4. verifying
print("Merged dataset info:")
print(sales_data.info())
print(f"Number of rows in merged dataset: {sales_data.shape[0]}")
print("\nFirst 5 rows:")
print(sales_data.head())

# Part B: Calculate Business Metrics
# 1. add new column revenue
sales_data['revenue'] = sales_data['price'] * sales_data['quantity']

# 2. Time-based features
# Extract month from transaction date
sales_data['month'] = sales_data['transaction_date'].dt.month
# Extract day of week (Monday, Tuesday, etc.)
sales_data['day_of_week'] = sales_data['transaction_date'].dt.day_name()

# 3. Customer segments
total_spending_per_customer = sales_data.groupby('customer_id')['revenue'].sum().reset_index()
total_spending_per_customer.rename(columns={'revenue':'total_spent'}, inplace=True)

# merge this to sales data on customer id
sales_data =  pd.merge(sales_data, total_spending_per_customer, on = 'customer_id')

# sales segmentation
def classify_spender(amount):
    if amount>1000:
        return 'high spender'
    elif amount > 500:
        return 'medium spender'
    else: return 'low spender'

# classifying customers
sales_data['segment'] = sales_data['total_spent'].apply(classify_spender)

##############################################
# Part C Generate Business Reports
# Revenue Analysis
print("\n--- revenue analysis ---")

# What is total revenue across all transactions?
total_revenue = sales_data['revenue'].sum()
print(f"Total revenue: ${total_revenue:,.2f}")

#  What is revenue by product category? (show top 3)
# sort it in ascending order and then chose first 3
revenue_by_category = sales_data.groupby('category')['revenue'].sum().sort_values(ascending=False)
print("\nRevenue by product category (top 3):")
print(revenue_by_category.head(3))

# Which month had the highest revenue?
# calculate revenue by months
revenue_by_month = sales_data.groupby('month')['revenue'].sum()
# choose the best month
best_month = revenue_by_month.idxmax()
print(f"\nMonth with highest revenue: {best_month} (${revenue_by_month[best_month]:.2f})")

#  What is the average transaction value?
avg_transaction_value = sales_data['revenue'].mean()
print(f"\nAverage transaction value: ${avg_transaction_value:.2f}")

# 2. Customer insights
#  Whoare the top 5 customers by spending?
# we should sort and with head function choose first 5
top_customers = total_spending_per_customer.sort_values('total_spent', ascending=False).head(5)
print("\nTop 5 customers by spending:")
print(top_customers)

# What is the average spending per customer?
avg_spending_per_customer = total_spending_per_customer['total_spent'].mean()
print(f"\nAverage spending per customer: ${avg_spending_per_customer:.2f}")

#  Which country generates the most revenue?
# still, calculate sum by countries and then sort it
revenue_by_country = sales_data.groupby('country')['revenue'].sum().sort_values(ascending=False)
print("\nRevenue by country:")
print(revenue_by_country)

#  How many customers in each segment (High/Medium/Low)?
customers_per_segment = sales_data.groupby('segment')['customer_id'].nunique()
print("\nNumber of customers in each segment:")
print(customers_per_segment)

# Product Performance:
# Top 5 products by revenue
top_products_by_revenue = sales_data.groupby('product_name')['revenue'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 products by revenue:")
print(top_products_by_revenue)

# Top 5 products by quantity sold
top_products_by_quantity = sales_data.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 products by quantity sold:")
print(top_products_by_quantity)

# Most popular product category (by quantity sold)
popular_category = sales_data.groupby('category')['quantity'].sum().sort_values(ascending=False)
print("\nMost popular product category (by quantity sold):")
# we need only one product so with head choose only first row
print(popular_category.head(1))

# Average revenue per product category
avg_revenue_category = sales_data.groupby('category')['revenue'].mean().sort_values(ascending=False)
print("\nAverage revenue per product category:")
print(avg_revenue_category)

print("\nBusiness Recommendations:")

print(f"1. Focus growth on the top product category {revenue_by_category.idxmax()} which generated ${revenue_by_category.max():.2f} in revenue.")
print(f"2. Target high and medium spender customers for marketing, with {customers_per_segment.get('high spender',0)} high spenders and {customers_per_segment.get('medium spender',0)} medium spenders.")
print(f"3. Plan promotions around month {best_month}, which generated the highest revenue of ${revenue_by_month[best_month]:.2f}.")
print(f"4. Focus on '{revenue_by_country.idxmax()}', the country generating the most revenue (${revenue_by_country.max():,.2f}).")