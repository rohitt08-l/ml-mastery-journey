# Practice Problems: Time and Space Complexity

Analyze the time and space complexity for the following scenarios. Try to explain **why** you chose the complexity.

### Easy
1. **Scenario 1**: You have a list of 100 numbers and you want to print the first element. What is the time complexity?
2. **Scenario 2**: You want to print every element in a list of size $n$ using a `for` loop. What is the time complexity?
3. **Scenario 3**: You have a function that takes two numbers $a$ and $b$ and returns their sum. What is the time and space complexity?

### Medium
4. **Scenario 4**: You have a nested loop where the outer loop runs $n$ times and the inner loop runs $n$ times. What is the time complexity?
5. **Scenario 5**: You are searching for a name in a sorted phone book by opening the book in the middle, seeing if the name is in the left or right half, and repeating the process. What is the time complexity?
6. **Scenario 6**: Consider the following Python code:
   ```python
   def print_pairs(arr):
       for i in arr:
           for j in arr:
               print(i, j)
   ```
   What is the time and space complexity?

### Hard
7. **Scenario 7**: You have a recursive function that calls itself twice for every single call (like the naive Fibonacci sequence). What is the time complexity?
8. **Scenario 8**: If an algorithm has a time complexity of $\mathcal{O}(n \log n)$ and $n$ increases from 1,000 to 1,000,000, by roughly how many times does the number of operations increase?
9. **Scenario 9**: Analyze the space complexity of a recursive function that calculates the factorial of $n$ (where the recursion depth is $n$).
10. **Scenario 10**: What is the time complexity of the following code?
    ```python
    i = 1
    while i <= n:
        print(i)
        i = i * 2
    ```
