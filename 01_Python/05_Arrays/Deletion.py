"""
Deletion in Arrays

Deletion means removing an element from an array.

Deletion can be performed:

1. From the beginning
2. From the middle
3. From the end

Time Complexity:

Beginning : O(n)
Middle    : O(n)
End       : O(1)
"""

# Example array
arr = [10, 20, 30, 40, 50]

print("Original Array:")
print(arr)

# -----------------------------------------
# Delete from end
# -----------------------------------------

removed = arr.pop()

print("\nDeleted from end:", removed)
print(arr)

# -----------------------------------------
# Delete from beginning
# -----------------------------------------

removed = arr.pop(0)

print("\nDeleted from beginning:", removed)
print(arr)

# -----------------------------------------
# Delete from middle
# -----------------------------------------

removed = arr.pop(1)

print("\nDeleted from index 1:", removed)
print(arr)

# -----------------------------------------
# Remove by value
# -----------------------------------------

arr = [10, 20, 30, 40, 50]

arr.remove(30)

print("\nAfter removing value 30:")
print(arr)

# -----------------------------------------
# Delete using del keyword
# -----------------------------------------

del arr[2]

print("\nAfter deleting index 2:")
print(arr)

# -----------------------------------------
# Delete multiple elements using slicing
# -----------------------------------------

arr = [10, 20, 30, 40, 50, 60]

del arr[1:4]

print("\nAfter deleting multiple elements:")
print(arr)

# -----------------------------------------
# Clear entire array
# -----------------------------------------

arr.clear()

print("\nAfter clearing array:")
print(arr)

"""
Output:

Original Array:
[10, 20, 30, 40, 50]

Deleted from end: 50
[10, 20, 30, 40]

Deleted from beginning: 10
[20, 30, 40]

Deleted from index 1: 30
[20, 40]

After removing value 30:
[10, 20, 40, 50]

After deleting index 2:
[10, 20, 50]

After deleting multiple elements:
[10, 50, 60]

After clearing array:
[]
"""