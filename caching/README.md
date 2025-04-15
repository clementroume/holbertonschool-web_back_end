# Caching - Holberton School

Welcome to the **Caching** project repository! This project is part of the **Holberton School Full-Stack** curriculum, focusing on the implementation of various caching strategies using Python.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project introduces **caching systems** and explores how different **cache replacement algorithms** work. A caching system is a mechanism that stores data temporarily to serve future requests faster and reduce computational cost. The main challenge in caching is **what to keep** and **what to discard** when space is limited.

Throughout this project, multiple cache strategies are implemented:

- **Basic** dictionary-based cache without size limitations.
- Replacement policies such as **FIFO**, **LIFO**, **LRU**, **MRU**, and **LFU**.

All caching classes inherit from a common parent: `BaseCaching`, which provides a standard interface and storage dictionary.

---

## Project Structure

The `caching` directory includes the following files:

| File               | Description                                                                                                                                             |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `0-basic_cache.py` | Implements a basic dictionary-based caching system with no size limitation. The `put()` method adds a key-value pair, while `get()` retrieves a value.  |
| `1-fifo_cache.py`  | Implements the **FIFO** (First-In First-Out) cache replacement policy. When the cache exceeds `MAX_ITEMS`, the oldest added item is discarded.          |

---

## Learning Objectives

By the end of this project, the following concepts should be understood and applied:

- What a **caching system** is and its purpose.
- The pros and cons of different **cache replacement policies**:
  - **FIFO** (First In First Out)
  - **LIFO** (Last In First Out)
  - **LRU** (Least Recently Used)
  - **MRU** (Most Recently Used)
  - **LFU** (Least Frequently Used)
- Limitations and trade-offs in cache design.
- How to create clean, documented, and testable Python code that adheres to `pycodestyle` standards.
- Writing Python classes with proper inheritance, method overriding, and clear docstrings.

All Python files follow strict requirements, including:

- Python 3.9 compatibility
- Executable scripts with shebangs
- Fully documented modules, classes, and functions

---
