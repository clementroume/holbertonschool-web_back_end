# Personal Data - Holberton School

Welcome to the **Personal Data** project repository. This project is part of the **Holberton School Full-Stack** curriculum and focuses on protecting and managing **personally identifiable information (PII)** in Python applications.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project introduces best practices for handling **personal and sensitive user data** in backend systems. It emphasizes **PII protection**, **password encryption**, and **safe logging**, simulating real-world scenarios where user privacy and data integrity are critical.

Key topics include:

- Obfuscating PII in application logs using custom logging filters
- Encrypting and verifying passwords with the `bcrypt` library
- Using environment variables to securely store credentials
- Following Python conventions for clean, documented, and type-annotated code

---

## Project Structure

The `personal_data` directory includes the following files:

| Step | File                  | Description                                                                                                     |
|------|-----------------------|-----------------------------------------------------------------------------------------------------------------|
| 0    | `filtered_logger.py`  | Implements `filter_datum()` to obfuscate PII fields in log messages using regex                                 |
| 1    | `filtered_logger.py`  | Defines `RedactingFormatter`, a custom log formatter that filters sensitive fields using `filter_datum()`       |
| 2    | `filtered_logger.py`  | Adds `get_logger()` to configure and return a logger named `"user_data"` with `RedactingFormatter`. Defines `PII_FIELDS` with 5 sensitive keys |
| 3    | `filtered_logger.py`  | Implements `get_db()` to securely connect to a MySQL database using environment variable credentials            |
| 4    | `filtered_logger.py`  | Defines a `main()` function to retrieve users from the database and log filtered user data using the logger      |
| 5    | `encrypt_password.py` | Implements `hash_password(password)` to return a salted bcrypt hash of the given password                       |
| 6    | `encrypt_password.py` | Adds `is_valid(hashed_password, password)` to check if a password matches its bcrypt hash                      |

---

## Learning Objectives

By the end of this project, you should be able to explain and implement the following:

- Identify **Personally Identifiable Information (PII)** and distinguish it from non-sensitive data
- Create a **custom logging filter** to redact PII fields in logs
- Safely **hash and verify passwords** using the `bcrypt` package
- Store and retrieve **secure credentials using environment variables**
- Follow Python best practices for:
  - Module, class, and method **documentation**
  - **Executable** and well-structured scripts
  - **Pycodestyle** compliance (v2.5)
  - **Type annotations** for all functions and methods

All Python files follow these technical specifications:

- Python version: **3.9**
- Executable with: `#!/usr/bin/env python3`
- Proper documentation for **modules**, **classes**, and **functions**
- All files are executable and end with a newline
