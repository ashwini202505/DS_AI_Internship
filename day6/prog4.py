<<<<<<< HEAD
import pandas as pd
scores=pd.Series([45,67,89,34,90])
passed=scores[scores>60]
print(passed)

data=pd.Series([10,None,30,None])
print(data.isnull())
=======
import pandas as pd
scores=pd.Series([45,67,89,34,90])
passed=scores[scores>60]
print(passed)

data=pd.Series([10,None,30,None])
print(data.isnull())
>>>>>>> ff76e3eddbe2d96c384d51df0e77d62d8377c190
print(data.fillna(0))