# Arrays

## What is an Array?
An array is a collection of items stored at **contiguous memory locations**. This means they are stored right next to each other in your computer's RAM.

Imagine a row of lockers. Each locker has a number (index) and holds one item. If you know the locker number, you can find the item instantly.

### Key Characteristics
- **Fixed Size:** In most low-level languages, once you create an array, you cannot change its size.
- **Same Data Type:** Usually, all elements in an array must be of the same type (e.g., all integers).
- **Index-Based:** The first element is always at index `0`.

---

## Basic Operations & Time Complexity

| Operation | Time Complexity | Explanation |
| :--- | :--- | :--- |
| **Access** | $\mathcal{O}(1)$ | If you have the index, you jump straight to the memory location. |
| **Search** | $\mathcal{O}(n)$ | In an unsorted array, you might have to check every single element. |
| **Insertion** | $\mathcal{O}(n)$ | If you insert at the start, you have to shift all other elements to the right. |
| **Deletion** | $\mathcal{O}(n)$ | If you delete from the start, you have to shift all elements to the left to fill the gap. |

### 💡 Pro Tip: Why is Access $\mathcal{O}(1)$?
The computer calculates the location using a simple formula:
`Address = Base Address + (Index * Size of one element)`
Because this is just one multiplication and one addition, it happens instantly!

---

## Static vs. Dynamic Arrays

### 1. Static Arrays
Fixed size. You must know the size at the time of creation.
Example: `int arr[5]` in C++.

### 2. Dynamic Arrays
Can resize themselves automatically. When the array gets full, the computer creates a new, larger array and copies all the old elements into it.
Example: `list` in Python or `ArrayList` in Java.

#### How Dynamic Arrays grow (Amortized Analysis):
When a Python list fills up, it doesn't just add one spot. It usually doubles its capacity. This means resizing happens rarely, so the *average* time for an insertion is still $\mathcal{O}(1)$.

---

## Implementation in Python

```python
# Creating an array (called a 'list' in Python)
my_array = [10, 20, 30, 40, 50]

# 1. Accessing an element - O(1)
print(my_array[2]) # Output: 30

# 2. Searching for an element - O(n)
for x in my_array:
    if x == 40:
        print("Found it!")

# 3. Inserting an element - O(n)
my_array.insert(0, 5) # Inserts 5 at the beginning. All others shift right.

# 4. Deleting an element - O(n)
my_array.pop(0) # Removes the first element. All others shift left.
```

## Interview Patterns to Watch For
- **Two Pointers:** Using two indices to scan the array from different directions (e.g., finding a pair that sums to a target).
- **Sliding Window:** Maintaining a "window" of elements to find a subarray with specific properties.
- **Prefix Sums:** Pre-calculating the sum of elements up to index `i` to answer range sum queries quickly.

## Edge Cases
- **Empty Array:** Always check if the array is empty before accessing `arr[0]`.
- **Single Element Array:** Does your loop work if there is only one item?
- **Out of Bounds:** Trying to access `arr[10]` when the array only has 5 elements.
