import pandas as pd
names = pd.Series(["Ashwini", "Asiya", None, "Sneha", "Harini", None])
print("Original Names:",names)
print("\nAfter Filling Missing Values:",names.fillna("Unknown"))
print("\nLowercase Names:",names.str.lower())
print("\nNames containing 'a':",names.str.contains("a"))   