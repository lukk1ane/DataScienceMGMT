import numpy as np
np.random.seed(42)

stores = ["Downtown", "Mall", "Airport", "Suburb"]
categories = ["Electronics", "Clothing", "Food"]
weeks = 12

sales = np.random.randint(5000, 15001, size=(4, 3, 12))

print(type(sales))
print(sales.shape)
print(f"Week 1 Sales : {sales[:,:,0]}")

# Part B
totalSales = sales.sum(axis=( 1,2))
print(f"Total Sales: {totalSales}") #Highest = Mall, Lowest = Downtown

avgWeeklySales = sales.mean(axis=(0,2))
print(f"Average Weekly sales: {avgWeeklySales}")


totalSalesCategory = sales.sum(axis=(0,2))
print(f"Total Sales in Each Category {totalSalesCategory}")


totalSalesWeek = sales.sum(axis=(0,1))
print(f"Totals Sales of Each Week {totalSalesWeek}")
best_week = np.argmax(totalSalesWeek) + 1
worst_week = np.argmin(totalSalesWeek) + 1
print(f"Best Week  {best_week},  Worst Week:  {worst_week}")

# growthRate = np.diff ?????!!!!!

downtownStore = sales[0, :, :].sum(axis = 1)
print(f"Downtown Store Sales {downtownStore}") # Highest Clothing



