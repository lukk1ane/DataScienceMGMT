#for easier life
import numpy as np

# Task1
print("Task1")
numbers_arr = np.arange(1, 10, 1, dtype=np.int16)
print("This is the sum of numbers from 1 to 10{}".format(numbers_arr.sum()))
print("This is the product of number from 1 to 10{}".format(numbers_arr.prod())) 

#Task2
print("Task2")
numbers_arr2 = np.arange(0, 20, 1, dtype=np.int16)
print(numbers_arr2[3:8])

#Task3
print("Task3")
numbers_matrix = np.arange(0,25,1).reshape(5, 5)
print(numbers_matrix[0:2])
print(numbers_matrix[:,-2:])

#Task4
print("Task4")
a = np.array([1,2,3,4])
b = np.array([2,4,6,8])
b += a
print(b)
b = np.array([2,4,6,8])
b *= a
print(b)
b = np.array([2,4,6,8])
print(np.sin(b))

#Task5
print("Task5")
arr = np.random.randint(0, 50, size=20)
mask = arr > 25
print(arr[mask])

#Task6
print("Task6")
arr = np.arange(25).reshape(5, 5)
np.fill_diagonal(arr, 0)
arr = arr * 2
print(arr)

#Task7
print("Task7")
arr = np.arange(1,10).reshape(3, 3)
print(arr)
print(f"Second row:\n{arr[1]}")
print(f"Columns:\n{arr[:,0:2]}")

#Task8
print("Task8")
arr = np.arange(6).reshape(2,3)
print(arr.T)

#Task9
print("Task9")
arr = np.arange(9).reshape(3,3)
arr1 = np.arange(3).reshape(1,3)
print(arr+arr1)

#Task10
print("Task10")
arr = np.arange(16).reshape(4,4)
rows = [0, 2, 3]
columns = [1, 3, 2]
print(arr[rows, columns])