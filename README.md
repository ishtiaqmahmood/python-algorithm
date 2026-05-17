# Python Data Structures and Algorithms

A comprehensive collection of 120+ professional, PEP 8-compliant implementations of fundamental and advanced data structures and algorithms in Python.

## Table of Contents

- [Data Structures](#data-structures)
  - [Linked Lists](#linked-lists)
  - [Stacks](#stacks)
  - [Queues](#queues)
  - [Trees](#trees)
  - [Heaps](#heaps)
  - [Hash Tables](#hash-tables)
  - [Disjoint Set](#disjoint-set)
  - [Trie](#trie)
- [Algorithms](#algorithms)
  - [Recursion](#recursion)
  - [Search](#search)
  - [Sort](#sort)
  - [Graphs](#graphs)
  - [Dynamic Programming](#dynamic-programming)
  - [Greedy](#greedy)
  - [Backtracking](#backtracking)
  - [Strings](#strings)
  - [Bit Manipulation](#bit-manipulation)
  - [Math](#math)

## Data Structures

### Linked Lists
- **Singly Linked List**: Basic implementation.
- **Doubly Linked List**: Bidirectional links.
- **Circular Singly Linked List**: Last node points to head.
- **Circular Doubly Linked List**: Circular and bidirectional.
- **Cycle Detection**: Floyd's Cycle-Finding Algorithm.
- **Reverse Linked List**: Iterative reversal.

### Stacks
- **Stack (List-based)**: Built-in list.
- **Stack (Linked List-based)**: Linked list structure.
- **Limited Stack**: Fixed capacity.
- **Min Stack**: O(1) minimum retrieval.

### Queues
- **Queue (Linked List-based)**: Efficient operations.
- **Circular Queue**: Fixed-capacity circular buffer.
- **Queue using Stacks**: Queue implementation using two stacks.
- **Stack using Queues**: Stack implementation using a queue.
- **Deque**: Double-ended queue implementation.

### Trees
- **Binary Tree**: Fundamental binary tree with traversals.
- **Binary Search Tree (BST)**: Efficient search/insert/delete.
- **AVL Tree**: Self-balancing BST.
- **Red-Black Tree**: Balanced BST (insertion).
- **Segment Tree**: Range sum queries and updates.
- **Fenwick Tree**: Binary Indexed Tree for prefix sums.

### Heaps
- **Binary Heap**: Min and Max Heaps.
- **Priority Queue**: Implementation using `heapq`.

### Hash Tables
- **Linear Probing**: Collision resolution via linear search.
- **Chaining**: Collision resolution via linked lists.
- **Bloom Filter**: Probabilistic data structure for set membership.

### Disjoint Set
- **DSU**: Basic Union-Find.
- **DSU Path Compression**: Optimized with path compression and union by rank.

### Trie
- **Trie Implementation**: Prefix tree for string operations.

## Algorithms

### Graphs
- **BFS/DFS**: Fundamental traversals.
- **Dijkstra's Algorithm**: Shortest path in weighted graphs.
- **Bellman-Ford**: Shortest path with negative weights.
- **Floyd-Warshall**: All-pairs shortest paths.
- **Topological Sort**: Ordering of DAG vertices.
- **Cycle Detection**: Directed and Undirected graphs.
- **Bridges & Articulation Points**: Graph connectivity.
- **Strongly Connected Components**: Kosaraju's and Tarjan's algorithms.

### Dynamic Programming
- **Fibonacci**: Memoization and Tabulation.
- **LCS/LIS**: Longest Common/Increasing Subsequence.
- **Knapsack**: 0/1 Knapsack problem.
- **Edit Distance**: Minimum edit operations.
- **Coin Change**: Minimum coins for amount.
- **Matrix Chain Multiplication**: Optimal multiplication order.
- **Rod Cutting**: Maximum value from cutting a rod.
- **Egg Dropping**: Minimum trials for critical floor.
- **Word Break**: Segmenting strings into words.
- **Max Subarray Sum**: Kadane's Algorithm.
- **Min Path Sum**: Minimal path in grid.
- **Unique Paths**: Counting grid paths.
- **Subset Sum**: Checking for subset with target sum.
- **Partition Equal Subset Sum**: Splitting list into equal sum subsets.
- **Palindromes**: Longest palindromic substring/subsequence.
- **Wildcard/Regex Matching**: Pattern matching implementations.

### Greedy
- **Fractional Knapsack**: Greedy knapsack.
- **Activity Selection**: Non-overlapping activities.
- **Huffman Coding**: Data compression.
- **Job Sequencing**: Max profit with deadlines.
- **Prim's/Kruskal's**: Minimum Spanning Tree.
- **Gas Station**: Circuit completion.
- **Lemonade Change**: Greedy change providing.
- **Min Platforms**: Minimum platforms for trains.
- **Police and Thieves**: Catching maximum thieves.

### Backtracking
- **N-Queens**: Placing N queens on a board.
- **Sudoku Solver**: Solving 9x9 Sudoku.
- **Rat in a Maze**: Pathfinding in a maze.
- **Permutations/Combinations**: Generating all arrangements.
- **Subset Generation**: Power set creation.
- **M-Coloring**: Graph coloring.
- **Hamiltonian Path**: Visiting all vertices once.
- **Knight's Tour**: Knight visiting all board squares.
- **Word Search**: Finding words in a character grid.

### Strings
- **Pattern Matching**: KMP, Rabin-Karp, Z-Algorithm, Naive.
- **Manipulation**: Reversal, Anagrams, Palindrome check.
- **Common Prefix**: Longest prefix among strings.
- **Compression**: Basic string compression.
- **Group Anagrams**: Categorizing anagrams.

### Bit Manipulation
- **Basics**: Set bits count, Power of two, Odd/Even check.
- **Problems**: Single number, Reverse bits, Sum of two integers.
- **Range AND**: Bitwise AND of range.
- **Hamming Distance**: Bit difference.
- **Counting Bits**: Bits for 0 to n.
- **Subsets**: Generating subsets via bitmasking.

### Math
- **Primes**: Sieve of Eratosthenes, Prime check, Prime factorization.
- **Number Theory**: GCD, LCM, Divisors.
- **Properties**: Perfect, Armstrong, Palindrome numbers.
- **Calculations**: Fast exponentiation, Square root.

## How to Run

Most files include a `if __name__ == "__main__":` block with example usage. You can run any script directly using Python:

```bash
python3 sort/merge_sort.py
python3 graph/graph.py
python3 dynamic_programming/knapsack_01.py
```

## License

This project is open-source and available under the [MIT License](LICENSE).
