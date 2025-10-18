# Nino Abramishvili
#18801074092
#19/10/2025
#I completed this work independently

import numpy as np
np.random.seed(42)

# task 1
# Employee Database

employees = {
    "E001" : {
        "name" : "Alice Johnson",
        "monthly_sales" : [45000, 52000, 48000],
        "days_worked" : 58
    },

    "E002" : {
        "name" : "John Smith",
        "monthly_sales" : [51000, 49000, 39000],
        "days_worked" : 60
    },

    "E003" : {
        "name" : "Carol White",
        "monthly_sales" : [51000, 49000, 53000],
        "days_worked" : 57
    },

    "E004": {
        "name": "David Brown",
        "monthly_sales": [42000, 38000, 40000],
        "days_worked": 55
    },

    "E005": {
        "name": "Emma Davis",
        "monthly_sales": [47000, 50000, 48000],
        "days_worked": 59
    },

    "E006": {
        "name": "Frank Miller",
        "monthly_sales": [35000, 37000, 36000],
        "days_worked": 52
    },

    # adding 2 employees

    "E007" : {
        "name" : "Nino Abramishvili",
        "monthly_sales" : [52000, 47500, 49000],
        "days_worked" : 51
    },

    "E008" : {
        "name" : "Mariam Gamrekelashvili",
        "monthly_sales" : [38500, 39000, 40100],
        "days_worked" : 53
    }

}

#calculating total employees
print(f"Total employees: {len(employees)}")


# to calculate total sales we need to sum up all monthly sales
def calculate_total_sales (monthly_sales):
    total = sum(monthly_sales)
    return total

#to calculate average sales we need to divide sum of monthly sales to the number of month
def calculate_average_sales (monthly_sales):
    average_sales = sum(monthly_sales)/len(monthly_sales)
    return average_sales

# attendance rate as a percentage out of 60 possible days
def calculate_attendance_rate (days_worked):
    attendance_rate = (days_worked/60)*100
    return attendance_rate

# performance rating
def get_performance_rating (avg_sales, attendance_rate):
    if avg_sales >= 48000 and attendance_rate >= 95:
         return "Excellent"
    elif avg_sales >= 40000 and attendance_rate >= 90:
        return "Good"
    else:
        return "Satisfactory"


# test the functions
test_sales = [45000, 52000, 48000]
print(f"Total: ${calculate_total_sales(test_sales):,.0f}")
print(f"Average: ${calculate_average_sales(test_sales):,.2f}")
print(f"Attendance: {calculate_attendance_rate(58):.2f}%")

# employee performance report

print("="*60)
print("QUARTERLY PERFORMANCE REPORT")
print("="*60)

excellent_count = 0
total_sales = 0
highest_total_sales = 0
top_performer = ""

# For each employee, calculating and printing their metrics
# we will use our functions to calculate their performance
for emp_id, emp_data in employees.items():
    name = emp_data["name"]
    total = calculate_total_sales(emp_data["monthly_sales"])
    average = calculate_average_sales(emp_data["monthly_sales"])
    attendance = calculate_attendance_rate(emp_data["days_worked"])
    rating = get_performance_rating(average, attendance)
    # printing outputs
    print(f"\n{emp_id} - {name}")
    print(f" Total Sales: ${total:,.0f}")
    print(f" Average Sales: ${average:,.2f}")
    print(f" Attendance: {attendance:.1f}%")
    print(f" Rating: {rating}")

    # Calculating team statistics
    # how many employees have Excellent ratings
    if rating=="Excellent":
        excellent_count+=1

    #What 's the average total sales across all employees?
    # first of all we should calculate total sales
    total_sales+=total

    #Who has the highest total sales?
    if total>highest_total_sales:
        highest_total_sales = total
        top_performer=name


print("="*60)
print("TEAM STATISTICS")
print("="*60)

# Printing how many employees have excellent rating
print(f"Number of Excellent Employees: {excellent_count}")


# Printing  average total sales across all employees
print(f"Average total sales of all employees: {total_sales/len(employees):,.2f}")

# Printing who has the highest total sales
print(f"Top performer: {top_performer} with ${highest_total_sales:,} in total sales")


#############################################################################################
# task 2
#1
np.random.seed(42)

#4 stores, 3 categories, 12 weeks
stores = ["Downtown", "Mall", "Airport", "Suburb"]
categories = ["Electronics", "Clothing", "Food"]
weeks = [f"week{i+1}" for i in range(0,12)]

# 3D array with shape (4, 3, 12) and sales values between 5000 and 15000
sales = np.random.randint(5000, 15000, size=(4, 3, 12))

#2
#printing array shape and data type
print(f"Array shape: {sales.shape}, Array type: {sales.dtype}")

#week 1 sales for all categories
print("\nWeek 1 sales for all stores and all categories:")
print(sales[:, :, 0])
print()

# Explanation of array structure
# The array sales is 3-dimensional and its shape is (4, 3, 12) - 4 stores, 3 categories, 12 weeks
# each element represents the sales amount between 5000, 15000 for a specific combinations of store, category and week


# part B Store performance analysis
# 1. total sales by store
total_sales_store = np.sum(sales, axis=(1,2))

# displaying total sales in a formatted table with store names
for i in range(len(stores)):
    print(f"{stores[i]}  ${total_sales_store[i]:,}")

# identifying highest and lowest sales
# as argmax returns the index of maximum value we can write:
highest_sales_store = stores[np.argmax(total_sales_store)]

#as argmin returns the index of minimum value so:
lowest_sales_store = stores[np.argmin(total_sales_store)]

print(f"Highest total sales have: {highest_sales_store}")
print(f"Lowest total sales have: {lowest_sales_store}")

#2 Category Performance

# average weekly sales for each category across all stores
average_weekly_sales = np.mean(sales, axis=(0,2))
print()
for i in range(len(categories)):
    print(f"average sales of {categories[i]}: ${average_weekly_sales[i]:.2f}")

# calculate total sales by category
sales_by_category =  np.sum(sales, axis=(0,2))

#Printing sales by category
print()
for i in range(len(categories)):
    print(f"Total sales of {categories[i]}: ${sales_by_category[i]}")

print()
# Determining which category is revenue driver
revenue_driver = categories[np.argmax(sales_by_category)]
print(f"Revenue driver category is {revenue_driver}")
print()

# Weekly trends
total_sales_for_weeks = np.sum(sales, axis=(0, 1))

# Printing total sales for each week
for i in range(len(total_sales_for_weeks)):
    print(f"week{i+1} sales: ${total_sales_for_weeks[i]:,}")

# Identifying best and worst performing weeks
best_performing_week = weeks[np.argmax(total_sales_for_weeks)]
worst_performing_week = weeks[np.argmin(total_sales_for_weeks)]

print(f"\nBest performing week is {best_performing_week}")
print(f"Worst performing week is {worst_performing_week}")

# Calculating the week-over-week growth rate for 6 weeks
print()
for i in range(6, 12):
     growth_rate = (total_sales_for_weeks[i]-total_sales_for_weeks[i-1])/total_sales_for_weeks[i-1] * 100
     print(f"week {i} -> week{i+1} growth rate: {growth_rate:.2f}%")
print()
#4 Store-specific insights
# for the Downtown store, find which category performed best

# select only downtown sales
downtown_sales = sales[0, :, :]
print(downtown_sales)
#finding the best category

# first of all find sales across categories
downtown_sales_by_categories = np.sum(downtown_sales, axis=1)

# choosing maximum between categories
best_category_downtown = categories[np.argmax(downtown_sales_by_categories)]

print(f"\nDowntown best category: {best_category_downtown}")

#  Calculate the percentage contribution of each store to total company sales
print("Store contribution in total sales:")
for i in range(len(stores)):
    print(f"{stores[i]}: {total_sales_store[i]/sum(total_sales_store)*100:.2f}%")

# Part C: Business Analysis & Recommendations

# 1. performance comparison:
#  Compare each store’s performance against the company average
#  Identify underperforming and overperforming stores

company_average = np.mean(total_sales_store)

print("\nPerformance vs company average: ")
for i in range(len(stores)):
    diff = total_sales_store[i] - company_average
    if diff<0:
        status ="Underperforming"
    else: status = "Overperforming"

    print(f"{stores[i]} is {status} ({diff} difference)")

# Growth analysis
#  Compare first 6 weeks average vs. last 6 weeks average

first6 = np.sum(total_sales_for_weeks[:6])
last6 = np.sum(total_sales_for_weeks[6:])
growth = ((last6-first6)/first6)*100

trend = "upward" if growth>0 else "downward"

print(f"\n growth rate is {growth:+,.2f}% and trend is {trend}")

##############################################################################
# Strategic recommendations
print("\nStrategic recommendations")
print(f"We should prioritize for expansion {revenue_driver} category")
print(f"Performance improvements needs {lowest_sales_store}")
print(f"Maintain strong sales in {highest_sales_store}")

###########################################################################################
#task 3
np.random.seed(42)

categories = ["Product Quality", "Customer Service", "Value for Money", "Delivery Speed"]

# generate 50 customers and 4 categories

ratings = np.random.normal(7.5, 1.5, size=(50,4))

# keep ratings between 1-10 and round it to 1 decimal
ratings = np.round(np.clip(ratings, 1, 10),1)

# Displaying the shape of array
print(f"\nThe shape of array is: {ratings.shape}")

# first 5 customers
print(f"\nFirst fime customers: \n{ratings[:5]}")

# Part B: Descriptive statistics
# Overall average satisfaction score across all customers and categories
overall_avg = np.mean(ratings)
print(f"\nOverall average satisfaction score is {overall_avg:.2f}")

# Overall standard deviation
overall_std = np.std(ratings)
print(f"Overall standard deviation is {overall_std:.2f}")
print()

# Category analysis
# Average rating for each of the 4 categories
categories_avg = np.mean(ratings, axis=0)
for i in range(len(categories)):
    print(f"{categories[i]}'s average: {categories_avg[i]:.2f}")
print()

# Standard deviation for each category
categories_std = np.std(ratings, axis = 0)
for i in range(len(categories)):
    print(f"{categories[i]}'s standard deviation: {categories_std[i]:.2f}")

# Identifying the highest and lowest rated categories
highest_rated_cat = categories[np.argmax(categories_avg)]
lowest_rated_cat = categories[np.argmin(categories_avg)]

print(f"\nHighest rated category is {highest_rated_cat}")
print(f"Lowest rated category is {lowest_rated_cat}")

# Customer level analysis
# Calculate each customer’s average satisfaction (across all 4 categories)
average_satisfaction = np.mean(ratings, axis=1)
print(f"\naverage satisfaction level of each customer: \n{average_satisfaction}")

# identifying most satisfied customer
most_satisfied = np.argmax(average_satisfaction)
print(f"\nmost satisfied customer is #{most_satisfied+1} customer (Avg is {average_satisfaction[most_satisfied]:.2f})")

least_satisfied = np.argmin(average_satisfaction)
print(f"least satisfied customer is #{least_satisfied} customer (Avg is {average_satisfaction[least_satisfied]:.2f})")

# Part C, customer segmentation
promoters = average_satisfaction>=8
passives = (average_satisfaction>=6) & (average_satisfaction<8)
detractors = average_satisfaction<6

# 2. calculate metrics

# count
count_prom = np.sum(promoters)
count_pass = np.sum(passives)
count_det = np.sum(detractors)
total = len(average_satisfaction)

# Percentages
prom_percentage = count_prom/total*100
pass_percentage = count_pass/total*100
det_percentage = count_det/total*100

print()
print(f"Promotes are: {count_prom} ({prom_percentage}%)")
print(f"Passives are: {count_pass} ({pass_percentage}%)")
print(f"detractors are: {count_det} ({det_percentage}%)")


# calculate nps
nps = ((count_prom - count_det)/total)*100
print(f"\nNet promoter score (NPS) is {nps}")

# average rating for each segment

avg_prom = np.mean(average_satisfaction[promoters]) if count_prom>0 else 0
avg_pass = np.mean(average_satisfaction[passives])if count_pass>0 else 0
avg_det = np.mean(average_satisfaction[detractors]) if count_det>0 else 0

print(f"\nAverage rating for promoters: {avg_prom:.2f}")
print(f"Average rating for passives: {avg_pass:.2f}")
print(f"Average rating for detractors: {avg_det:.2f}")

#3 category performance by segment
# For detractors, identify which categories have the lowest ratings
if count_det>0:
    detractor_data = ratings[detractors]
    detractor_category_avg = np.mean(detractor_data, axis=0)
    print("Detractor category averages:")
    for i in range(len(categories)):
        print(f"{categories[i]}: {detractor_category_avg[i]:.2f}")
     # for lowest category we need minimum from detractor's category averages
    print(f"\nLowest category for Detractors: {categories[np.argmin(detractor_category_avg)]}")
else:
    print("\nThere are no detractors, so overall satisfaction is strong")
print()
# part D Business insight report
print("-----------------------Executive Summary---------------------------")
print(f"The overall customer satisfaction is {overall_avg:.2f} (std {overall_std:.2f}) win an NPS of {nps}")
print(f"Key findings:")
print(f"{highest_rated_cat} received the highest average rating ({np.max(categories_avg):.2f}).")
print(f"{lowest_rated_cat} received the lowest average rating ({np.min(categories_avg):.2f}).")
print(f"The majority of customers are Passives ({pass_percentage:.2f}%), that shows moderate satisfaction.\n")

#2 Strength & Weaknesses
print(f"Strength: {highest_rated_cat} is performing best with an average score of {np.max(categories_avg):.2f}. "
      f"This suggests strong product consistency and customer trust.")
print(f"Weakness: {lowest_rated_cat} has the lowest rating ({np.min(categories_avg):.2f}), that indicates a need for improvement "
      f"in this area — likely due to perceived value or delivery concerns.\n")

# Strategic recommendations
print("Strategic Recommendations:")
print("Reassess pricing or enhance perceived value to address weaknesses in Value for Money or Delivery Speed.")
print("Invest in customer service training and faster response systems to improve overall experience.")
print("Introduce a continuous feedback and loyalty system to monitor satisfaction and convert Passives to Promoters.\n")

# Customer retention strategy
print("Customer retention strategy:")
if count_det > 0:
    print(f"For Detractors ({count_det} customers): Follow up personally to resolve key complaints, especially in "
          f"{categories[np.argmin(categories_avg)]}. Offer compensation or service recovery gestures.")
else:
    print("There are no Detractors,but it is important to continue monitoring to maintain satisfaction levels.")
    print("For Passives: Provide exclusive offers or reward programs to encourage repeat purchases.")
    print("For Promoters: Keep them engaged through early access to new products and referral bonuses.\n")

