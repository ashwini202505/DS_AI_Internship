<<<<<<< HEAD
import pandas as pd
marks = pd.Series(
    [80, 55, 75, 90, 60],
    index=["Math", "Science", "English", "Python", "DBMS"]
)
print("Marks:",marks)

print("\nUsing Position:")
print(marks.iloc[0])
print(marks.iloc[2])

print("\nUsing Label:")
print(marks["Math"])
print(marks["English"])

print("\nValues:")
print(marks.values)

print("\nIndex:")
print(marks.index)

print("\nMarks above 60:")
=======
import pandas as pd
marks = pd.Series(
    [80, 55, 75, 90, 60],
    index=["Math", "Science", "English", "Python", "DBMS"]
)
print("Marks:",marks)

print("\nUsing Position:")
print(marks.iloc[0])
print(marks.iloc[2])

print("\nUsing Label:")
print(marks["Math"])
print(marks["English"])

print("\nValues:")
print(marks.values)

print("\nIndex:")
print(marks.index)

print("\nMarks above 60:")
>>>>>>> ff76e3eddbe2d96c384d51df0e77d62d8377c190
print(marks[marks > 60])