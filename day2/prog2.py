nums = []
while True:
    n = input("Enter numbers: ")
    if n.lower() == "done":
        break
    nums.append(int(n))
print("Minimum numbers:",min(nums))
print("Maximum numbers:",max(nums))
print("Sum of numbers:",sum(nums))
print("Avg of numbers:",sum(nums)/len(nums))
print("Total length:",len(nums))
print("Sorted:",sorted(nums))