"""
Searching in Arrays

Searching means finding whether an element exists in the array.

Types of Searching:

1. Linear Search
2. Membership Operator
3. Index Method

Time Complexity:

Linear Search       : O(n)
Membership Operator : O(n)
Index Method        : O(n)
"""

# Example array
arr = [10, 20, 30, 40, 50]

target = 30

# -----------------------------------------
# Linear Search
# -----------------------------------------

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element {target} found at index {i}")
        found = True
        break

if not found:
    print("Element not found")

# -----------------------------------------
# Membership Operator
# -----------------------------------------

print("\nUsing 'in' operator:")

if 40 in arr:
    print("40 is present in the array")
else:
    print("40 is not present")

# -----------------------------------------
# Index Method
# -----------------------------------------

print("\nUsing index() method:")

position = arr.index(20)

print("20 found at index", position)

# -----------------------------------------
# Searching for all occurrences
# -----------------------------------------

arr = [10, 20, 30, 20, 50, 20]

target = 20

print("\nAll positions of 20:")

for i in range(len(arr)):
    if arr[i] == target:
        print(i)

# -----------------------------------------
# Count occurrences
# -----------------------------------------

count = arr.count(20)

print("\nNumber of times 20 appears:", count)

"""
Output:

Element 30 found at index 2

Using 'in' operator:
40 is present in the array

Using index() method:
20 found at index 1

All positions of 20:
1
3
5

Number of times 20 appears: 3
"""