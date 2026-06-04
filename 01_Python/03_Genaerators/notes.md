# Generator Expressions in Python

---

# Introduction

A Generator Expression is a concise way to create generators in Python.

It is similar to a list comprehension, but instead of creating and storing all values in memory at once, it generates values one by one when needed.

This process is called **Lazy Evaluation**.

---

# Why Use Generator Expressions?

Generator expressions are useful when working with:

- Large datasets
- Large files
- Data pipelines
- Machine Learning preprocessing
- Memory optimization

Unlike lists, generators do not store all values in memory.

---

# List Comprehension vs Generator Expression

## List Comprehension

```python
squares = [x*x for x in range(5)]

print(squares)
```

### Output

```python
[0, 1, 4, 9, 16]
```

Creates the entire list in memory.

---

## Generator Expression

```python
squares = (x*x for x in range(5))

print(squares)
```

### Output

```python
<generator object ...>
```

Creates a generator object that produces values only when requested.

---

# Syntax

```python
(expression for item in iterable)
```

---

# Syntax Breakdown

Example:

```python
(x*x for x in range(5))
```

| Part | Meaning |
|--------|----------|
| `x*x` | Expression |
| `for x in` | Loop |
| `range(5)` | Iterable |

---

# Creating a Generator Expression

```python
gen = (x*x for x in range(5))

print(gen)
```

### Output

```python
<generator object ...>
```

---

# Accessing Values from Generator

Generators produce values one at a time.

Using a loop:

```python
gen = (x*x for x in range(5))

for value in gen:
    print(value)
```

### Output

```python
0
1
4
9
16
```

---

# Using next()

The `next()` function retrieves the next value from a generator.

```python
gen = (x*x for x in range(5))

print(next(gen))
print(next(gen))
print(next(gen))
```

### Output

```python
0
1
4
```

---

# Generator Exhaustion

Once all values are consumed, the generator becomes exhausted.

```python
gen = (x*x for x in range(3))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
```

### Output

```python
0
1
4
StopIteration Error
```

---

# Conditional Generator Expressions

We can add conditions using `if`.

## Syntax

```python
(expression for item in iterable if condition)
```

---

# Example — Even Numbers

```python
gen = (x for x in range(10) if x % 2 == 0)

for value in gen:
    print(value)
```

### Output

```python
0
2
4
6
8
```

---

# Example — Odd Numbers

```python
gen = (x for x in range(10) if x % 2 != 0)

for value in gen:
    print(value)
```

---

# Generator with Functions

Generator expressions can use functions.

```python
words = ["apple", "banana", "kiwi"]

lengths = (len(word) for word in words)

for value in lengths:
    print(value)
```

### Output

```python
5
6
4
```

---

# Converting Generator to List

A generator can be converted into a list.

```python
gen = (x*x for x in range(5))

result = list(gen)

print(result)
```

### Output

```python
[0, 1, 4, 9, 16]
```

---

# Converting Generator to Set

```python
gen = (x*x for x in range(5))

result = set(gen)

print(result)
```

---

# Converting Generator to Tuple

```python
gen = (x*x for x in range(5))

result = tuple(gen)

print(result)
```

---

# Memory Efficiency

Generator expressions are memory efficient because they generate values only when needed.

---

# Example

```python
numbers = [x for x in range(1000000)]
```

Creates and stores all one million values.

---

```python
numbers = (x for x in range(1000000))
```

Creates only a generator object.

---

# Memory Comparison

```python
import sys

lst = [x for x in range(1000)]
gen = (x for x in range(1000))

print(sys.getsizeof(lst))
print(sys.getsizeof(gen))
```

The generator uses significantly less memory.

---

# Lazy Evaluation

Generators calculate values only when requested.

Example:

```python
gen = (x*x for x in range(5))

print(next(gen))
```

Only the first value is generated.

The remaining values are not computed until requested.

---

# Real-World Uses

Generator expressions are heavily used in:

- Reading large files
- Processing logs
- Data pipelines
- Machine Learning preprocessing
- Streaming data
- ETL processes

---

# Example 1 — Reading Large Files

```python
lines = (line.strip() for line in open("data.txt"))
```

---

# Example 2 — NLP Preprocessing

```python
tokens = (word.lower() for word in sentence.split())
```

---

# Example 3 — Filtering Data

```python
positive = (x for x in numbers if x > 0)
```

---

# Generator Expressions vs List Comprehensions

| Feature | List Comprehension | Generator Expression |
|----------|------------------|----------------------|
| Syntax | `[]` | `()` |
| Memory Usage | High | Low |
| Execution | Immediate | Lazy |
| Speed | Slightly Faster | Slightly Slower |
| Large Data Handling | Poor | Excellent |

---

# Time Complexity

Most generator expressions:

- Time Complexity → O(n)
- Space Complexity → O(1)

Because:
- Values are generated one at a time.
- No complete collection is stored.

---

# Advantages

| Advantage | Description |
|------------|-------------|
| Memory Efficient | Uses very little memory |
| Lazy Evaluation | Generates values when needed |
| Suitable for Large Data | Handles huge datasets |
| Pythonic | Preferred for streaming data |

---

# Common Mistakes

## Mistake 1 — Trying to Reuse Exhausted Generator

```python
gen = (x for x in range(3))

list(gen)
list(gen)
```

Second call returns:

```python
[]
```

The generator is already exhausted.

---

## Mistake 2 — Expecting Random Access

Wrong:

```python
gen[0]
```

Generators do not support indexing.

---

## Mistake 3 — Forgetting Parentheses

Wrong:

```python
x*x for x in range(5)
```

Correct:

```python
(x*x for x in range(5))
```

---

# Interview Tips

## Important Concepts

Interviewers commonly ask:

- Difference between list and generator
- Memory efficiency
- Lazy evaluation
- next() function
- Generator exhaustion
- Real-world use cases

---

# Best Practice

Use generators when:

- Working with large datasets
- Reading large files
- Building data pipelines
- Memory optimization is important

Use lists when:

- You need random access
- Data size is small
- Multiple iterations are required

---

# Summary

| Concept | Syntax |
|----------|---------|
| Basic Generator | `(x for x in iterable)` |
| Conditional Generator | `(x for x in iterable if condition)` |
| next() | `next(generator)` |
| List Conversion | `list(generator)` |
| Set Conversion | `set(generator)` |
| Tuple Conversion | `tuple(generator)` |

---

# Final Notes

Generator expressions are one of the most important Python optimization techniques.

Mastering them helps in:

- Python Development
- Data Science
- Machine Learning
- ETL Pipelines
- Interview Preparation

Always remember:

**List Comprehension = Store Everything**
**Generator Expression = Generate When Needed**