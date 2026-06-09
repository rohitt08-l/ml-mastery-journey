\# Arrays in Python



\---



\# Introduction



An array is a collection of elements stored in contiguous memory locations.



Arrays allow us to store multiple values of the same or different data types in a single variable.



In Python, lists are commonly used to represent arrays.



\---



\# Why Learn Arrays?



Arrays are one of the most fundamental data structures because they are used in:



\- Searching algorithms

\- Sorting algorithms

\- Dynamic Programming

\- Sliding Window techniques

\- Two Pointer problems

\- Prefix Sum problems

\- Matrix operations



Almost every data structure and algorithm problem starts with arrays.



\---



\# Characteristics of Arrays



\- Elements are stored sequentially.

\- Indexing starts from 0.

\- Supports random access.

\- Allows duplicate elements.

\- Dynamic in size (Python lists).



\---



\# Array Representation



```text

Index : 0   1   2   3   4

Value : 10  20  30  40  50

```



\---



\# Indexing



Each element is identified by its index.



\### Positive Indexing



```text

0 1 2 3 4

```



\---



\### Negative Indexing



```text

\-5 -4 -3 -2 -1

```



Negative indexing starts from the end of the array.



\---



\# Types of Arrays



\---



\## One-Dimensional Array



Stores elements in a single row.



```text

\[10, 20, 30, 40, 50]

```



\---



\## Two-Dimensional Array



Stores elements in rows and columns.



```text

\[

&#x20;\[1, 2, 3],

&#x20;\[4, 5, 6]

]

```



\---



\## Multi-Dimensional Array



Array containing multiple dimensions.



Example:



```text

3D Array

```



\---



\# Common Operations on Arrays



| Operation | Description |

|------------|-------------|

| Traversal | Visiting every element |

| Access | Retrieve an element |

| Insertion | Add a new element |

| Deletion | Remove an element |

| Searching | Find an element |

| Updating | Modify an element |

| Sorting | Arrange elements |

| Reversing | Reverse order |



\---



\# Traversal



Traversal means visiting every element in the array one by one.



\---



\# Accessing Elements



Arrays support direct access using indexes.



\### Characteristics



\- Very fast

\- Constant time operation



\### Time Complexity



```text

O(1)

```



\---



\# Insertion



Insertion means adding a new element.



Insertion may occur:



\- At the beginning

\- At the middle

\- At the end



\### Time Complexity



| Position | Complexity |

|----------|------------|

| Beginning | O(n) |

| Middle | O(n) |

| End | O(1) (Amortized) |



\---



\# Deletion



Deletion means removing an element from the array.



\### Time Complexity



| Position | Complexity |

|----------|------------|

| Beginning | O(n) |

| Middle | O(n) |

| End | O(1) |



\---



\# Searching



Searching means locating an element.



\---



\## Linear Search



Checks every element one by one.



\### Time Complexity



```text

O(n)

```



\---



\## Binary Search



Works only on sorted arrays.



\### Time Complexity



```text

O(log n)

```



\---



\# Updating Elements



Updating means changing the value stored at a specific index.



\### Time Complexity



```text

O(1)

```



\---



\# Sorting



Sorting arranges elements in ascending or descending order.



Examples:



\- Bubble Sort

\- Selection Sort

\- Insertion Sort

\- Merge Sort

\- Quick Sort



\---



\# Reversing



Reversing changes the order of elements.



Example:



```text

Original:

\[1, 2, 3, 4]



Reversed:

\[4, 3, 2, 1]

```



\---



\# Advantages of Arrays



\- Fast indexing

\- Simple implementation

\- Efficient traversal

\- Good cache locality

\- Useful for mathematical computations



\---



\# Disadvantages of Arrays



\- Insertion at beginning is expensive.

\- Deletion from middle is costly.

\- Fixed size in some languages.

\- Requires contiguous memory.



\---



\# Time Complexity Summary



| Operation | Complexity |

|------------|------------|

| Access | O(1) |

| Traversal | O(n) |

| Search | O(n) |

| Binary Search | O(log n) |

| Insert at End | O(1) |

| Insert at Beginning | O(n) |

| Delete at End | O(1) |

| Delete at Beginning | O(n) |

| Update | O(1) |



\---



\# Applications of Arrays



Arrays are used in:



\- Searching algorithms

\- Sorting algorithms

\- Dynamic Programming

\- Matrix computations

\- Image processing

\- Machine Learning

\- Graph algorithms

\- Databases



\---



\# Interview Topics Based on Arrays



After mastering arrays, the next important patterns are:



1\. Linear Search

2\. Binary Search

3\. Two Pointers

4\. Sliding Window

5\. Prefix Sum

6\. Kadane's Algorithm

7\. Matrix Problems



\---



\# Final Notes



Arrays are the foundation of Data Structures and Algorithms.



Strong understanding of arrays is essential before learning:



\- Strings

\- Hashing

\- Stack

\- Queue

\- Linked List

\- Trees

\- Graphs

\- Dynamic Programming



Mastering arrays will make advanced DSA topics much easier.

