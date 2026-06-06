# Time Complexity in Python

---

# Introduction

Time Complexity is a way to measure how the running time of an algorithm grows as the size of the input increases.

It helps us analyze and compare different algorithms and determine which solution is more efficient.

Time complexity focuses on the growth rate of an algorithm rather than the actual execution time.

---

# Why Learn Time Complexity?

Understanding time complexity helps in:

- Comparing algorithms
- Writing efficient code
- Reducing execution time
- Solving large-scale problems
- Preparing for coding interviews
- Optimizing programs

---

# Input Size

The input size is generally represented by **n**.

It refers to the number of elements or the amount of data being processed by an algorithm.

As the input size increases, the running time of the algorithm changes.

---

# Big-O Notation

Big-O notation describes the upper bound or worst-case growth rate of an algorithm.

It represents how the execution time increases as the input size increases.

---

# Common Time Complexities

| Complexity | Name |
|------------|------|
| O(1) | Constant Time |
| O(log n) | Logarithmic Time |
| O(n) | Linear Time |
| O(n log n) | Linearithmic Time |
| O(n²) | Quadratic Time |
| O(n³) | Cubic Time |
| O(2ⁿ) | Exponential Time |
| O(n!) | Factorial Time |

---

# Complexity Order

Fastest to Slowest:

```text
O(1)
↓
O(log n)
↓
O(n)
↓
O(n log n)
↓
O(n²)
↓
O(n³)
↓
O(2ⁿ)
↓
O(n!)
```

---

# O(1) — Constant Time

Constant time means that the execution time does not depend on the size of the input.

No matter how large the input becomes, the number of operations remains constant.

### Characteristics

- Fastest complexity
- Independent of input size
- Performs a fixed number of operations

---

# O(log n) — Logarithmic Time

Logarithmic time occurs when the input size is repeatedly divided into smaller parts.

As the input size grows, the number of operations increases very slowly.

### Characteristics

- Very efficient
- Common in searching algorithms
- Reduces the problem size in each step

---

# O(n) — Linear Time

Linear time means that the execution time grows proportionally with the input size.

If the input doubles, the running time approximately doubles.

### Characteristics

- Processes each element once
- Growth rate is proportional to input size
- Common in traversing arrays and lists

---

# O(n log n) — Linearithmic Time

Linearithmic time is a combination of linear and logarithmic growth.

This complexity is commonly seen in efficient sorting algorithms.

### Characteristics

- Efficient for large inputs
- Better than quadratic complexity
- Common in divide-and-conquer algorithms

---

# O(n²) — Quadratic Time

Quadratic time occurs when every element interacts with every other element.

The number of operations increases rapidly as the input size grows.

### Characteristics

- Common with nested loops
- Suitable for small inputs
- Becomes inefficient for large inputs

---

# O(n³) — Cubic Time

Cubic complexity involves three levels of processing.

The execution time increases very quickly as the input size increases.

### Characteristics

- Very expensive
- Often found in matrix-based computations
- Inefficient for large datasets

---

# O(2ⁿ) — Exponential Time

Exponential complexity doubles the number of operations with each increase in input size.

These algorithms become extremely slow even for moderate input sizes.

### Characteristics

- Very inefficient
- Common in recursive brute-force solutions
- Difficult to scale

---

# O(n!) — Factorial Time

Factorial complexity grows faster than exponential complexity.

It is one of the slowest complexities and becomes impractical very quickly.

### Characteristics

- Extremely expensive
- Common in permutation-based problems
- Suitable only for very small inputs

---

# Rules for Calculating Time Complexity

---

## Rule 1 — Ignore Constants

Constant factors do not affect the overall growth rate.

Examples:

- O(2n) becomes O(n)
- O(5n) becomes O(n)

### Reason

Big-O notation focuses on growth rate rather than exact operations.

---

## Rule 2 — Sequential Operations Add

When operations occur one after another, their complexities are added.

The dominant term is kept.

Examples:

- O(n + n) becomes O(n)
- O(n² + n) becomes O(n²)

---

## Rule 3 — Nested Operations Multiply

When one loop runs inside another, their complexities multiply.

Examples:

- O(n × n) becomes O(n²)
- O(n × log n) becomes O(n log n)

---

## Rule 4 — Keep the Dominant Term

Only the term with the highest growth rate is considered.

Examples:

- O(n² + n + 100) becomes O(n²)
- O(n log n + n) becomes O(n log n)

---

# Space Complexity

Space complexity measures the amount of memory required by an algorithm.

It tells us how memory usage changes with input size.

---

# O(1) Space Complexity

Constant memory usage.

### Characteristics

- Uses fixed memory
- Independent of input size

---

# O(n) Space Complexity

Memory usage grows proportionally with input size.

### Characteristics

- Stores additional data
- Memory increases as input increases

---

# Best Case, Average Case and Worst Case

---

## Best Case

The minimum amount of work required by an algorithm.

### Characteristics

- Fastest execution
- Most favorable scenario

---

## Average Case

The expected amount of work performed under normal conditions.

### Characteristics

- Represents typical performance
- More realistic than best case

---

## Worst Case

The maximum amount of work required by an algorithm.

### Characteristics

- Slowest execution
- Guarantees upper bound performance

---

# Important Complexities for Interviews

| Complexity | Performance |
|------------|------------|
| O(1) | Excellent |
| O(log n) | Excellent |
| O(n) | Good |
| O(n log n) | Good |
| O(n²) | Acceptable for small inputs |
| O(n³) | Slow |
| O(2ⁿ) | Very Slow |
| O(n!) | Extremely Slow |

---

# General Guidelines

- Prefer O(1) whenever possible.
- O(log n) algorithms are highly efficient.
- O(n) is acceptable for most problems.
- O(n log n) is ideal for sorting and divide-and-conquer algorithms.
- Avoid O(n²) for very large inputs.
- O(2ⁿ) and O(n!) solutions are usually impractical for large datasets.

---

# Summary

| Complexity | Description |
|------------|------------|
| O(1) | Constant Time |
| O(log n) | Logarithmic Time |
| O(n) | Linear Time |
| O(n log n) | Linearithmic Time |
| O(n²) | Quadratic Time |
| O(n³) | Cubic Time |
| O(2ⁿ) | Exponential Time |
| O(n!) | Factorial Time |

---