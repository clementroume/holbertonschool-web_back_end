# Web Back-End - Holberton School

Welcome to the **Web Back-End** project repository! This repository is part of the **Holberton School Full-Stack** curriculum and focuses on a wide range of programming concepts related to back-end web development in both Python and JavaScript.

Each directory in this repository covers a specific back-end topic, offering hands-on experience with essential tools and techniques for building robust, scalable, and secure applications.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This repository contains multiple projects that help build a strong foundation in back-end web development. Topics covered include:

- **Database Management**: Implementing advanced MySQL features like stored procedures, triggers, and indexes, as well as using Redis for caching and temporary data storage.
- **Authentication & Security**: Building authentication systems from scratch (`Basic`, `session`) and protecting personally identifiable information (PII) through logging filters and password encryption.
- **Queuing Systems**: Creating background job processing systems in Node.js with Kue to handle asynchronous tasks efficiently.
- **Internationalization (i18n)**: Making a Flask application multilingual and region-aware using the Flask-Babel extension.
- **Testing**: Mastering the principles of unit and integration testing in both Python (`unittest`) and JavaScript (`Mocha`, `Chai`, `Sinon`).

The tasks in this repository gradually increase in complexity, providing practical scenarios to explore best practices and optimize workflows.

---

## Project Structure

Here’s an overview of the directories included in the repository:

|**Directory**|**Description**|
|---|---|
|`basic_authentication`|Guides you through implementing the HTTP `Basic` authentication scheme for a simple API using Python and Flask.|
|`caching`|Explores implementing caching strategies such as FIFO, LIFO, LRU, MRU, and LFU in Python to optimize back-end data handling.|
|`i18n`|Focuses on internationalizing a Flask web application by managing translations, locales, and timezones with Flask-Babel.|
|`MySQL_Advanced`|Delves into advanced MySQL features including indexes, stored procedures, functions, triggers, and views for optimization and automation.|
|`personal_data`|Focuses on protecting personal user information (PII) by filtering logs, encrypting passwords with `bcrypt`, and connecting securely to a database.|
|`queuing_system_in_js`|Teaches how to implement and manage background job processing systems using Node.js, Redis, and the Kue library.|
|`redis_basic`|Introduces Redis for basic operations, implementing a simple cache with expiration and method decorators in Python.|
|`session_authentication`|Focuses on building a session-based authentication mechanism, managing user state with cookies and session IDs.|
|`unittests_and_integration_tests`|Covers unit and integration testing in Python using the `unittest` and `unittest.mock` libraries to test utilities and API clients.|
|`unittests_in_js`|Introduces testing in JavaScript using Mocha, Chai, and Sinon for unit, asynchronous, and integration tests of a Node.js API.|
|`user_authentication_service`|Builds a complete user authentication service with SQLAlchemy, including registration, login, and password reset functionalities.|

---

## Learning Objectives

By the end of this repository, the following concepts should be clearly understood and mastered:

### Advanced MySQL

- How to create tables with advanced constraints like `UNIQUE` and `ENUM`.
- How to optimize queries by adding single-column and composite indexes.
- What stored procedures, functions, views, and triggers are, and how to implement them.

### Authentication (Basic, Session & User Service)

- Understand the concepts of `Basic` and session-based authentication.
- Know how to send and use the `Authorization` HTTP header and manage cookies.
- Define a data model and interact with a database using SQLAlchemy.
- Manage the complete lifecycle of a user session, from login to logout.

### Caching

- Understand the purpose and benefits of caching systems.
- Implement various cache replacement strategies: FIFO, LIFO, LRU, MRU, and LFU.
- Build clean, testable Python code with class inheritance and method overriding.

### Internationalization (i18n)

- How to internationalize a Flask application and parametrize templates.
- Using Flask-Babel and `gettext` for translation, and managing translation catalogs.
- Inferring the correct locale and timezone based on URL parameters, user settings, or request headers.
- Localizing timestamps and dates with `pytz`.

### Personal Data Protection

- Identify Personally Identifiable Information (PII) and implement methods to protect it.
- Create custom logging filters to obfuscate sensitive data in logs.
- Safely hash and verify passwords using the `bcrypt` library.
- Store and retrieve secure credentials using environment variables.

### Queuing Systems (Node.js & Kue)

- How to use a Redis client with Node.js for basic and advanced operations (hashes, async).
- How to use Kue as a queue system to create and manage background jobs.
- How to build a basic Express app interacting with a Redis server and a job queue.

### Redis

- Using the `redis-py` Python client to communicate with a Redis server.
- Implementing a simple cache with strings, numbers, and bytes, including expiration.
- Using Python decorators to add functionality like counting and logging.
- Manipulating Redis lists (`RPUSH`, `LRANGE`).

### Unittests and Integration Tests (Python)

- The difference between unit tests and integration tests.
- Using `unittest.mock` to mock dependencies and isolate components.
- How to parameterize tests to run with different datasets.
- How to mock read-only properties and test memoization.

### Unittests in JS

- How to use Mocha, Chai, and Sinon to write test suites.
- When and how to use spies and stubs to test interactions.
- What test hooks are (`beforeEach`, `afterEach`) and when to use them.
- How to conduct unit testing with asynchronous functions and write integration tests for a Node.js server.

---
