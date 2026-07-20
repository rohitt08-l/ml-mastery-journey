# Revision: Time and Space Complexity

### 🔑 Key Takeaways
- **Time Complexity**: Measures how the number of operations grows as the input size $n$ grows.
- **Space Complexity**: Measures the extra memory used by the algorithm.
- **Big O ($\mathcal{O}$)**: Focuses on the worst-case scenario.

### 🚀 Complexity Cheat Sheet
- $\mathcal{O}(1) < \mathcal{O}(\log n) < \mathcal{O}(n) < \mathcal{O}(n \log n) < \mathcal{O}(n^2) < \mathcal{O}(2^n) < \mathcal{O}(n!)$

### ⚠️ Common Mistakes
- Confusing **Time Complexity** with actual execution time (seconds).
- Forgetting to count the space used by the **recursion stack** (call stack) in space complexity.
- Overlooking the "worst-case" and assuming the "average-case".

### 💡 Quick Tip
When you see "divided by 2" or "doubling" in each step of a loop or recursion $\rightarrow$ Think $\mathcal{O}(\log n)$.
