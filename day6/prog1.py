<<<<<<< HEAD
import numpy as np
marks=np.array([[60,70,80],[70,80,90],[70,80,60]])
print(marks)

# Mean
print(np.mean(marks))
print(marks.shape)
result=np.mean(marks,axis=1)
print(result)
print(result.shape)
Result=np.mean(marks,axis=0)
print(Result)
print(Result.shape)


# Median
print(np.median(marks))
result1=np.median(marks,axis=1)
print(result1)
Result1=np.median(marks,axis=0)
print(Result1)


# Standard deviation
print(np.std(marks))

# Variance
=======
import numpy as np
marks=np.array([[60,70,80],[70,80,90],[70,80,60]])
print(marks)

# Mean
print(np.mean(marks))
print(marks.shape)
result=np.mean(marks,axis=1)
print(result)
print(result.shape)
Result=np.mean(marks,axis=0)
print(Result)
print(Result.shape)


# Median
print(np.median(marks))
result1=np.median(marks,axis=1)
print(result1)
Result1=np.median(marks,axis=0)
print(Result1)


# Standard deviation
print(np.std(marks))

# Variance
>>>>>>> ff76e3eddbe2d96c384d51df0e77d62d8377c190
print(np.var(marks))