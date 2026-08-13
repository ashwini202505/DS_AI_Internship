import numpy as np
sales = np.array([
    [10, 20, 15],
    [30, 35, 60],
    [90, 20, 50],
    [15, 40, 70]
])
print("Sales Data:",sales)

print("Mean:",np.mean(sales))
print(np.mean(sales, axis=0))
print(np.mean(sales, axis=1))

print("Median:",np.median(sales))
print(np.median(sales, axis=0))
print(np.median(sales, axis=1))

print("Variance:", np.var(sales))

print("Standard Deviation:", np.std(sales))