import numpy as np
import random

# Task 1
a = np.arange(1, 11)
print(np.sum(a))
print(np.prod(a))

# Task 2
a = np.arange(21)
print(a[3:8])

# Task 3
a = np.arange(25).reshape(5,5)
print(a[:2, -2:])

# Task 4
a = np.array([1,2,3,4])
b = np.array([2,4,6,8])
print(a + b, a * b, np.sin(b))

# Task 5
a = np.random.randint(0, 50, size = 20)
mask = (a > 25) & (a < 40)
print(a[mask])

# Task 6
a = np.arange(25).reshape(5,5)
np.fill_diagonal(a, 0)
a = a * 2
print(a)

# Task 7
a = np.arange(1, 10).reshape(3, 3)
print(a[1, :-1])

# Task 8
a = np.array([[1,2,3],[4,5,6]])
print(a.T)

# Task 9
a = np.arange(1, 10).reshape(3,3)
b = np.array([1,2,3])
print(a + b)

# Task 10
a = np.arange(1, 17).reshape(4,4)
index = ([0,2,3],[1,3,2])
print(a[index])
