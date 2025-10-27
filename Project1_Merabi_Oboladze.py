#Merabi Oboladze
#30803
#19.10.2025
#30803
#I completed this work independently
import numpy as np
employees = {
 "E001": {
 "name": "Alice Johnson",
 "monthly_sales": [45000 , 52000 , 48000] ,
 "days_worked": 58
 },
 "E002": {
 "name": "Bob Smith",
 "monthly_sales": [38000 , 41000 , 39000] ,
 "days_worked": 60
 },
 "E003": {
 "name": "Carol White",
 "monthly_sales": [51000 , 49000 , 53000] ,
 "days_worked": 57
 },
 "E004": {
 "name": "David Brown",
 "monthly_sales": [42000 , 38000 , 40000] ,
 "days_worked": 55
 },
 "E005": {
 "name": "Emma Davis",
 "monthly_sales": [47000 , 50000 , 48000] ,
 "days_worked": 59
 },
 "E006": {
 "name": "Frank Miller",
 "monthly_sales": [35000 , 37000 , 36000] ,
 "days_worked": 52
},
 "E007": {
  "name": "Otar Kiparoidze",
 "monthly_sales": [43200 , 36700 , 33000] ,
 "days_worked":57
 },

 "E008": {
  "name": "Vazha Zhghenti",
 "monthly_sales": [33500 , 47000 , 51900] ,
 "days_worked":50
 }

}

#calculating total sales by sum function
def calculate_total_sales(monthly_sales):
    sumOfAllMonths=sum(monthly_sales)
    return sumOfAllMonths


print(calculate_total_sales(employees["E008"]["monthly_sales"]))
#calculating average by dividing sum by lenth of it
def calculate_average_sales (monthly_sales):
    avg1=sum(monthly_sales)/len(monthly_sales)
    return avg1

print(calculate_average_sales(employees["E008"]["monthly_sales"]))
#calculating attendance rate of speccific employee
def calc_attendance_rate(days_worked):
    atRate=(days_worked/60)*100
    return atRate

print(calc_attendance_rate(employees["E007"]["days_worked"]))   


def get_performance_rating(atRate,avg1):
    if(atRate>=95 and avg1>=4800):
        return "Excellent"
    elif(atRate>=90 and avg1>=4000):
        return "Good"
    else:
        return "Satisfactory"



ratings={
"Excellent":0,
 "Good":0, 
 "Satisfactory":0
 }


excellents=0
highest=("", 0)
total_sales=[]

#using cycle calculating every needed information
for ids, data in employees.items():
    total=calculate_total_sales(data["monthly_sales"])
    average=calculate_average_sales(data["monthly_sales"])
    attendance=calc_attendance_rate(data["days_worked"])
    rating=get_performance_rating(attendance, average)
    
    #counting numbers of excellent performances
    if rating=="Excellent":
        excellents=excellents+1
        total_sales.append(total)
    
    #calculating total by comparing each element and storing greatest value in highest[1] and the name of it in highest[0]
    if total>highest[1]:
        highest= (data["name"], total)

    print(f"\n{ids}-{data['name']}")
    print(f"Total Sales:${total:,.0f}")
    print(f"Avg Monthly:${average:,.2f}")
    print(f"Attendance:{attendance:.1f}%")
    print(f"Rating:{rating}")

avgg1=sum(total_sales)/len(total_sales)
hSaleName=highest[0]
hSale=highest[1]
print("Team's Statistics")
print(f"Count of excellent:{excellents}")
print(f"Average of total sales:${avgg1:,.0f}")
print(f"Top Performer: {hSaleName}(${hSale:,.0f})")