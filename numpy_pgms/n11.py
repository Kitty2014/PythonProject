import numpy as np 
a=np.array([[1,2,3],[4,5,6]])
np.save("a.npy",a)
b=np.load("a.npy")
print(b)
np.savez("ab.npz",x=a,y=b)
arr=np.load("ab.npz")
print(arr)
print (arr['x'])
print(arr['y'])