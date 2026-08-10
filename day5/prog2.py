import numpy as np
x=np.array([[2,1,1],[2,1,3]])
print(np.shape(x))
print(x.reshape(3,2))
print(x.flatten())
print(x.transpose())

a=np.array([1,2])
b=np.array([3,4])
print(np.vstack((a,b)))
print(np.hstack((a,b)))

print(np.concatenate(x))
print(np.concatenate((a,b),axis=0))