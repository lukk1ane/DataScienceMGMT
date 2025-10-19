import numpy as np
# Task 1
arr1 = np.arange(1,11)

print(np.sum(arr1))
print(np.prod(arr1))

#Task 2
arr2 = np.arange(0,21)
arrSlice = arr2[3: 9]
print(arrSlice)

#Task 3
a = np.arange(25).reshape(5,5)
print(a[:2, -2:])

#Task 4
a = np.array([1,2,3,4])
b = np.array([2,4,6,8])
print(a + b, a * b, np.sin(b))

# Task 5
arr5 = np.random.randint(0, 50, size=20)
mask = (arr5 > 25) & (arr5 < 40)
print([mask])

#Task 6
arr6 = np.arange(25).reshape(5,5)
np.fill_diagonal(arr6, 0)
arr6 = np.where(arr6 != 0, arr6 * 2,0)
print(arr6)

#Task 7
arr7 = np.arange(1,10).reshape(3,3)
print(arr7[1,:-1])

# Task 8
arr8 = np.array([[1,2,3], [4,5,6]])
print(arr8.T)

# Task 9
arr9 = np.array([[1,2,3], [4,5,6], [7,8,9]])
arr9b = np.array([1,2,3])
print(arr9 + arr9b)

# Task 10
arr10 = np.arange(16).reshape(4,4)
rows = [0,2,3]
cols = [1,3,2]
print(arr10[rows,cols])







