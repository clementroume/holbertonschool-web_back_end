# Redis basic - Holberton School

Welcome to the **Redis basic** project repository. This project is part of the **Holberton School Full-Stack** curriculum and focuses on using Redis for basic operations and implementing a simple cache with Python.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project serves as an introduction to **Redis**, a high-performance in-memory data structure store used as a database, cache, and message broker. Throughout this project, you will learn to interact with a Redis server using the `redis-py`Python client to store, retrieve, and manage data.

Implemented features include:

- A `Cache` class for interacting with Redis.
- Storing and retrieving various data types (`str`, `bytes`, `int`, `float`).
- Decorators to count method calls and log input/output history.
- A function to display the history of calls.
- An expiring web cache for the HTML content of web pages.

---

## Project Structure

The project primarily consists of the following files:

|File|Description|
|---|---|
|`exercise.py`|Contains the `Cache` class that interacts with Redis. It implements storage (`store`) and retrieval (`get`, `get_str`, `get_int`) methods. This file also includes decorators (`count_calls`, `call_history`) to track method usage and a `replay` function to display this history.|
|`web.py`|Implements an expiring web cache. The `get_page` function fetches the HTML content of a URL, caches it in Redis with a 10-second expiration, and tracks how many times each URL is accessed.|

---

## Learning Objectives

The following concepts are covered in the scope of this project:

- Understanding the basic operations of **Redis**.
- Using the **`redis-py`** Python client to communicate with a Redis server.
- Implementing a **simple cache** with strings, numbers, and bytes.
- Handling type conversion when reading from Redis.
- Using **Python decorators** to seamlessly add functionality (counting, logging).
- Manipulating Redis lists (`RPUSH`, `LRANGE`).
- Implementing a **cache with an expiration time**.
- Writing clean, documented, and type-annotated Python code that adheres to `pycodestyle` standards.

---
