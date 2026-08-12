<<<<<<< HEAD
import pandas as pd
x=[1,2,3,4]
y=pd.Series(x)
print(y)

import numpy as np
x=np.array([2,4,6])
y=pd.Series(x)
print(y.to_string())

x={"math":80,"science":85,"english":80}
y=pd.Series(x)
print(y)
print(y[y>80])
print(y.index[2],":",y.iloc[2])

s1=pd.Series([10,20,30,40])
s2=pd.Series([10,20,30],index=['a','b','c'])
print(s1)
print(s2)

marks=[80,90,75] 
x=pd.Series(marks,index=["maths","science","hindi"])
print(x)
print(x.index.tolist())

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[0:2])
print(marks[0:3])
=======
import pandas as pd
x=[1,2,3,4]
y=pd.Series(x)
print(y)

import numpy as np
x=np.array([2,4,6])
y=pd.Series(x)
print(y.to_string())

x={"math":80,"science":85,"english":80}
y=pd.Series(x)
print(y)
print(y[y>80])
print(y.index[2],":",y.iloc[2])

s1=pd.Series([10,20,30,40])
s2=pd.Series([10,20,30],index=['a','b','c'])
print(s1)
print(s2)

marks=[80,90,75] 
x=pd.Series(marks,index=["maths","science","hindi"])
print(x)
print(x.index.tolist())

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[0:2])
print(marks[0:3])
>>>>>>> ff76e3eddbe2d96c384d51df0e77d62d8377c190
print(x[["science"]])