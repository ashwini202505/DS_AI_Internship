import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print(np.dot(A,B))
print(np.matmul(A,B))
print(A@B)

print(A.T)
print(B.T)

print(np.linalg.det(A))
print(np.linalg.det(B))

print(np.linalg.inv(A))
print(np.linalg.inv(B))