import matplotlib.pyplot as plt
import numpy as np

# TASK 1:
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# temps = [12, 14, 15, 13, 16, 18, 17]
#
# plt.plot(days, temps)
# plt.xlabel("Day")
# plt.ylabel("Temperature (°C)")
# plt.title("Temperature Changes Over a Week")
# plt.grid(False)
# plt.show()


# TASK 2:
# days2 = range(1,31)
#
# p1_sales = [50,60,45,70,65,80,75,60,55,50,70,80,85,90,60,70,75,65,55,50,80,85,90,100,95,85,80,75,70,60]
# p2_sales = [40,50,35,60,55,70,65,50,45,40,60,70,75,80,50,60,65,55,45,40,70,75,80,90,85,75,70,65,60,50]
#
# plt.plot(days2, p1_sales, label="Product 1")
# plt.plot(days2, p2_sales, label="Product 2")
# plt.xlabel("Day of Month")
# plt.ylabel("Sales")
# plt.title("Sales Over Month")
# plt.legend()
# plt.show()

#TASK 3:
# x = np.random.rand(50)
# y = np.random.rand(50)
# z = np.random.rand(50)
#
# plt.scatter(x, y, c=z, s=z*300)
# plt.colorbar(label="Z value")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Scatter Plot with Third Variable (Color & Size)")
# plt.show()

#TASK 4:
# months = ["Jan", "Feb", "Mar"]
# store1 = [12000, 15000, 17000]
# store2 = [10000, 14000, 16000]
# store3 = [13000, 16000, 18000]
#
# x = np.arange(len(months))
# width = 0.25
#
# plt.bar(x - width, store1, width, label="Store 1")
# plt.bar(x, store2, width, label="Store 2")
# plt.bar(x + width, store3, width, label="Store 3")
#
# plt.xticks(x, months)
# plt.ylabel("Revenue")
# plt.title("Average Monthly Revenue (3 Stores)")
# plt.legend()
# plt.show()

#TASK 5:
# import matplotlib.pyplot as plt
# import numpy as np
#
# data1 = np.random.normal(50, 10, 1000)
# data2 = np.random.normal(60, 15, 1000)
#
# plt.hist(data1, bins=30, alpha=0.6, label="Group 1")
# plt.hist(data2, bins=30, alpha=0.6, label="Group 2")
# plt.legend()
# plt.title("Histogram Comparison")
# plt.show()

#TASK 6:
# segments = ["A", "B", "C", "D"]
# values = [30, 25, 20, 25]
# explode = [0.1, 0, 0, 0]  # highlight segment A
#
# plt.pie(values, labels=segments, explode=explode, autopct="%1.1f%%")
# plt.title("Customer Segments")
# plt.show()

#TASK7
# fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Line
# axs[0, 0].plot([1,2,3,4])
# axs[0, 0].set_title("Line Plot")
#
# # Bar
# axs[0, 1].bar(["A","B","C"], [3,5,2])
# axs[0, 1].set_title("Bar Chart")
#
# # Histogram
# axs[1, 0].hist(np.random.randn(1000))
# axs[1, 0].set_title("Histogram")
#
# # Scatter
# axs[1, 1].scatter(np.random.rand(50), np.random.rand(50))
# axs[1, 1].set_title("Scatter Plot")
#
# plt.tight_layout()
# plt.show()

#TASK 8:
# x = [1,2,3,4,5,6]
# y = [10,15,12,20,18,25]
#
# plt.plot(x, y, marker="o")
# plt.title("Customized Line Chart")
#
# # Highlight point
# plt.scatter(4, 20, s=200, edgecolor="black")
# plt.annotate("Peak Value", (4, 20), textcoords="offset points", xytext=(10,10))
#
# plt.show()

#TASK 9:
# matrix = np.random.rand(10, 10)
#
# plt.imshow(matrix, cmap="viridis")
# plt.colorbar()
# plt.title("10x10 Heatmap")
# plt.show()

#TASK 10:
fig = plt.figure(figsize=(12, 8))

# Line chart
plt.subplot(3, 1, 1)
plt.plot([1,2,3,4,5])
plt.title("Mini Visualization Report")

# Bar chart
plt.subplot(3, 1, 2)
plt.bar(["A","B","C"], [5,8,6])

# Scatter plot
plt.subplot(3, 1, 3)
plt.scatter(np.random.rand(50), np.random.rand(50))

plt.tight_layout()
plt.show()

