# Tekla Kbiladze
# ID - 30971
# Sun 19 Oct
#• Statement: ” I completed this work independently”


import numpy as np

# Set random seed for reproducible results
np.random.seed(42)

print("Setup complete!")

# task 1: Employee Performance Analysis (2%)
# Part A
employees = {
    "E001": {
        "name": "Alice Johnson",
        "monthly_sales": [45000,52000,48000], #Jan, Feb, Mar
        "days_worked": 58,
    } ,
    "E002": {
        "name": "Bob Smith",
        "monthly_sales": [38000,41000,39000], #Jan, Feb, Mar
        "days_worked": 60,
    } ,
    "E003": {
        "name": "Carol White",
        "monthly_sales": [51000,49000,53000], #Jan, Feb, Mar
        "days_worked": 57,
    } ,
    "E004": {
        "name": "David Brown",
        "monthly_sales": [42000 , 38000 , 40000], #Jan, Feb, Mar
        "days_worked": 55,
    } ,
    "E005": {
        "name": "Emma Davis",
        "monthly_sales": [47000 , 50000 , 48000], #Jan, Feb, Mar
        "days_worked": 59,
    } ,
    "E006": {
        "name": "Frank Miller",
        "monthly_sales": [35000 , 37000 , 36000], #Jan, Feb, Mar
        "days_worked": 52,
    } ,
    "E007": {
        "name": "Tekla Kbiladze",
        "monthly_sales": [50000,45000,33000], #Jan, Feb, Mar
        "days_worked": 58,
    } ,
    "E008": {
        "name": "Gia Suramelashvili",
        "monthly_sales": [32000,45000,37000], #Jan, Feb, Mar
        "days_worked": 51,
    } ,
}
print (f" Total employees : {len( employees )}")

# Part B
def calculate_total_sales ( monthly_sales ):
    """
    Calculate total sales across all months
    Example : [45000 , 52000 , 48000] -> 145000
    """
    total = sum( monthly_sales )
    return total

def calculate_average_sales ( monthly_sales ):
    """
    Calculate average monthly sales
    Example : [45000 , 52000 , 48000] -> 48333.33
    """
    average = sum( monthly_sales )/len( monthly_sales )
    return average

def calculate_attendance_rate ( days_worked ):
    """
    Calculate attendance as a percentage
    Example : 58 days out of 60  -> 96.67%
    """
    attendance = (days_worked/60)*100
    return attendance

def get_performance_rating ( avg_sales,attendance_rate ):
    """
    Assign performance rating based on criteria :
    - Excellent : avg_sales >= 48000 AND attendance >= 95%
    - Good : avg_sales >= 40000 AND attendance >= 90%
    - Satisfactory : Otherwise
    """
    if avg_sales >= 48000 and attendance_rate>=95  :
        performance_rating = "Excellent"
    elif avg_sales >= 40000 and attendance_rate>=90 :
        performance_rating = "Good"
    else:
        performance_rating = "Satisfactory"
    return performance_rating



# Test my functions
test_sales = [45000 , 52000 , 48000]
print (f" Total : ${ calculate_total_sales ( test_sales ): ,.0f}")
print (f" Average : ${ calculate_average_sales ( test_sales ): ,.2f}")
print (f" Attendance : { calculate_attendance_rate (58) :.2f}%")
print (f" Performance_rating : { get_performance_rating (30000,97)}")


#part C : Generate Report
 # Employee Performance Report
print ("=" *60)
print (" QUARTERLY PERFORMANCE REPORT ")
print ("=" *60)
ratings = []
total_sales = []
names = []

# For each employee , calculate and print their metrics
for emp_id , emp_data in employees . items ():
    name = emp_data ["name"]

    total = calculate_total_sales ( emp_data ["monthly_sales"])
    average = calculate_average_sales ( emp_data ["monthly_sales"])
    attendance = calculate_attendance_rate ( emp_data ["days_worked"])
    rating = get_performance_rating ( average , attendance )

    # Print formatted output
    print (f"\n{ emp_id } - { name }")
    print (f" Total Sales : ${ total : ,.0f}")
    print (f" Avg Monthly : ${ average : ,.2f}")
    print (f" Attendance : { attendance :.1f}%")
    print (f" Rating : { rating }")
    #To have a lists
    ratings.append(rating)
    total_sales.append(total)
    names.append(name)
print ("\n" + "=" *60)

# TODO : Calculate team statistics
# - How many employees have " Excellent " rating ?
# Collect for later stats
count = ratings.count("Excellent")
print(f"Number of Excellent employees: {count}")
# - Who has the highest total sales ?
max_sales = max(total_sales)
best_employee = names[total_sales.index(max_sales)]
print(f"Highest Total Sales: {best_employee} ${max_sales:,.0f}")
# - What 's the average total sales across
average_total_sales = sum(total_sales) / len(total_sales)
print(f"Average Total Sales Across: ${average_total_sales:,.2f}")




#Task 2

# Part A
import numpy as np

# Arrays
stores = ["Downtown", "Mall", "Airport", "Suburb"]
categories = ["Electronics", "Clothing", "Food"]
weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Random seed
np.random.seed(42)

# Sales value
sales_values_bet = np.random.randint(5000, 15000, size=(4, 3, 12))

# Prints
#Shapes
print("Array Shape:", sales_values_bet.shape)
print("Data Shape:", sales_values_bet.dtype)
#Sample data for 1 week
week_1_sales = sales_values_bet[:, :, 0]  # first week along axis 2
print("\nWeek 1 sales:")
print(week_1_sales)
#Explanation of Array Structure
#we have 3D array. where the AXIS 0 -> the first layer of this aray
#represents the stores, AXIS 1 -> the second layer of this aray represents the
#categories what are they selling and the last layer AXIS 2 -> represents weeks
#from 1 to 12. so we have 4 stores, 3 categories and 12 weeks.

# Part B

#1 Total Sales

# Calculate total sales for each of the 4 stores (sum across all categories and weeks)
stores_total_sales = sales_values_bet.sum(axis=(1, 2))

# Display in a formatted table with store names
print("\nTotal Sales by Store:")
for store, total in zip(stores, stores_total_sales):
    print(f"{store}: ${total:,.0f}")

# • Identify which store had the highest and lowest total sales
print(f"\nHighest : {stores[stores_total_sales.argmax()]}")
print(f"Lowest : {stores[stores_total_sales.argmin()]}")

#2 Category Performance
#• Calculate average weekly sales for each category across all stores
average_category_per = sales_values_bet.mean(axis=(0, 2))

#• Calculate total sales by category
print("\nAverage weekly sales for categories:")
for category, avg in zip(categories, average_category_per):
    print(f"{category}: ${avg:,.2f}")

#• Determine which category is the revenue driver
print(f"\nRevenue driver category: {categories[average_category_per.argmax()]}")

#3 Weekly trends

#Calculate total sales for each week
weekly_sales = sales_values_bet.sum(axis=(0, 1))

# • Identify the best and worst week
print(f"\nBest : {weeks[weekly_sales.argmax()]}")
print(f"Worst : {weeks[weekly_sales.argmin()]}")

#Calculate week over week growth rate

# Select last 6 weeks
last_6_weeks = weekly_sales[-6:]

# Calculate week-over-week percentage growth
growth_rate = (last_6_weeks[1:] - last_6_weeks[:-1]) / last_6_weeks[:-1] * 100

print("\nWeek-over-week growth rate:")
for i, rate in enumerate(growth_rate, start=1):
    week_start = 12 - 6 + i
    week_finish = week_start + 1
    print(f"Week {week_start} → Week {week_finish}: {rate:.2f}%")

#4

# Best performing category

downtown_sales = sales_values_bet[0]
# Total sales per category for Downtown
total_per_category_downtown = downtown_sales.sum(axis=1)
best_category = categories[total_per_category_downtown.argmax()]
print(f"\nBest performing category for Downtown store: {best_category}")

# Percentage of each store contribution

# Total company sales
# Percentage contribution per store
percentage_per_store = stores_total_sales / sales_values_bet.sum() * 100

print("\nPercentage contribution per store: ")
for store, contribution in zip(stores, percentage_per_store):
    print(f"{store:10s}: {contribution:.2f}%")


#Task 3


import numpy as np
#Part A

categories = ["Product Quality", "Customer Service", "Value for Money", "Delivery Speed"]
np.random.seed(42)
ratings = np.random.normal(loc=7.5, scale=1.5, size=(50, 4))
ratings = np.clip(ratings, 1, 10)
ratings = np.round(ratings, 1)

#Display array shape
print("Shape:", ratings.shape)

#Sample 5 customers
print("\nSample 5 Customers:")
print(ratings[:5])


#Part B
#1 Overall Metrics
# Overall average satisfaction score
print(f"\nAverage satisfaction score: {ratings.mean():.2f}")

# Overall standard deviation
print(f"Standard deviation: { ratings.std():.2f}")


#2 Category analysis

# Average rating per category
average_per_category = ratings.mean(axis=0)

# Standard deviation per category
std_per_category = ratings.std(axis=0)

print("\nCategories:")
for cat, avg, std in zip(categories, average_per_category, std_per_category):
    print(f"{cat:18s}: Avg = {avg:.2f}, Std = {std:.2f}")

# Identify highest and lowest rated categories
print(f"\nHighest rated category: {categories[average_per_category.argmax()]}")
print(f"Lowest rated category: {categories[average_per_category.argmin()]}")


#3 Customer-level Analysis
#Average Satisfaction
satisfaction_per_custumer = ratings.mean(axis=1)

#Identify Most/Worst satisfied customer
print(f"\nMost Satisfied: {ratings[satisfaction_per_custumer.argmax()]}")
print(f"Least Satisfied: {ratings[satisfaction_per_custumer.argmin()]}")


#Part C Customer Segmentation

#1 Define Segment
customer_avg = ratings.mean(axis=1)

customer_segments = []

for avg in customer_avg:
    if avg >= 8.0:
        segment = "Promoters"
    elif avg >= 6.0:
        segment = "Passives"
    else:
        segment = "Detractors"
    customer_segments.append(segment)

# Convert to NumPy array
customer_segments = np.array(customer_segments)
# Show first 5 customer segments
print("\nFirst 5 customer segments:")
print(customer_segments[:5])

#2 Calculate Metrics
customer_segments = np.array(customer_segments)

segments = ["Promoters", "Passives", "Detractors"]
total_customers = len(customer_segments)

print("\nCustomer segments summary:")
for seg in segments:
    count = np.sum(customer_segments == seg)
    pct = (count / total_customers) * 100
    print(f"{seg:10s}: {count:2d} customers ({pct:.1f}%)")

# Calculate Net Promoter Score (NPS)
promoters_count = np.sum(customer_segments == "Promoters")
detractors_count = np.sum(customer_segments == "Detractors")
nps = (promoters_count - detractors_count) / total_customers * 100
print(f"\nNet Promoter Score (NPS) = {nps:.1f}")

# Average rating per segment
print("\nAverage rating per segment:")
for seg in segments:
    seg_check = customer_avg[customer_segments == seg]
    if len(seg_check) > 0:
        avg_rating = seg_check.mean()
        print(f"{seg:10s}: {avg_rating:.2f}")
    else:
        print(f"{seg:10s}: No customers")

#3 Category performance by segment

detractor_ratings = ratings[customer_segments == "Detractors"]

# Check if there are any Detractors, I am checking because in my case I have 0 Detractors
if len(detractor_ratings) > 0:
    avg_per_category_detractors = detractor_ratings.mean(axis=0)
    min_value = avg_per_category_detractors.min()
    lowest_categories = [category for category, val in zip(categories, avg_per_category_detractors) if val == min_value]

    print("\nLowest-rated categories:")
    for category in lowest_categories:
        print(f"- {category}: {min_value:.2f}")
else:
    print("\nThere are no Detractors")


#Part D Business Insight Report
#executive summary:
#overally the mainly costumers are satisfied, with an average score of 7.5 out of 10.
#The Net Promoter Score is 16, which shows that more customers are Promoters than Detractors,
# but there is still need to improve.
# Key findings:
#*Customer Services are performing very well, scoring the highest on average.
#*Delivery Speed is the weakest area, especially for unhappy customers, it has the lowest ratings among Detractors.
#*About 14% of customers are Detractors, meaning they are dissatisfied and i think they could leave if issues are not fixed soon.

#strengths and weaknesses:
#Strength: Customer Service are performing the best as it seems helpful, friendly, and responsive.
#Weakness: Delivery Speed needs more attention. Detractors gave these areas
#low ratings which is below 5/10, showing delays or concerns about these costs and it needs to be solved as soon as possible.
#Recommendations:
#first of all they have to fix delivery issues: better logistics and improve tracking so packages arrive on time.
#also offer deals, vouchers, or loyalty rewards to make customers feel they get more for their money.
#Use positive customer experiences to build trust, encourage repeat purchases, and attract new customers.

#customer retention strategy:
#so there are some customers who are unhappy with our service, if we ignore them,they may leave or share negative feedbacks.
#to solve this problems we need to contact them personally via email for example
#and turn detractors into loyal customers by fixing their problem.

#passive customers are moderately satisfied so we also need some improvements like
#give special deals, discounts. they are not unhappy but not enough loyal too,
#so we need to make them feel valued and turn neutral into loyal.
