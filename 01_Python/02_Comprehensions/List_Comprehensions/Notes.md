# List Comprehension in Python

## Introduction

List comprehension is a concise and elegant way to create lists in Python.

Instead of using traditional loops with `append()`, Python provides list comprehensions to write cleaner and shorter code.

---

## Traditional Method

```python
numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)
```

### Output

```python
[0, 1, 2, 3, 4]
```

---

## Using List Comprehension

```python
numbers = [i for i in range(5)]

print(numbers)
```

### Output

```python
[0, 1, 2, 3, 4]
```

---

# Why Use List Comprehension

List comprehensions are widely used because they are:

- Short and clean
- Easy to read
- Faster than normal loops
- Pythonic
- Useful in Data Science and Machine Learning

---

# Basic Syntax

```python
[expression for item in iterable]
```

---

# Syntax Breakdown

Example:

```python
[x*x for x in range(5)]
```

| Part | Meaning |
|------|----------|
| `x*x` | Expression |
| `for x in` | Loop |
| `range(5)` | Iterable |

---

# Working of List Comprehension

Example:

```python
squares = [x*x for x in range(1, 6)]
```

Python performs:

```python
1 * 1 → 1
2 * 2 → 4
3 * 3 → 9
4 * 4 → 16
5 * 5 → 25
```

### Final Output

```python
[1, 4, 9, 16, 25]
```

---

# Basic Examples

## Example 1 — Squares

```python
squares = [x*x for x in range(1, 6)]

print(squares)
```

---

## Example 2 — Cubes

```python
cubes = [x**3 for x in range(1, 6)]

print(cubes)
```

---

## Example 3 — Convert to Uppercase

```python
names = ["rohit", "amit", "sneha"]

upper_names = [name.upper() for name in names]

print(upper_names)
```

---

## Example 4 — Find Length of Words

```python
words = ["apple", "banana", "kiwi"]

lengths = [len(word) for word in words]

print(lengths)
```

---

# Conditional List Comprehension

We can add conditions using `if`.

---

# Syntax

```python
[expression for item in iterable if condition]
```

---

# Example 1 — Even Numbers

```python
evens = [x for x in range(10) if x % 2 == 0]

print(evens)
```

### Output

```python
[0, 2, 4, 6, 8]
```

---

# Example 2 — Odd Numbers

```python
odds = [x for x in range(10) if x % 2 != 0]

print(odds)
```

---

# Example 3 — Numbers Greater Than 50

```python
nums = [23, 67, 12, 89, 45, 90]

greater = [x for x in nums if x > 50]

print(greater)
```

---

# If-Else in List Comprehension

We can use `if-else` inside list comprehensions.

---

# Syntax

```python
[value_if_true if condition else value_if_false for item in iterable]
```

---

# Example 1 — Positive or Negative

```python
nums = [1, -2, 3, -4]

result = ["Positive" if x > 0 else "Negative" for x in nums]

print(result)
```

---

# Example 2 — Even or Odd

```python
result = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]

print(result)
```

---

# Nested List Comprehension

Nested list comprehensions are used for working with matrices and nested lists.

---

# Example 1 — Flatten Nested List

```python
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flat = [num for row in matrix for num in row]

print(flat)
```

### Output

```python
[1, 2, 3, 4, 5, 6]
```

---

# Understanding the Order

```python
[num for row in matrix for num in row]
```

Equivalent to:

```python
for row in matrix:
    for num in row:
```

---

# Example 2 — Multiplication Table

```python
table = [[i*j for j in range(1, 6)] for i in range(1, 6)]

print(table)
```

---

# Real-World Uses

List comprehensions are heavily used in:

- Data Cleaning
- Machine Learning
- NLP
- Data Transformation
- Automation Scripts

---

## Example 1 — Lowercase Tokens

```python
tokens = [word.lower() for word in sentence.split()]
```

---

## Example 2 — Remove Empty Strings

```python
clean = [x for x in data if x != ""]
```

---

## Example 3 — Convert Data Types

```python
nums = [int(x) for x in string_numbers]
```

---

# Time Complexity

Most list comprehensions:

- Time Complexity → O(n)
- Space Complexity → O(n)

Because:
- Loop runs `n` times
- Stores `n` elements

---

# Advantages

| Advantage | Description |
|-----------|-------------|
| Cleaner Code | Less code compared to loops |
| Faster Execution | Optimized internally |
| Readable | Easy to understand |
| Pythonic | Preferred in Python |

---

# Common Mistakes

## Mistake 1 — Wrong Loop Order

Wrong:

```python
[num for num in row for row in matrix]
```

Correct:

```python
[num for row in matrix for num in row]
```

---

## Mistake 2 — Too Much Nesting

Bad Practice:

```python
[x*y if x>0 else x+1 for x in a for y in b if y%2==0]
```

Avoid writing overly complex comprehensions.

---

# Interview Tips

## Important Concepts

Interviewers commonly ask:

- List comprehension basics
- Conditional comprehensions
- Nested comprehensions
- Matrix flattening
- Matrix transpose
- Filtering problems

---

## Best Practice

Always:

1. Write normal loop first
2. Convert into comprehension
3. Dry run mentally
4. Optimize readability

---

# Summary

| Concept | Syntax |
|----------|---------|
| Basic | `[x for x in iterable]` |
| Conditional | `[x for x in iterable if condition]` |
| If-Else | `[a if cond else b for x in iterable]` |
| Nested | `[x for row in matrix for x in row]` |

---

# Final Notes

List comprehensions are one of the most important Python features.

Mastering them helps in:

- DSA
- Competitive Coding
- Data Science
- Machine Learning
- Interview Preparation

Practice is the key to mastering list comprehensions.