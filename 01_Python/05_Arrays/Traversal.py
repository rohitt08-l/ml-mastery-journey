"""
Traversal in Arrays

Traversal means visiting each element of an array exactly once.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Example array
arr = [10, 20, 30, 40, 50]

# -----------------------------------------
# Method 1: Traversal using for loop
# -----------------------------------------

print("Traversal using for loop:")

for element in arr:
    print(element)


# -----------------------------------------
# Method 2: Traversal using index
# -----------------------------------------

print("\nTraversal using index:")

for i in range(len(arr)):
    print(f"Index {i} -> Value {arr[i]}")


# -----------------------------------------
# Method 3: Traversal using while loop
# -----------------------------------------

print("\nTraversal using while loop:")

i = 0

while i < len(arr):
    print(arr[i])
    i += 1


# -----------------------------------------
# Method 4: Reverse Traversal
# -----------------------------------------

print("\nReverse Traversal:")

for i in range(len(arr) - 1, -1, -1):
    print(arr[i])


# -----------------------------------------
# Method 5: Traversal using enumerate()
# -----------------------------------------

print("\nTraversal using enumerate():")

for index, value in enumerate(arr):
    print(f"Index = {index}, Value = {value}")


# -----------------------------------------
# Method 6: Traversal with condition
# -----------------------------------------

print("\nEven numbers in the array:")

for num in arr:
    if num % 2 == 0:
        print(num)


# -----------------------------------------
# Method 7: Traversal and summation
# -----------------------------------------

total = 0

for num in arr:
    total += num

print("\nSum of array elements =", total)


# -----------------------------------------
# Method 8: Finding maximum element
# -----------------------------------------

maximum = arr[0]

for num in arr:
    if num > maximum:
        maximum = num

print("Maximum element =", maximum)


# -----------------------------------------
# Method 9: Finding minimum element
# -----------------------------------------

minimum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num

print("Minimum element =", minimum)


"""
Output:

Traversal using for loop:
10
20
30
40
50

Traversal using index:
Index 0 -> Value 10
Index 1 -> Value 20
Index 2 -> Value 30
Index 3 -> Value 40
Index 4 -> Value 50

Reverse Traversal:
50
40
30
20
10

Sum of array elements = 150
Maximum element = 50
Minimum element = 10
"""