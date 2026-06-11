"""
Insertion in Arrays

Insertion means adding a new element into an array.

Insertion can be performed:

1. At the beginning
2. At the middle
3. At the end

Time Complexity:

Beginning : O(n)
Middle    : O(n)
End       : O(1) (Amortized)
"""

# Example array
arr = [10, 20, 30, 40]

print("Original Array:")
print(arr)

# -----------------------------------------
# Insert at end
# -----------------------------------------

arr.append(50)

print("\nAfter inserting at end:")
print(arr)

# -----------------------------------------
# Insert at beginning
# -----------------------------------------

arr.insert(0, 5)

print("\nAfter inserting at beginning:")
print(arr)

# -----------------------------------------
# Insert at middle
# -----------------------------------------

arr.insert(3, 25)

print("\nAfter inserting at index 3:")
print(arr)

# -----------------------------------------
# Insert multiple elements
# -----------------------------------------

arr.extend([60, 70, 80])

print("\nAfter inserting multiple elements:")
print(arr)

# -----------------------------------------
# Concatenation
# -----------------------------------------

new_elements = [90, 100]

arr = arr + new_elements

print("\nAfter concatenation:")
print(arr)

# -----------------------------------------
# Using slicing for insertion
# -----------------------------------------

arr[2:2] = [15]

print("\nAfter slicing insertion:")
print(arr)

"""
Output:

Original Array:
[10, 20, 30, 40]

After inserting at end:
[10, 20, 30, 40, 50]

After inserting at beginning:
[5, 10, 20, 30, 40, 50]

After inserting at index 3:
[5, 10, 20, 25, 30, 40, 50]
"""