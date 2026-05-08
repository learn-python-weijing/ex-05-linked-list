# Exercise 05 — Linked List

## What you'll learn
- Building a data structure from scratch using classes
- The concept of Nodes and pointers (`next`)
- Traversal, insertion, and deletion

## Your task

A `Node` class and a `LinkedList` class skeleton are provided in `solution.py`.

Implement all the methods marked with `pass`.

## How to run the tests

```bash
pytest
```

## What is a Linked List?

Unlike a regular list (array), a linked list is a chain of **nodes**. Each node holds:
- A **value**
- A pointer to the **next** node

```
[3] -> [7] -> [12] -> [5] -> None
```

There is no direct indexing — to reach node 3, you must walk through nodes 1 and 2 first.

## Hints
- Start at `self.head` and use a `while current is not None:` loop to traverse
- To delete a node, make the previous node's `.next` skip over it
- Always handle the edge case of an empty list
