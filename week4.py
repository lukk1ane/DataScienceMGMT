import numpy as np
arr=np.arange(1,11)
print(np.sum(arr),np.prod(arr))
arr1=np.arange(0,21)
print(arr1[3:9])
arr2=np.arange(0,25).reshape(5,5)
print(arr2[:2][-2:])

a=np.array([1,2,3,4])
b=np.array([2,4,6,8])
print(a+b,a*b,np.sin(b))

arr3=np.random.randint(0,50,size=20)
masking=(arr3>25)&(arr3<47)
print(arr3[masking])

arr4=np.arange(25).reshape(5,5)
np.fill_diagonal(arr4,0)
res=np.where(arr4!=0,arr4*2,0)
print(res)

arr5=np.arange(1,10).reshape(3,3)
print(arr5[1][:-1])

arr6=np.arange(1,7).reshape(2,3)
print(arr6.T)