# Web Back-End - Holberton School

Welcome to the **Web Back-End** project repository! This repository is part of the **Holberton School Full-Stack**curriculum and focuses on various programming concepts related to back-end web development.

Each directory in this repository covers a specific back-end topic, offering hands-on experience with essential tools and techniques.

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

## Description

This repository contains multiple projects that help build a strong foundation in back-end web development. Topics covered include:

- **Caching**: Implement various caching strategies in Python, focusing on cache replacement algorithms and optimizing data retrieval.
- **Personal Data Protection**: Learn how to securely handle personally identifiable information (PII), including obfuscation in logs, password encryption, and safe database practices.
- **Authentication**: Build authentication systems from scratch, starting with `Basic` authentication, progressing to cookie-based `session` authentication, and culminating in a complete user authentication service with database management.

The tasks in this repository gradually increase in complexity, providing practical scenarios to explore best practices and optimize workflows.

## Project Structure

Here’s an overview of the directories included in the repository:

|**Directory**|**Description**|
|---|---|
|`caching`|Explores implementing caching strategies such as FIFO, LIFO, LRU, MRU, and LFU in Python to optimize back-end data handling.|
|`personal_data`|Focuses on protecting personal user information by filtering PII in logs and encrypting passwords using `bcrypt`.|
|`basic_authentication`|Guides you through implementing the HTTP `Basic` authentication scheme for a simple API using Python and Flask.|
|`session_authentication`|Focuses on building a session-based authentication mechanism, managing user state with cookies and session IDs.|
|`user_authentication_service`|Builds a complete user authentication service with SQLAlchemy, including registration, login, and password reset functionalities.|

## Learning Objectives

By the end of this repository, the following concepts should be clearly understood and mastered:

### Caching

- Understand the purpose and benefits of caching systems.
- Implement various cache replacement strategies: FIFO, LIFO, LRU, MRU, and LFU.
- Build clean, testable Python code with class inheritance and method overriding.

### Personal Data Protection

- Identify Personally Identifiable Information (PII) and implement methods to protect it.
- Create custom logging filters to obfuscate sensitive data.
- Safely hash and verify passwords using the `bcrypt` library.

### Basic Authentication

- Understand the concept of authentication.
- Know what Base64 is and how to encode a string in Base64.
- Understand how `Basic` authentication works.
- How to send and use the `Authorization` HTTP header.

### Session Authentication

- Understand what session authentication means.
- Know what cookies are and how they work.
- Send and parse cookies in HTTP requests and responses.

### User Authentication Service

- Declare API routes in a Flask application.
- Get form data from an incoming request.
- Define a data model and interact with a database using SQLAlchemy.
- Understand the principles of hashing passwords for secure storage.
- Manage the complete lifecycle of a user session, from login to logout.

The combined projects in this repository are designed to support the development of core skills in secure and efficient Python back-end programming
