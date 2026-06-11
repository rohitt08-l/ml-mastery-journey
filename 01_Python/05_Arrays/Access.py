"""
Accessing Elements in Arrays

Access means retrieving an element using its index.

Time Complexity: O(1)
Space Complexity: O(1)
"""

# Example array
arr = [10, 20, 30, 40, 50]

# -----------------------------------------
# Accessing first element
# -----------------------------------------

print("First element:", arr[0])

# -----------------------------------------
# Accessing last element
# -----------------------------------------

print("Last element:", arr[-1])

# -----------------------------------------
# Accessing middle element
# -----------------------------------------

middle_index = len(arr) // 2
print("Middle element:", arr[middle_index])

# -----------------------------------------
# Accessing elements using index
# -----------------------------------------

print("\nAccessing all elements using index:")

for i in range(len(arr)):
    print(f"Index {i} -> Value {arr[i]}")

# -----------------------------------------
# Negative indexing
# -----------------------------------------

print("\nNegative Indexing:")

print("arr[-1] =", arr[-1])
print("arr[-2] =", arr[-2])
print("arr[-3] =", arr[-3])

# -----------------------------------------
# Slicing
# -----------------------------------------

print("\nSlicing Examples:")

print("First 3 elements:", arr[:3])
print("Last 3 elements:", arr[-3:])
print("Middle elements:", arr[1:4])

"""
Output:

First element: 10
Last element: 50
Middle element: 30

Negative Indexing:
arr[-1] = 50
arr[-2] = 40
arr[-3] = 30
"""