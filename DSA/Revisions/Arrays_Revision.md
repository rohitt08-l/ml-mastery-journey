# Revision: Arrays

### 🔑 Key Takeaways
- **Contiguous Memory**: Arrays store elements right next to each other, which is why access is $\mathcal{O}(1)$.
- **Trade-offs**: Fast access, but slow insertion/deletion (because of shifting).
- **Dynamic Arrays**: Python lists are dynamic arrays—they resize automatically.

### ⚡ Complexity Quick-Reference
- Access: $\mathcal{O}(1)$
- Search: $\mathcal{O}(n)$
- Insert/Delete: $\mathcal{O}(n)$

### 🛠 Common Techniques
- **Two Pointers**: Scanning from both ends or at different speeds.
- **Sliding Window**: Tracking a subset of the array.
- **In-place modification**: Changing the array without using extra memory (Space: $\mathcal{O}(1)$).

### ⚠️ Common Pitfalls
- **Off-by-one errors**: Be careful with loop boundaries (e.g., using `i < len(arr)` vs `i <= len(arr)`).
- **Index Out of Bounds**: Always ensure your index is within `0` to `n-1`.
- **Thinking a List is Static**: Remember that Python lists are dynamic, but they still have $\mathcal{O}(n)$ time for inserting at the front.
