# Set Comprehension in Python

---

# Introduction

Set comprehension is a concise and elegant way to create sets in Python.

Instead of using traditional loops with `add()`, Python provides set comprehensions to write cleaner and shorter code.

---

# What is a Set?

A set in Python is:

- Unordered
- Mutable
- Stores unique values only
- Does not allow duplicates

---

# Example of a Set

```python
nums = {1, 2, 2, 3, 4}

print(nums)
```

### Output

```python
{1, 2, 3, 4}
```

Duplicate values are automatically removed.

---

# Traditional Method

```python
squares = set()

for x in range(1, 6):
    squares.add(x * x)

print(squares)
```

### Output

```python
{1, 4, 9, 16, 25}
```

---

# Using Set Comprehension

```python
squares = {x*x for x in range(1, 6)}

print(squares)
```

### Output

```python
{1, 4, 9, 16, 25}
```

---

# Why Use Set Comprehension

Set comprehensions are widely used because they are:

- Short and clean
- Easy to read
- Faster than normal loops
- Pythonic
- Useful for removing duplicates
- Helpful for fast lookup operations

---

# Basic Syntax

```python
{expression for item in iterable}
```

---

# Syntax Breakdown

Example:

```python
{x*x for x in range(5)}
```

| Part | Meaning |
|------|----------|
| `x*x` | Expression |
| `for x in` | Loop |
| `range(5)` | Iterable |

---

# Working of Set Comprehension

Example:

```python
squares = {x*x for x in range(1, 6)}
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
{1, 4, 9, 16, 25}
```

---

# Basic Examples

---

## Example 1 — Squares

```python
squares = {x*x for x in range(1, 6)}

print(squares)
```

---

## Example 2 — Cubes

```python
cubes = {x**3 for x in range(1, 6)}

print(cubes)
```

---

## Example 3 — Unique Characters

```python
word = "banana"

chars = {char for char in word}

print(chars)
```

### Output

```python
{'b', 'a', 'n'}
```

---

## Example 4 — Convert to Uppercase

```python
names = ["rohit", "amit", "rohit"]

upper = {name.upper() for name in names}

print(upper)
```

---

## Example 5 — ASCII Values

```python
chars = ['a', 'b', 'c']

ascii_values = {ord(char) for char in chars}

print(ascii_values)
```

---

# Conditional Set Comprehension

We can add conditions using `if`.

---

# Syntax

```python
{expression for item in iterable if condition}
```

---

# Example 1 — Even Numbers

```python
evens = {x for x in range(10) if x % 2 == 0}

print(evens)
```

### Output

```python
{0, 2, 4, 6, 8}
```

---

# Example 2 — Odd Numbers

```python
odds = {x for x in range(10) if x % 2 != 0}

print(odds)
```

---

# Example 3 — Positive Numbers

```python
nums = [-2, 5, -1, 7]

positive = {x for x in nums if x > 0}

print(positive)
```

---

# Example 4 — Vowels from String

```python
word = "education"

vowels = {char for char in word if char in "aeiou"}

print(vowels)
```

---

# Example 5 — Remove Duplicates

```python
nums = [1,2,2,3,4,4,5]

unique = {x for x in nums}

print(unique)
```

---

# Set Operations

Sets support mathematical operations.

---

# Union

Combines all unique elements.

```python
a = {1,2,3}
b = {3,4,5}

print(a | b)
```

### Output

```python
{1,2,3,4,5}
```

---

# Intersection

Returns common elements.

```python
a = {1,2,3}
b = {3,4,5}

print(a & b)
```

### Output

```python
{3}
```

---

# Difference

Returns elements present in first set but not second.

```python
a = {1,2,3}
b = {3,4,5}

print(a - b)
```

### Output

```python
{1,2}
```

---

# Nested Set Comprehension

Nested comprehensions can also be used with sets.

---

# Example — Flatten Nested List

```python
matrix = [
    [1,2],
    [3,4],
    [5,6]
]

flat = {num for row in matrix for num in row}

print(flat)
```

### Output

```python
{1,2,3,4,5,6}
```

---

# Real-World Uses

Set comprehensions are heavily used in:

- Duplicate Removal
- Data Cleaning
- NLP
- Machine Learning
- Fast Lookup Operations
- Graph Algorithms
- Feature Engineering

---

# Example 1 — Unique Words

```python
sentence = "apple banana apple orange banana"

words = {word for word in sentence.split()}

print(words)
```

---

# Example 2 — Lowercase Tokens

```python
tokens = {word.lower() for word in sentence.split()}
```

---

# Example 3 — Remove Duplicate Records

```python
data = [1,2,2,3,4,4,5]

unique = {x for x in data}
```

---

# Time Complexity

Most set comprehensions:

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
| Removes Duplicates | Stores only unique values |
| Fast Lookup | Membership checking is efficient |

---

# Common Mistakes

---

## Mistake 1 — Expecting Order

Sets are unordered.

```python
nums = {3,1,2}

print(nums)
```

Order may vary.

---

## Mistake 2 — Duplicate Elements

```python
nums = {1,1,1,2,2,3}

print(nums)
```

Duplicates are removed automatically.

---

## Mistake 3 — Using Mutable Types

Lists cannot be stored inside sets.

Wrong:

```python
data = {[1,2], [3,4]}
```

This causes an error.

---

# Interview Tips

---

# Important Concepts

Interviewers commonly ask:

- Duplicate removal
- Set operations
- Fast lookup problems
- Unique element extraction
- Intersection problems

---

# Best Practice

Always:

1. Write normal loop first
2. Convert into set comprehension
3. Dry run mentally
4. Optimize readability

---

# Summary

| Concept | Syntax |
|----------|---------|
| Basic | `{x for x in iterable}` |
| Conditional | `{x for x in iterable if condition}` |
| Nested | `{x for row in matrix for x in row}` |
| Union | `a | b` |
| Intersection | `a & b` |
| Difference | `a - b` |

---

# Final Notes

Set comprehensions are one of the most important Python features.

Mastering them helps in:

- DSA
- Competitive Coding
- Data Science
- Machine Learning
- Interview Preparation

Practice is the key to mastering set comprehensions.