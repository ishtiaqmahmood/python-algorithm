# Python Data Structures and Algorithms

A comprehensive collection of professional, PEP 8-compliant implementations of fundamental data structures and algorithms in Python.

## Table of Contents

- [Introduction](#introduction)
- [Data Structures](#data-structures)
  - [Linked Lists](#linked-lists)
  - [Stacks](#stacks)
  - [Queues](#queues)
  - [Trees](#trees)
- [Algorithms](#algorithms)
  - [Recursion](#recursion)
  - [Search](#search)
  - [Sort](#sort)
  - [Graphs](#graphs)
- [How to Run](#how-to-run)
- [License](#license)

## Introduction

This repository serves as a reference for common Data Structures and Algorithms (DSA) implemented in Python. Each implementation focuses on clarity, efficiency, and adherence to Python's best practices.

## Data Structures

### Linked Lists
- **Singly Linked List**: Basic implementation of a singly linked list with insertion and iteration.

### Stacks
- **Stack (List-based)**: Stack implementation using Python's built-in lists.
- **Stack (Linked List-based)**: Stack implementation using a linked list structure.
- **Limited Stack**: Stack with a fixed maximum capacity.

### Queues
- **Queue (List-based)**: Simple queue using a list (FIFO).
- **Queue (Linked List-based)**: Queue implementation using a linked list for efficient operations.
- **Circular Queue**: Fixed-capacity queue using a circular buffer.

### Trees
- **Binary Tree**: Fundamental binary tree with various traversal methods (Pre-order, In-order, Post-order, Level-order) and node deletion.
- **Binary Search Tree (BST)**: Specialized binary tree for efficient searching, insertion, and deletion.
- **Binary Heap**: Implementation of Min and Max Heaps.

## Algorithms

### Recursion
- **Factorial**: Computing $n!$ recursively.
- **Fibonacci**: Generating the nth Fibonacci number.
- **GCD**: Greatest Common Divisor using the Euclidean algorithm.
- **Power**: Recursive calculation of $base^{exp}$.
- **Sum of Digits**: Calculating the sum of an integer's digits.
- **Decimal to Binary**: Converting decimal numbers to binary representation.

### Search
- **Linear Search**: Sequential search through a list.
- **Binary Search**: Efficient search for sorted lists (Iterative and Recursive).
- **Ternary Search**: Divide-and-conquer search using three-way splits.

### Sort
- **Bubble Sort**: Simple comparison-based sorting.
- **Selection Sort**: Sorting by repeatedly finding the minimum element.
- **Insertion Sort**: Building the sorted list one element at a time.
- **Merge Sort**: Divide-and-conquer sorting algorithm.
- **Quick Sort**: Efficient partitioning-based sorting.
- **Bucket Sort**: Distribution-based sorting for uniform data.

### Graphs
- **Graph Traversal**: Implementations of BFS and DFS.
- **SSSP (Single Source Shortest Path)**: Finding the shortest path in unweighted graphs using BFS.
- **Dijkstra's Algorithm**: Shortest path in weighted graphs.
- **Topological Sort**: Ordering of vertices in a Directed Acyclic Graph (DAG).

## How to Run

Most files include a `if __name__ == "__main__":` block with example usage. You can run any script directly using Python:

```bash
python3 Sort/mergeSort.py
python3 Graph/Graph.py
```

## License

This project is open-source and available under the [MIT License](LICENSE).
