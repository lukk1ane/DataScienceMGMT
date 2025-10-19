# Employee Database
# We use a dictionary - think of it like an Excel table
employees = {
    "E001": {
        "name": "Alice Johnson",
        "monthly_sales": [45000, 52000, 48000], # Jan, Feb, Mar
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
    "E007": {
        "name": "Bob Muller",
        "monthly_sales": [30000, 35000, 33000],
        "days_worked": 50
    },
    "E008": {
        "name": "Jonny Miller",
        "monthly_sales": [36000, 33000, 47000],
        "days_worked": 45
    }
}


# Fundamentals of Data Science
# Project 1: Business Data Analysis
# TODO: Add data for 2 more employees (E007 and E008)
# Make up realistic names and numbers
print (f"Total employees: {len (employees)}")


# task 1-b
def calculate_total_sales ( monthly_sales ):
 total = sum( monthly_sales )
 return total

def calculate_average_sales( monthly_sales ):
    average = calculate_total_sales( monthly_sales ) / 3
    return average

def calculate_attendance_rate(days_worked):
    attendance_rate = days_worked / 60 * 100
    return attendance_rate

def average_performance_rate(avg_sales, attendance_rate):
    if avg_sales >= 48000 and attendance_rate >= 95:
        return "Excellent"
    elif avg_sales >= 40000 and attendance_rate >= 90:
        return "Good"
    else:
        return "Satisfactory"

# Test functions
# print(f"Total ${calculate_total_sales(employees['E001']['monthly_sales'])}")
# print(f"Average ${calculate_average_sales(employees['E001']['monthly_sales'])}")
# print(f"Attendance {calculate_attendance_rate(employees['E001']['days_worked'])}%")
# print(f"Performance: {average_performance_rate(calculate_average_sales(employees['E002']['monthly_sales']), calculate_attendance_rate(employees['E002']['days_worked']))}")

# Task 1-c
print ("=" *60)
print (" QUARTERLY PERFORMANCE REPORT ")
print ("=" *60)

# For each employee , calculate and print their metrics
excellentRating = 0
totalSales = 0
highesTotalSales = 0

for emp_id , emp_data in employees.items ():
    name = emp_data["name"]

    total = calculate_total_sales(emp_data['monthly_sales'])
    average = round(calculate_average_sales(emp_data['monthly_sales']),2)
    attendance = round(calculate_attendance_rate(emp_data['days_worked']),2)
    rating = average_performance_rate(average, attendance)

    if rating == "Excellent":
        excellentRating += 1

    totalSales += total

    if(total > highesTotalSales):
        highesTotalSales = total

    print(f"\n{emp_id} - {name}")
    print(f" Total Sales : ${total : ,.0f}")
    print(f" Avg Monthly : ${average : ,.2f}")
    print(f" Attendance : {attendance :.1f}%")
    print(f" Rating : {rating}")

print("=" *60)
print(f"Excellent: {excellentRating}")
print(f"Average Total Sales : {totalSales / 8}")
print(f"Highest Total Sales : {highesTotalSales}")


