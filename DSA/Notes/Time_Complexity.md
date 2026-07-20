# Time and Space Complexity

## What is Complexity?
In simple terms, complexity is a way to measure how "expensive" an algorithm is. When we write code, we want it to run as fast as possible (Time) and use as little memory as possible (Space).

### 1. Time Complexity
Time complexity is **not** the actual time in seconds (because different computers have different speeds). Instead, it is the number of operations an algorithm performs relative to the size of the input (usually denoted as `n`).

#### Big O Notation $\mathcal{O}(\cdot)$
We use Big O notation to describe the **worst-case scenario**. It tells us: "In the worst case, this algorithm will not take more than this much time."

**Common Time Complexities (from fastest to slowest):**

- $\mathcal{O}(1)$ - **Constant Time**: The time stays the same regardless of the input size. (Example: Accessing an element in an array by index).
- $\mathcal{O}(\log n)$ - **Logarithmic Time**: The input size is reduced by half in each step. (Example: Binary Search).
- $\mathcal{O}(n)$ - **Linear Time**: The time grows proportionally to the input size. (Example: A single loop through an array).
- $\mathcal{O}(n \log n)$ - **Linearithmic Time**: Common in efficient sorting algorithms. (Example: Merge Sort, Quick Sort).
- $\mathcal{O}(n^2)$ - **Quadratic Time**: Time grows as the square of the input size. (Example: Nested loops).
- $\mathcal{O}(2^n)$ - **Exponential Time**: Time doubles with each addition to the input. (Example: Simple recursive Fibonacci).
- $\mathcal{O}(n!)$ - **Factorial Time**: The slowest growth. (Example: Generating all permutations of a string).

### 2. Space Complexity
Space complexity measures the total amount of extra memory an algorithm needs to run.

- **Auxiliary Space**: The extra space used by the algorithm (excluding the input space).
- **Total Space**: Input space + Auxiliary space.

#### Example in Python:
```python
def find_sum(n):
    total = 0              # O(1) space: just one variable
    for i in range(n):     # O(n) time: loop runs n times
        total += i
    return total
```
- **Time Complexity**: $\mathcal{O}(n)$
- **Space Complexity**: $\mathcal{O}(1)$

---

## Interview Patterns & Tips
- **Single Loop** $\rightarrow$ usually $\mathcal{O}(n)$
- **Nested Loops** $\rightarrow$ usually $\mathcal{O}(n^2)$ or $\mathcal{O}(n \times m)$
- **Dividing by 2 in each step** $\rightarrow$ usually $\mathcal{O}(\log n)$
- **Recursion** $\rightarrow$ look at the depth of the recursion tree and the work done at each level.

## Edge Cases to Consider
- **Empty Input**: What happens if $n = 0$?
- **Single Element**: What happens if $n = 1$?
- **Huge Input**: Will the $\mathcal{O}(n^2)$ approach time out if $n = 10^5$? (Usually, $10^8$ operations per second is the limit for most online judges).
