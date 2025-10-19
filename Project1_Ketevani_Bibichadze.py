
# ---------------------------
# Full Name: Ketevani Bibichadze
# Date: 19/10/2025
# I completed this work independently
# ---------------------------

import numpy as np

# Set random seed for reproducible results
np.random.seed(42)

print("Setup complete !")

#===================TASK 1=====================================
print("=" * 60)
print("TASK 1")
print("=" * 60)

#Part A
#Employee Database
employees = {
    "E001": {
        "name": "Alice Johnson",
        " monthly_sales ": [45000, 52000, 48000],  # Jan , Feb , Mar
        " days_worked ": 58
    },
    "E002": {
        "name": "Bob Smith",
        " monthly_sales ": [38000, 41000, 39000],
        " days_worked ": 60
    },
    "E003": {
        "name": "Carol White",
        " monthly_sales ": [51000, 49000, 53000],
        " days_worked ": 57
    },
    "E004": {
        "name": "David Brown",
        " monthly_sales ": [42000, 38000, 40000],
        " days_worked ": 55
    },
    "E005": {
        "name": "Emma Davis",
        " monthly_sales ": [47000, 50000, 48000],
        " days_worked ": 59
    },
    "E006": {
        "name": "Frank Miller",
        " monthly_sales ": [35000, 37000, 36000],
        " days_worked ": 52
    },
    "E007": {
        "name": "John Black",
        " monthly_sales ": [40000, 47000, 44000],
        " days_worked ": 55
    },
    "E008": {
        "name": "Emily Jonas",
        " monthly_sales ": [51000, 47000, 52000],
        " days_worked ": 58
    }

}

print(f"Total employees : {len(employees)}")


#Part B
def calculate_total_sales(monthly_sales):

 """
Calculate total sales across all months
Example: [45000 , 52000 , 48000] -> 145000
 """
 total = sum(monthly_sales)
 return total


def calculate_average_sales(monthly_sales):
    """
 Calculate average monthly sales
 Example: [45000 , 52000 , 48000] -> 48333.33
 """
    total = sum(monthly_sales)
    average = total / len(monthly_sales)
    return average


def calculate_attendance_rate(days_worked):

    """
 Calculate attendance as a percentage
 Example: 58 days out of 60 -> 96.67%
 """
    percentage = (days_worked / 60) * 100
    return percentage


def get_performance_rating(avg_sales, attendance_rate):

    """
 Assign performance rating based on criteria:
 - Excellent : avg_sales >= 48000 AND attendance >= 95%
 - Good: avg_sales >= 40000 AND attendance >= 90%
 - Satisfactory : Otherwise
 """
    if avg_sales >= 4800 and attendance_rate >=95 :
        return "Excellent"
    elif avg_sales >= 40000 and attendance_rate >= 90 :
        return "Good"
    else : return "Satisfactory"

 # Testing the functions
test_sales = [45000, 52000, 48000]
print(f"Total: ${ calculate_total_sales ( test_sales ):,.0f}")
print(f"Average: ${ calculate_average_sales ( test_sales ):,.2f}")
print(f" Attendance : { calculate_attendance_rate (58) :.2f}%")


#Part C
# Employee Performance Report

print("="*60)
print(" QUARTERLY PERFORMANCE REPORT")
print("="*60)

# For each employee , calculate and print their metrics
for emp_id , emp_data in employees .items ():
 name = emp_data["name"]

# TODO: Use your functions to calculate these
total = calculate_total_sales (emp_data[" monthly_sales "])
average = calculate_average_sales (emp_data[" monthly_sales "])
attendance = calculate_attendance_rate (emp_data[" days_worked "])
rating = get_performance_rating (average , attendance )

# Print formatted output
print(f"\n{emp_id} - {name}")
print(f" Total Sales: ${total :,.0f}")
print(f" Avg Monthly: ${average :,.2f}")
print(f" Attendance : { attendance :.1f}%")
print(f" Rating: {rating}")

print("\n" + "="*60)

# TODO: Calculate team statistics
# - How many employees have " Excellent " rating?
# - What 's the average total sales across all employees ?
# - Who has the highest total sales?

excellent_count = 0
total_sales_all_employees = 0
highest_sales = 0
top_salesperson = ""

for emp_id , emp_data in employees .items ():
    total= calculate_total_sales(emp_data[" monthly_sales "])
    average=calculate_average_sales(emp_data[" monthly_sales "])
    attendance=calculate_attendance_rate(emp_data[" days_worked "])
    rating=get_performance_rating(average,attendance)

    # count "excellent" rating
    if rating== "Excellent":
        excellent_count+=1

    #total sales of all employees
    total_sales_all_employees+=total

    #Salesperson with highest total sales
    if total > highest_sales:
        highest_sales=total
        top_salesperson=emp_data["name"]

#average total sales across all employees
average_total_sales = total_sales_all_employees/ len(employees)

#PRINTING THE ANSWERS
print(f"Employees with 'Excellent' rating: {excellent_count}")
print(f"Average total sales across all employees: ${average_total_sales:,.2f}")
print(f"Top performer: {top_salesperson} with ${highest_sales:,.2f}")


#======================================TASK 2=======================================
print("=" * 60)
print("TASK 2")
print("=" * 60)
#PART A

#Generate a 3D NumPy array with shape (4, 3, 12)
sales_data = {
    'stores': np.array(["Downtown", "Mall", "Airport", "Suburb"]),
    'categories': np.array(["Electronics", "Clothing", "Food"]),
    'sales': np.arange(5000, 5000 + 144*50, 50).reshape(4, 3, 12)
}

print(sales_data)

np.random.seed(42)


# ARRAY SHAPE AND DATA TYPE
print("Array shape:", sales_data['sales'].shape)
print("Data type:", sales_data['sales'].dtype)

# WEEK 1 SALES FOR ALL STORES AND CATEGORIES
print("\nWeek 1 sales for all stores and categories:")
print(sales_data['sales'][:, :, 0])

# BRIEF EXPLANATION OF THE ARRAY STRUCTURE
print("\nA brief explnation of the array structure:")
print("-Dimension 0 with 4 elements: Stores -", sales_data['stores'])
print("- Dimension 1 with 3 elements: Categories -", sales_data['categories'])
print("- Dimension 2: Weeks (Week 1 to Week 12)")
print(f"- For example, Week 6 sales value of Electronics in Downtown store is: sales_data['sales'][0, 1, 5] = ${sales_data['sales'][0, 1, 5]}")


#PART B
print("=" * 60)
print("PART B")
print("=" * 60)

# Calculate total sales for each store
total_sales_by_store = []
for i in range(4):
    total = sales_data['sales'][i].sum()
    total_sales_by_store.append(total)

# Display in a formatted table
print("\nStore Name     Total Sales")
for i in range(4):
    print(f"{sales_data['stores'][i]:<15}  ${total_sales_by_store[i]}")

# Identify which store had the highest and lowest total sales
max_index = total_sales_by_store.index(max(total_sales_by_store))
min_index = total_sales_by_store.index(min(total_sales_by_store))

print("\nStore with highest total sales is ", sales_data['stores'][max_index])
print("Store with lowest total sales is ", sales_data['stores'][min_index])


print("\n2. Category Performance")

#Calculate average weekly sales for each category across all stores
print("\nAverage weekly sales for each category across all stores:")
average_weekly_sales_by_category = []
for i in range(3):
    average = sales_data['sales'][:, i, :].mean()
    average_weekly_sales_by_category.append(average)
    print(f"{sales_data['categories'][i]}: ${average_weekly_sales_by_category[i]:.2f}")


#Calculate total sales by category
print("\nTotal sales by category:")
total_sales_by_category = []
for i in range(len(sales_data['categories'])):
    total = sales_data['sales'][:, i, :].sum()
    total_sales_by_category.append(total)
    print(f"{sales_data['categories'][i]}  ${total_sales_by_category[i]}")

#Determine which category is the revenue driver
max_index = total_sales_by_category.index(max(total_sales_by_category))
print("\nRevenue driver category is ", sales_data['categories'][max_index])


print("\n4. Weekly trends")

#Calculate total sales for each week (across all stores and categories)
print("\nTotal sales by each week:")
total_sales_by_week = []
for i in range(sales_data['sales'].shape[2]):   # 12 weeks
    total = sales_data['sales'][:, :, i].sum()
    total_sales_by_week.append(total)
for week in range(len(total_sales_by_week)):
    print(f"Week {week + 1}: ${total_sales_by_week[week]}")

#Identify the best and worst performing weeks
best_week = total_sales_by_week.index(max(total_sales_by_week)) + 1
worst_week = total_sales_by_week.index(min(total_sales_by_week)) + 1

print(f"\nBest performing: Week {best_week}")
print(f"Worst performing: Week {worst_week}")

#Calculate the week-over-week growth rate for the last 6 weeks
print("\nWeek-over-week growth rate for the last 6 weeks:")

for i in range(6, 12):  # Weeks 7 to 12
    previous_week = total_sales_by_week[i - 1]
    current_week = total_sales_by_week[i]
    growth_rate = ((current_week - previous_week) / previous_week) * 100
    print(f"Week {i} to Week {i + 1}: {growth_rate}%")

print("\n5. Store-specific insights ")

#For the Downtown store, find which category performed best

category_totals = []

for i in range(3):  #we have 3 categories
    total = sales_data['sales'][0, i, :].sum() #downtown store index is 0
    category_totals.append(total)

best_category_index = category_totals.index(max(category_totals))
print(f"\nDowntown store best performing category: {sales_data['categories'][best_category_index]}")

#Calculate the percentage contribution of each store to total company sales
print("\nPercentage contribution of each store to total company sales:")

total_company_sales = sales_data['sales'].sum()
for i in range(4):
    store_total = sales_data['sales'][i].sum()
    percentage = (store_total / total_company_sales) * 100
    print(f"{sales_data['stores'][i]}: {percentage:}%")


#PART C
print("=" * 60)
print("PART C")
print("=" * 60)


# COMPARE EACH STORE’S PERFORMANCE AGAINST THE COMPANY AVERAGE

print("Store performance vs company average:")

total_sales_by_store = []
for i in range(4):  #the length of 'stores' is 4
    total_sales_by_store.append(sales_data['sales'] .sum())

company_avg_per_store = sum(total_sales_by_store) / 4

for i in range(4):
    diff = total_sales_by_store[i] - company_avg_per_store
    print(f"Store: {sales_data['stores'][i]} , Total: ${total_sales_by_store[i]} , Difference: ${diff}")


# IDENTIFY UNDERPERFORMING AND OVERPERFORMING STORES

underperforming = []
overperforming = []
for i in range(4):
    if total_sales_by_store[i] < company_avg_per_store:
        underperforming.append(sales_data['stores'][i])
    elif total_sales_by_store[i] > company_avg_per_store:
        overperforming.append(sales_data['stores'][i])

print("\nUnderperforming stores:", underperforming)
print("Overperforming stores:", overperforming)


# CALCULATE THE QUARTERLY GROWTH RATE

#total sales for each week
total_sales_weekly = []
for week in range(12):
    total = sales_data['sales'][:, :, week].sum()
    total_sales_weekly.append(total)

total_sales_weekly = np.array(total_sales_weekly)

# split into quarters( 3 weeks each)
Q1 = total_sales_weekly[0:3].sum()
Q2 = total_sales_weekly[3:6].sum()
Q3 = total_sales_weekly[6:9].sum()
Q4 = total_sales_weekly[9:12].sum()

#calculating quarterly growth rates (Q1 to Q2, Q2 to Q3, Q3 to Q4)
growth_Q1_Q2 = ((Q2 - Q1) / Q1) * 100
growth_Q2_Q3 = ((Q3 - Q2) / Q2) * 100
growth_Q3_Q4 = ((Q4 - Q3) / Q3) * 100

print(f"\nQuarterly growth Q1 → Q2: {growth_Q1_Q2:.2f}%")
print(f"Quarterly growth Q2 → Q3: {growth_Q2_Q3:.2f}%")
print(f"Quarterly growth Q3 → Q4: {growth_Q3_Q4:.2f}%")


# COMPARE FIRST 6 WEEKS AVERAGE VS. LAST 6 WEEKS AVERAGE
first6_avg = sum(total_sales_by_week[0:6]) / 6
last6_avg = sum(total_sales_by_week[6:12]) / 6
change_percentage = ((last6_avg - first6_avg) / first6_avg) * 100

print(f"Weeks 1-6 average: ${first6_avg:.2f}")
print(f"Weeks 7-12 average: ${last6_avg:.2f}")
print(f"Change Percentage: {change_percentage:.2f}%")

# BASED ON YOUR ANALYSIS, IDENTIFY WHICH CATEGORY TO PRIORITIZE FOR EXPANSION
total_sales_by_category = []
for i in range(3):
    total_sales_by_category.append(int(sales_data['sales'][:, i, :].sum()))

best_category_index = total_sales_by_category.index(max(total_sales_by_category))
best_category =sales_data['categories'][best_category_index]

print("\nCategory to prioritize for expansion: ", best_category)
# Recommend which store needs performance improvement
worst_store_index = total_sales_by_store.index(min(total_sales_by_store))
worst_store = sales_data['stores'][worst_store_index]
print("Store that needs improvement:", worst_store)

# SUGGEST AT LEAST 2 ACTIONABLE BUSINESS STRATEGIES SUPPORTED BY DATA

# A good business strategy would be to prioritize the top-performing category(food category)
# add more products in this category to increase sales. Second strategy: improving performance for
# the lowest-performing store, which is Downtown, analyze customer behaviour in that area
# and come up with marketing campaigns, discounts,etc.


#===============================Task 3===================================
print("="*60)
print(" Task 3: Customer Satisfaction Analysis ")
print("="*60)

# Set seed for reproducibility
np.random.seed(42)

# Create a 2D NumPy array (50 customers × 4 rating categories)
# normal distribution (mean=7.5, std=1.5)

ratings = np.random.normal(7.5, 1.5, 200)
ratings = ratings.reshape(50, 4)

ratings = np.clip(ratings, 1, 10) # clip ratings to 1-10
ratings = np.round(ratings, 1)  # round to one decimal

#category names
categories = np.array(["Electronics", "Clothing", "Food", "Accessories"])

print("Array shape:", ratings.shape)
print("\nSample ratings of first 5 customers:")
print(ratings[:5])


#####PART B#####

#OVERALL AVERAGE SATISFACTION SCORE ACROSS ALL CUSTOMERS AND CATEGORIES
overall_average = ratings.mean()
print(f"Overall average satisfaction: {overall_average:.2f}")

#OVERALL STANDARD DEVIATION
overall_std = ratings.std()
print(f"Overall standard deviation: {overall_std:.2f}")

#AVERAGE RATING FOR EACH OF THE 4 CATEGORIES
category_avg = ratings.mean(axis=0)
print("\nAverage rating per category:")
for i in range(4):
    print(f"{categories[i]}: {category_avg[i]:.2f}")

#STANDARD DEVIATION FOR EACH CATEGORY
category_std = ratings.std(axis=0)
print("\nStandard deviation per category:")
for i in range(4):
    print(f"{categories[i]}: {category_std[i]:.2f}")

# HIGHEST AND LOWEST RATED CATEGORIES
highest_cat_index = category_avg.argmax()
lowest_cat_index = category_avg.argmin()
print(f"\nHighest rated category: {categories[highest_cat_index]} ({category_avg[highest_cat_index]:.2f})")
print(f"Lowest rated category: {categories[lowest_cat_index]} ({category_avg[lowest_cat_index]:.2f})\n")

#EACH CUSTOMER’S AVERAGE SATISFACTION (ACROSS ALL 4 CATEGORIES)
customer_avg = ratings.mean(axis=1)
for i in range(50): #len of customers is 50
    print(f"Customer {i+1:>2} Average satisfaction : {customer_avg[i]:.2f}")

# THE MOST SATISFIED CUSTOMER (HIGHEST AVERAGE)
most_satisfied_cust_index = customer_avg.argmax()
print(f"\nMost satisfied customer: Customer {most_satisfied_cust_index+1} ")

#  THE LEAST SATISFIED CUSTOMER (LOWEST AVERAGE)
least_satisfied_cust_index = customer_avg.argmin()
print(f"Leasr satisfied customer: Customer {least_satisfied_cust_index+1} ")


#####PART C#####

#DEFINE SEGMENTS

#each customer's avg rating
customer_avg = ratings.mean(axis=1)
#initializing empty array for segments
segments = [''] * 50
#assigning segments
for i in range(50):
    if customer_avg[i] >= 8.0:
        segments[i] = 'Promoter'
    elif customer_avg[i] >= 6.0:
        segments[i] = 'Passive'
    else:
        segments[i] = 'Detractor'

# COUNT AND PERCENTAGE OF CUSTOMERS IN EACH SEGMENT
promoters_count = segments.count('Promoter')
passives_count = segments.count('Passive')
detractors_count = segments.count('Detractor')

total_customers = 50

print("Segment counts and percentages:")
print(f"Promoters: {promoters_count} ({(promoters_count/50)*100:.1f}%)")
print(f"Passives: {passives_count} ({(passives_count/50)*100:.1f}%)")
print(f"Detractors: {detractors_count} ({(detractors_count/50)*100:.1f}%)")

# NET PROMOTER SCORE (NPS) = (PROMOTERS - DETRACTORS) / TOTAL × 100
NPS = ((promoters_count - detractors_count) / total_customers) * 100
print("\nNet Promoter Score (NPS): ", NPS)

# AVERAGE RATING FOR EACH SEGMENT

promoter_avg_ratings = []
passive_avg_ratings = []
detractor_avg_ratings = []


for i in range(50):
    if segments[i] == 'Promoter':
        promoter_avg_ratings.append(customer_avg[i])
    elif segments[i] == 'Passive':
        passive_avg_ratings.append(customer_avg[i])
    else:
        detractor_avg_ratings.append(customer_avg[i])


print("\nAverage rating per segment:")
print(f"Promoters: {np.mean(promoter_avg_ratings):.2f}" if promoter_avg_ratings else "Promoters: N/A")
print(f"Passives: {np.mean(passive_avg_ratings):.2f}" if passive_avg_ratings else "Passives: N/A")
print(f"Detractors: {np.mean(detractor_avg_ratings):.2f}" if detractor_avg_ratings else "Detractors: N/A")

# FOR DETRACTORS, IDENTIFY WHICH CATEGORIES HAVE THE LOWEST RATINGS
# Find indices of Detractors
detractor_indices = [i for i in range(50) if segments[i] == 'Detractor']

if detractor_indices:
    detractor_ratings = ratings[detractor_indices, :]
    category_avg_detractors = detractor_ratings.mean(axis=0)

    # Print category averages
    print("\nCategory averages for Detractors:")
    for i in range(4):
        print(f"{categories[i]}: {category_avg_detractors[i]:.2f}")

    # Lowest rated category
    lowest_category = categories[category_avg_detractors.argmin()]
    print(f"\nLowest rated category among Detractors: {lowest_category}")

else:  # to handle case with no Detractors (N/A)
    print("\n Theres no Detractors in dataset. Category analysis is not applicable.")

print("=" * 60)
print("PART D")

print("\n EXECUTIVE SUMMARY")

print("""The overall customer satisfaction level is 7.41, and NPS = 24%, which 
    means that moderate portion of customers are highly satisfied, and majority
    of the customers are passive. Key findings are: 
    • Highest-rated category: Accessories (7.57)
    • Lowest-rated category: Food (7.27)
    • Top-performing store: Suburb
    • Lowest-performing store: Downtown
    """)

print("\n STRENGTHS & WEAKNESSES")

print("""Best performing service aspect: We have high sales in Electronics and
 Accessories, with many employees' performance being 'Excellent'. Weaknesses
 lie in the Food category, which is lowest rated(7.27) and has less customer 
 satisfaction. One more weakness is Downtown store which has lower sales 
 compared to other stores. Improvements are needed in both product offerings
 and store performance.
""")

print("\n STRATEGIC RECOMMENDATIONS")

print(""" • Food category improvement: Improve product variety, quality, discounts
            and promotions to increase sales and satisfaction.
          • Downtown store improvement: Staff training, marketing campaigns, customer
            engagement strategies in Downtown Store to increase sales and service 
            quality.
          • Engaging with customers: Loyalty programs and personalized offers to convert
            Passives into Promoters, and increase customer satisfaction.
""")

print("\n CUSTOMER RETENTION STRATEGY")

print(""" • Since there are no Detractors, the focus should be 
            on Passives, who make up 76% of customers.
          • As already mentioned, they can convert Passives to 
            Promoters through customer loyalty programs and 
            personalized. Improved food offerings and discounts
            could also be beneficial.

""")




































