<<<<<<< HEAD
import numpy as np
A = np.array([[4, 9],
              [7, 3]])
B = np.array([[2, 6],
              [5, 1]])
print("Matrix A:",A)
print("\nMatrix B:",B)
result1 = np.dot(A, B)
print("\nMatrix Multiplication (np.dot):",result1)
print("Shape:", result1.shape)
result2 = A * B
print("\nElement-wise Multiplication (*):",result2)
print("Shape:", result2.shape)
result3 = np.dot(B, A)

print("\nAfter Swapping A and B:")
print(result3)
=======
import numpy as np
A = np.array([[4, 9],
              [7, 3]])
B = np.array([[2, 6],
              [5, 1]])
print("Matrix A:",A)
print("\nMatrix B:",B)
result1 = np.dot(A, B)
print("\nMatrix Multiplication (np.dot):",result1)
print("Shape:", result1.shape)
result2 = A * B
print("\nElement-wise Multiplication (*):",result2)
print("Shape:", result2.shape)
result3 = np.dot(B, A)

print("\nAfter Swapping A and B:")
print(result3)
>>>>>>> ff76e3eddbe2d96c384d51df0e77d62d8377c190
print("Shape:", result3.shape)