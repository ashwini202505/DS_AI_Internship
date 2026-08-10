marks=[90,80,70,75]
new_marks=[]
for x in marks:
    new_marks.append(x+5)
    print(new_marks)


import numpy as np
marks=np.array([90,80,70,75])
Result=marks+5
print(Result)

x=np.array([[10,20,30],
           [40,50,60],
           [70,80,90]])
y=np.array([5,10,5])
z=np.array([[5],[10],[5]])
print(x+y)
print(x+z)