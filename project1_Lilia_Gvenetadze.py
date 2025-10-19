# =====================================================
# Lilia Gvenetadze
# 60301162766
# 19-10-2025
# "I completed this work independently"
# ====================================================
import numpy as np

np.random.seed(42)
print("Setup complete!")


print("---- TASK 1 ----")
#Task1
#a
# Employee Database
employees = {
    "E001": {
        "name": "Alice Johnson",
        "monthly_sales": [45000, 52000, 48000],
        "days_worked": 58
    },
    "E002": {
        "name": "Bob Smith",
        "monthly_sales": [38000, 41000, 39000],
        "days_worked": 60
    },
    "E003": {
        "name": "Carol White",
        "monthly_sales": [51000, 49000, 53000],
        "days_worked": 57
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
    # other 2 employees
    "E007": {
        "name": "Lilia Gvenetadze",
        "monthly_sales": [51000, 45000, 52000],
        "days_worked": 56
    },
    "E008": {
        "name": "Nino Chkhartishvili",
        "monthly_sales": [48000, 53000, 55000],
        "days_worked": 60
    }
}

print(f"Total employees: {len(employees)}")


#b
def calculate_total_sales(monthly_sales):
    total = sum(monthly_sales)
    return total

def calculate_average_sales(monthly_sales):
    average = sum(monthly_sales) / len(monthly_sales)
    return average

def calculate_attendance_rate(days_worked):
    attendance_rate = (days_worked / 60) * 100
    return attendance_rate

def get_performance_rating(avg_sales, attendance_rate):
    if avg_sales >= 48000 and attendance_rate >= 95:
        return "Excellent"
    elif avg_sales >= 40000 and attendance_rate >= 90:
        return "Good"
    else:
        return "Satisfactory"


test_sales = [45000, 52000, 48000]
print(f"Total: ${calculate_total_sales(test_sales):,.0f}")
print(f"Average: ${calculate_average_sales(test_sales):,.2f}")
print(f"Attendance: {calculate_attendance_rate(58):.2f}%")



#c
print("="*60)
print("QUARTERLY PERFORMANCE REPORT")
print("="*60)

# here we save the information about employees, first the ratings of them and second one total sales:
ratings_list = []
total_sales_list = []

for emp_id, emp_data in employees.items():
    name = emp_data["name"]
    total = calculate_total_sales(emp_data["monthly_sales"])
    average = calculate_average_sales(emp_data["monthly_sales"])
    attendance = calculate_attendance_rate(emp_data["days_worked"])
    rating = get_performance_rating(average, attendance)
# here we add this employees info  to our lists
    ratings_list.append(rating)
    total_sales_list.append(total)

    print(f"\n{emp_id} - {name}")
    print(f" Total Sales: ${total:,.0f}")
    print(f" Avg Monthly: ${average:,.2f}")
    print(f" Attendance: {attendance:.1f}%")
    print(f" Rating: {rating}")

# here we calculate team statistics
excellent_count = ratings_list.count("Excellent")

average_sales = sum(total_sales_list) / len(total_sales_list)
# here we are seeing who has the best sales and who is the best employee
best_employee_name = ""
highest_sales = 0

for emp_id, emp_data in employees.items():
    total = calculate_total_sales(emp_data["monthly_sales"])
    if total > highest_sales:
        highest_sales = total
        best_employee_name = emp_data["name"]

print(f"Top performer: {best_employee_name} with ${highest_sales:,.0f}")



print("\n" + "="*60)
#How many employees have " Excellent" rating?
print(f"Excellent rating have: {excellent_count} employees ")
#What's the average total sales across all employees?
print(f"Average total sales are: ${average_sales:,.0f}")
#Who has the highest total sales?
print(f"{best_employee_name} has highest total sales")



print("\n" + "="*60+"\n")

print("---- TASK 2 ----")
#Task2
np.random.seed(42)
print("task2")

#a
#here creating the sales array
sales = np.random.randint(5000, 15000, size=(4, 3, 12))
#showing the array shape and data type
print("Shape:", sales.shape)
print("Data type:", sales.dtype)

stores = ["Downtown", "Mall", "Airport", "Suburb"]
categories = ["Electronics", "Clothing", "Food"]

#showing week 1 sales for all stores and categories
print("Week 1 sales all stores and categories: ")
print(sales[:, :, 0])

#b
#here we are calculating total sales for each of the 4 stores
store_total = np.sum(sales, axis=(1,2))
#Display in a formatted table with store names
for i, total in enumerate(store_total):
    print(f"{stores[i]} total sales: ${total:,.0f}")


#Identifying which store had the highest and lowest total sales
best_store_index = np.argmax(store_total)
worst_store_index = np.argmin(store_total)
print(f"\nBest store: {stores[best_store_index]}")
print(f"Worst store: {stores[worst_store_index]}")

#Category performance
#average weekly sales for each category across all stores
category_avg = np.mean(sales, axis=(0,2))
#total sales by category
category_total = np.sum(sales, axis=(0,2))

for i, cat in enumerate(categories):
    print(f"{cat}: Avg = ${category_avg[i]:,.2f}, Total = ${category_total[i]:,.0f}")

#here showing which category is the revenue driver
top_category_index = np.argmax(category_total)
print(f"\nRevenue driver: {categories[top_category_index]}")

#Weekly trends
#total sales for each week (across all stores and categories)
weekly_total = np.sum(sales, axis=(0,1))
#Identifying the best and worst performing weeks
best_week = np.argmax(weekly_total) + 1
worst_week = np.argmin(weekly_total) + 1

print(f"\nBest week: Week {best_week}")
print(f"Worst week: Week {worst_week}")
#the week-over-week growth rate for the last 6 weeks
growth = np.diff(weekly_total[-7:]) / weekly_total[-7:-1] * 100
print("\nWeek-over-week growth last 6 weeks:\n", np.round(growth, 2))


#Store-specific insights for downtown store
downtown_data = sales[0, :, :]
downtown_total = np.sum(downtown_data, axis=1)
best_category_index = np.argmax(downtown_total)

print(f"\nDowntown best category is {categories[best_category_index]}")

#percentage contribution of each store to total company sales
company_total = np.sum(sales)
store_percent = (store_total / company_total) * 100

for i, pct in enumerate(store_percent):
    print(f"{stores[i]} has {pct:.2f}% of total sales.")


#c
#Business Analysis & Recommendations

#companys average total sales across all stores
company_avg_sales = np.mean(store_total)
#performace comparison
print(f"Company average total sales: ${company_avg_sales:,.0f}")
# Comparing each store's performance
for i, total in enumerate(store_total):
    difference = total - company_avg_sales
    status = "overperforming" if total > company_avg_sales else "underperforming"
    print(f"{stores[i]}: ${total:,.0f}, {difference:+,.0f} vs avg, so it's  {status}")

#Identifying best and worst performers
overperformers = [stores[i] for i, total in enumerate(store_total) if total > company_avg_sales]
underperformers = [stores[i] for i, total in enumerate(store_total) if total < company_avg_sales]

print(f"\nOverperforming Stores: {', '.join(overperformers)}")
print(f"Underperforming Stores: {', '.join(underperformers)}")

#Growth analysis
# Calculating averages for first and last 6 weeks
first_half_avg = np.mean(weekly_total[:6])
last_half_avg  = np.mean(weekly_total[6:])

# Calculating quarterly growth rate
quarterly_growth_rate = ((last_half_avg - first_half_avg) / first_half_avg) * 100

# Determining if sales are trending upward or downward
if quarterly_growth_rate > 0:
    trend = "Upward"
elif quarterly_growth_rate < 0:
    trend = "Downward"
else:
    trend = "Stable"

print(" GROWTH ANALYSIS ")
print(f"Average weekly sales first 6 weeks is  ${first_half_avg:,.2f}")
print(f"Average weekly sales last 6 weeks is ${last_half_avg:,.2f}")
print(f"Quarterly growth rate is {quarterly_growth_rate:.2f}%")
print(f"Sales trend over the quarter is {trend}")

# as we can see from our analysis the best performing store is Mall and about 25.6% of total sales,
# top-selling categori is electronics from all the stores so we need to work expanding this categori since it provides highest revenue
#the wakest performer is downtown which has 23.6% of total sales, so it needs more improvements maybe we can promote this better or
#implement top performer Malls techniques that worked there to be bestseller store
# the bestselling week was 11 and worst was 8


print("---- TASK 3 ----")
#Task3
np.random.seed(42)
print("\n" + "="*60+"\n")
print("task3")

#a
#Data Generation
n_customers = 50
n_categories = 4
categories = ["Product Quality", "Customer Service", "Value for Money", "Delivery Speed"]
ratings = np.random.normal(loc=7.5, scale=1.5, size=(n_customers, n_categories))
# Ensure all values stay between 1 and 10
ratings = np.clip(ratings, 1, 10)
#Round ratings to 1 decimal place
ratings = np.round(ratings, 1)
#Display the array shape and show a sample of the first 5 customers
print("Ratings array shape:", ratings.shape)
print("\nSample of first 5 customers:")
for i in range(5):
    print(f"Customer {i+1:02d}: {ratings[i]}")


#b
#Descriptive Statistics
#Overall average satisfaction score across all customers and categories
overall_avg = np.mean(ratings)
#Overall standard deviation
overall_std = np.std(ratings)

print("\n")
print("Overall metrics")
print(f"Overall average satisfaction is {overall_avg:.2f}")
print(f"Overall standard deviation is {overall_std:.2f}")



#Category analysis
print("\n")
print("Category analysis")
#Average rating for each of the 4 categories
category_avg = np.mean(ratings, axis=0)
#Standard deviation for each category
category_std = np.std(ratings, axis=0)
#Identifying the highest and lowest rated categories
highest_cat_index = np.argmax(category_avg)
lowest_cat_index = np.argmin(category_avg)

for i, cat in enumerate(categories):
    print(f"{cat}: Average = {category_avg[i]:.2f}, Std = {category_std[i]:.2f}")
print(f"\nHighest rated category is {categories[highest_cat_index]}")
print(f"Lowest rated category is  {categories[lowest_cat_index]}")


#Customer-level analysis
#Calculate each customer’s average satisfaction (across all 4 categories)
customer_avg = np.mean(ratings, axis=1)
#Identify the most satisfied customer& least satisfied/
most_satisfied_idx = np.argmax(customer_avg)
least_satisfied_idx = np.argmin(customer_avg)

print("\n")
print("Customer-level analysis")
print(f"Most satisfied customer is N{most_satisfied_idx+1:02d}, average {customer_avg[most_satisfied_idx]:.2f}")
print(f"Least satisfied customer is N{least_satisfied_idx+1:02d}, average {customer_avg[least_satisfied_idx]:.2f}")




print("\n")
#c
#Customer Segmentation
#Define segments
promoters_mask = customer_avg >= 8.0
passives_mask = (customer_avg >= 6.0) & (customer_avg < 8.0)
detractors_mask = customer_avg < 6.0

#Count and percentage of customers in each segment
promoters_count = np.sum(promoters_mask)
passives_count = np.sum(passives_mask)
detractors_count = np.sum(detractors_mask)

promoters_perc = promoters_count / n_customers * 100
passives_perc = passives_count / n_customers * 100
detractors_perc = detractors_count / n_customers * 100

#Net Promoter Score (NPS) = (Promoters - Detractors) / Total × 100
nps = (promoters_count - detractors_count) / n_customers * 100

#Average rating for each segment
avg_promoters = np.mean(customer_avg[promoters_mask]) if promoters_count > 0 else 0
avg_passives = np.mean(customer_avg[passives_mask]) if passives_count > 0 else 0
avg_detractors = np.mean(customer_avg[detractors_mask]) if detractors_count > 0 else 0

print(f"Promoters are {promoters_count}, percentage of this customers are {promoters_perc:.1f}%, average rating for them are {avg_promoters:.2f}%")
print(f"Passives are {passives_count}, percentage of this customers are {passives_perc:.1f}%, average rating for them are {avg_passives:.2f}%")
print(f"detractors are {detractors_count}, percentage of this customers are {detractors_perc:.1f}%, average rating for them are {avg_detractors:.2f}%")
print(f"Net Promoter Score (NPS): {nps:.1f}")

#Category performance by segment
#For Detractors, identifying which categories have the lowest ratings, This reveals where improvements are most needed
if detractors_count > 0:
    detractor_ratings = ratings[detractors_mask, :]
    detractor_categ_avg = np.mean(detractor_ratings, axis=0)
    lowest_det_categ_index = np.argmin(detractor_categ_avg)
    print("\nDetractor's weakest category is ", categories[lowest_det_categ_index])
else:
    print("\nNo detractors in this dataset, since all customers rated ≥ 6 ")



#d
# this survey of 50 customers shows strong overall performance, with average satisfaction score of 7.41 and standard deviation 1.34
#NPS score is 24 so this means that more customer likes our store than don't
#from the category analysis we can clearly see that the best performing service is delivery speed, i this because it is well managed, have grat staff to do so
#aspect that needs the most improvement is value for money, because as we can see people think that pricing on products should be changed and improved
#data to support this you can see in part b on category analysis.
# strategic recommendations i can provide is improve value for money, since this is the least performing category, for this they can provide discounts or analyse pricing and offer more appropriate prices.
# also they should keep up with the good work on delivery speed, may give some incentives to the staff so they can continue good work
# they also should get feedback from customers and will know what aspets need improvement exactly and what they need to do to improve this
#If there are Detractors they  identify the categories they rated lowest and contact them personally to resolve issues.
#to convert passives to promoters they need to work on weaker aspects, see what they don't like and try to improve it.

