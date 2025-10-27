import numpy as np

arr1=np.arange(1,11)
print(sum(arr1))
print(np.prod(arr1))


arr2=np.arange(0,21)
for i in range (3,9):
    print(arr2[i])

arr3=np.arange(0,25).reshape(5,5)
result=arr3[:2,-2:]
print(result)


a=np.arange(1,5)
b=np.array([2,4,6,8])
print(a+b, a*b, np.sin(b))


arr5=np.random.randint(0,50, size=20)
mask=(arr5> 25) & (arr5<40)
print(arr5[mask])


arr6=np.arange(25).reshape(5,5)
np.fill_diagonal(arr6,0)
print(arr6*2)

arr7=np.arange(1,10).reshape(3,3)
print(arr7[1,:-1])



arr8=np.array([[1,2,3],[4,5,6]])
print(arr8.T)


arr9=np.array([[1,2,3],[4,5,6],[7,8,9]])
array9=np.array([11,12,13])
result=arr9+array9
print(result)


arr10=np.arange(16).reshape(4,4)
row_indices=[0,2,3]
column_indices=[1,3,2]

result=arr10[row_indices, column_indices]
print(result)




