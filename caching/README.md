# Caching - Holberton School

Welcome to the **Caching** project repository. This project is part of the **Holberton School Full-Stack** curriculum and focuses on implementing various caching strategies using Python.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project introduces fundamental concepts of **caching systems** and explores multiple **cache replacement algorithms**. A caching system temporarily stores data to serve future requests more efficiently and reduce computational cost. One of the main challenges lies in determining **what to keep** and **what to discard** when storage is limited.

Several cache strategies are implemented in this project:

- A basic dictionary-based cache without size limitations
- Replacement policies including **FIFO**, **LIFO**, **LRU**, **MRU**, and **LFU**

All caching classes inherit from a common base: `BaseCaching`, which provides a shared storage dictionary and interface.

---

## Project Structure

The `caching` directory includes the following files:

| File               | Description                                                                                                                                             |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `0-basic_cache.py` | Implements a basic dictionary-based caching system with no size limit. The `put()` method adds a key-value pair; `get()` retrieves a value.             |
| `1-fifo_cache.py`  | Implements the FIFO (First-In First-Out) replacement policy. When the cache exceeds `MAX_ITEMS`, the oldest added item is discarded.                   |
| `2-lifo_cache.py`  | Implements the LIFO (Last-In First-Out) replacement policy. Discards the most recently added item when the cache exceeds `MAX_ITEMS`.                   |
| `3-lru_cache.py`   | Implements the LRU (Least Recently Used) replacement policy using `OrderedDict` to track access order and evict the least recently accessed item.       |
| `4-mru_cache.py`   | Implements the MRU (Most Recently Used) replacement policy. Discards the most recently accessed item when the cache exceeds `MAX_ITEMS`.                |
| `100-lfu_cache.py` | Implements the LFU (Least Frequently Used) replacement policy. Tracks item frequency and evicts the least used one; breaks ties using LRU strategy.     |

---

## Learning Objectives

The following concepts are covered in the scope of this project:

- Definition and purpose of **caching systems**
- Comparison of various **cache replacement strategies**, including:
  - **FIFO** (First-In First-Out)
  - **LIFO** (Last-In First-Out)
  - **LRU** (Least Recently Used)
  - **MRU** (Most Recently Used)
  - **LFU** (Least Frequently Used)
- Design considerations, limitations, and trade-offs in cache systems
- Clean and testable Python code following `pycodestyle` guidelines
- Implementation of class inheritance, method overriding, and documentation

All Python files are designed with the following specifications:

- Compatible with Python 3.9  
- Include executable script headers (`#!/usr/bin/python3`)  
- Contain module, class, and method docstrings  

---
