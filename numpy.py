import numpy as np

# NumPy task solutions --------------------------------------

# task 1
a = np.arange(1,11)
print(np.sum(a), np.prod(a))

# task 2
b = np.arange(21)
print(b[3:9])

# task 3
c = np.arange(25).reshape(5, 5)
print(c)
print(c[:2, -2:])

# task 4
d = np.array([1, 2, 3, 4])
e = np.array([2, 4, 6, 8])
print(d + e, d * e, np.sin(e))

# task 5
f = np.random.randint(0, 50, size = 20)
mask = (f > 25) & (f < 40)
print([mask])

# task 6
np.fill_diagonal(c, 0)
print(c)
print(np.where(c != 0, c * 2, 0))

# task 7
g = np.arange(1,10).reshape(3, 3)
print(g[1, :-1])

# task 8
print(g.T)

# task 9
h = np.array([2, 4, 6])
print(g + h)

# task 10
i = np.arange(16).reshape(4, 4)
rows = [0, 2, 3]
cols = [1, 3, 2]
print(i[rows, cols])







