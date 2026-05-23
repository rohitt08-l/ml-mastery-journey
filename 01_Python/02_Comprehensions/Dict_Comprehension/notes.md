# Dictionary Comprehension in Python

---

# Introduction

Dictionary comprehension is a concise and elegant way to create dictionaries in Python.

Instead of writing traditional loops to build dictionaries, Python provides dictionary comprehensions for cleaner and shorter code.

---

# Traditional Method

```python
squares = {}

for x in range(1, 6):
    squares[x] = x * x

print(squares)
```

### Output

```python
{1:1, 2:4, 3:9, 4:16, 5:25}
```

---

# Using Dictionary Comprehension

```python
squares = {x: x*x for x in range(1, 6)}

print(squares)
```

### Output

```python
{1:1, 2:4, 3:9, 4:16, 5:25}
```

---

# Why Use Dictionary Comprehension

Dictionary comprehensions are widely used because they are:

- Short and clean
- Easy to read
- Faster than normal loops
- Pythonic
- Useful in Data Science and Machine Learning
- Helpful in frequency counting and fast lookups

---

# Basic Syntax

```python
{key:value for item in iterable}
```

---

# Syntax Breakdown

Example:

```python
{x: x*x for x in range(5)}
```

| Part | Meaning |
|------|----------|
| `x` | Key |
| `x*x` | Value |
| `for x in` | Loop |
| `range(5)` | Iterable |

---

# Working of Dictionary Comprehension

Example:

```python
squares = {x: x*x for x in range(1, 6)}
```

Python performs:

```python
1 : 1
2 : 4
3 : 9
4 : 16
5 : 25
```

### Final Output

```python
{1:1, 2:4, 3:9, 4:16, 5:25}
```

---

# Basic Examples

---

## Example 1 — Squares Dictionary

```python
squares = {x: x*x for x in range(1, 6)}

print(squares)
```

---

## Example 2 — Cubes Dictionary

```python
cubes = {x: x**3 for x in range(1, 6)}

print(cubes)
```

---

## Example 3 — Word Length Dictionary

```python
words = ["apple", "banana", "kiwi"]

lengths = {word: len(word) for word in words}

print(lengths)
```

---

## Example 4 — Uppercase Mapping

```python
names = ["rohit", "amit", "sneha"]

upper_names = {name: name.upper() for name in names}

print(upper_names)
```

---

## Example 5 — ASCII Values

```python
chars = ['a', 'b', 'c']

ascii_values = {char: ord(char) for char in chars}

print(ascii_values)
```

---

# Conditional Dictionary Comprehension

We can add conditions using `if`.

---

# Syntax

```python
{key:value for item in iterable if condition}
```

---

# Example 1 — Even Numbers and Squares

```python
evens = {x: x*x for x in range(10) if x % 2 == 0}

print(evens)
```

### Output

```python
{0:0, 2:4, 4:16, 6:36, 8:64}
```

---

# Example 2 — Odd Numbers and Cubes

```python
odds = {x: x**3 for x in range(10) if x % 2 != 0}

print(odds)
```

---

# Example 3 — Words Greater Than Length 5

```python
words = ["apple", "banana", "watermelon", "kiwi"]

result = {word: len(word) for word in words if len(word) > 5}

print(result)
```

---

# Example 4 — Positive Numbers

```python
nums = [-2, 5, -1, 7]

positive = {x: x*x for x in nums if x > 0}

print(positive)
```

---

# If-Else in Dictionary Comprehension

We can use `if-else` inside dictionary comprehensions.

---

# Syntax

```python
{key:(value_if_true if condition else value_if_false) for item in iterable}
```

---

# Example 1 — Even or Odd

```python
result = {x: ("Even" if x % 2 == 0 else "Odd") for x in range(1, 6)}

print(result)
```

---

# Example 2 — Positive or Negative

```python
nums = [1, -2, 3, -4]

result = {x: ("Positive" if x > 0 else "Negative") for x in nums}

print(result)
```

---

# Example 3 — Pass or Fail

```python
marks = [35, 67, 90, 20]

result = {mark: ("Pass" if mark >= 40 else "Fail") for mark in marks}

print(result)
```

---

# Dictionary Methods with Comprehension

---

# Using `.items()`

```python
data = {'a':1, 'b':2, 'c':3}

squared = {k: v*v for k, v in data.items()}

print(squared)
```

---

# Swapping Keys and Values

```python
data = {'a':1, 'b':2, 'c':3}

swapped = {v:k for k, v in data.items()}

print(swapped)
```

---

# Nested Dictionary Comprehension

Nested dictionary comprehensions are used for creating complex dictionary structures.

---

# Example 1 — Multiplication Table

```python
table = {x: {y: x*y for y in range(1, 6)} for x in range(1, 6)}

print(table)
```

---

# Example 2 — Nested Squares

```python
nested = {x: {y: y*y for y in range(1, 4)} for x in range(1, 4)}

print(nested)
```

---

# Real-World Uses

Dictionary comprehensions are heavily used in:

- Data Cleaning
- NLP
- Frequency Counting
- Machine Learning
- API Data Transformation
- Fast Lookups
- Feature Engineering

---

# Example 1 — Frequency Counter

```python
word = "banana"

freq = {char: word.count(char) for char in word}

print(freq)
```

---

# Example 2 — Data Type Conversion

```python
nums = ["1", "2", "3"]

result = {x: int(x) for x in nums}

print(result)
```

---

# Example 3 — Celsius to Fahrenheit

Formula:

```text
F = (9/5)C + 32
```

```python
temps = [0, 10, 20, 30]

fahrenheit = {c: (9/5)*c + 32 for c in temps}

print(fahrenheit)
```

---

# Time Complexity

Most dictionary comprehensions:

- Time Complexity → O(n)
- Space Complexity → O(n)

Because:
- Loop runs `n` times
- Stores `n` key-value pairs

---

# Advantages

| Advantage | Description |
|-----------|-------------|
| Cleaner Code | Less code compared to loops |
| Faster Execution | Optimized internally |
| Readable | Easy to understand |
| Pythonic | Preferred in Python |
| Fast Lookups | Dictionary access is efficient |

---

# Common Mistakes

---

## Mistake 1 — Duplicate Keys

```python
data = {x % 2: x for x in range(5)}

print(data)
```

Duplicate keys overwrite previous values.

---

## Mistake 2 — Overcomplicated Logic

Bad Practice:

```python
{x: x*y if x>0 else x+1 for x in a for y in b if y%2==0}
```

Avoid overly complex comprehensions.

---

# Best Practice

Always:

1. Write normal loop first
2. Convert into comprehension
3. Dry run mentally
4. Optimize readability

---

# Summary

| Concept | Syntax |
|----------|---------|
| Basic | `{k:v for x in iterable}` |
| Conditional | `{k:v for x in iterable if condition}` |
| If-Else | `{k:(a if cond else b) for x in iterable}` |
| Swap Keys/Values | `{v:k for k,v in data.items()}` |
| Nested | `{x:{y:y*y for y in range()} for x in range()}` |

---

# Final Notes

Dictionary comprehensions are one of the most important Python features.

