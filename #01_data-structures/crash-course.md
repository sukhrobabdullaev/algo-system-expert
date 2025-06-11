# Crash Course: Data Structures

## What Are Data Structures?

Data structures are ways to organize and store data in a computer so it can be accessed and modified efficiently. They are fundamental to writing efficient algorithms and solving complex problems.

---

## Types of Data Structures

### 1. **Linear Data Structures**

- **Array**: A collection of elements stored at contiguous memory locations.
  - Example: `[1, 2, 3, 4]`
  - Operations: Access (O(1)), Insert/Delete (O(n))
- **Linked List**: A sequence of nodes where each node points to the next.
  - Types: Singly Linked List, Doubly Linked List
  - Operations: Insert/Delete (O(1) at head), Search (O(n))
- **Stack**: A collection following LIFO (Last In, First Out).
  - Operations: Push, Pop, Peek (all O(1))
- **Queue**: A collection following FIFO (First In, First Out).
  - Types: Simple Queue, Circular Queue, Priority Queue
  - Operations: Enqueue, Dequeue (O(1))

### 2. **Non-Linear Data Structures**

- **Tree**: A hierarchical structure with nodes.
  - Types: Binary Tree, Binary Search Tree, AVL Tree, Heap
  - Operations: Insert/Delete/Search (O(log n) for balanced trees)
- **Graph**: A set of nodes (vertices) connected by edges.
  - Types: Directed, Undirected, Weighted, Unweighted
  - Representations: Adjacency Matrix, Adjacency List
  - Operations: BFS, DFS (O(V + E))

---

## Key Concepts

### 1. **Hashing**

- **Hash Table**: Stores key-value pairs for fast lookups.
  - Operations: Insert/Search/Delete (O(1) average, O(n) worst-case)
  - Example: Dictionary in Python

### 2. **Sorting and Searching**

- Sorting Algorithms: Bubble Sort, Merge Sort, Quick Sort
- Searching Algorithms: Binary Search (O(log n)), Linear Search (O(n))

### 3. **Big-O Notation**

- Describes the time and space complexity of algorithms.
  - Common Complexities: O(1), O(log n), O(n), O(n^2)

---

## Applications of Data Structures

- **Arrays**: Used in dynamic programming, caching.
- **Stacks**: Used in parsing expressions, backtracking.
- **Queues**: Used in scheduling, breadth-first search.
- **Trees**: Used in databases, file systems.
- **Graphs**: Used in social networks, shortest path algorithms.

---

## Tips for Learning Data Structures

1. Start with basic structures like arrays and linked lists.
2. Practice implementing each structure from scratch.
3. Solve problems on platforms like LeetCode, HackerRank, or Codeforces.
4. Understand the trade-offs between time and space complexity.

---

## Conclusion

Mastering data structures is essential for efficient problem-solving and algorithm design. Focus on understanding their use cases and practice regularly to build a strong foundation.
