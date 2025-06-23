# Basic Authentication - Holberton School

Welcome to the **Basic Authentication** project repository. This project is part of the **Holberton School Full-Stack**curriculum and focuses on understanding and implementing the Basic Authentication scheme for a simple API using Python and Flask.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project introduces the fundamentals of API authentication by guiding you through the implementation of the HTTP Basic Authentication protocol. While production systems typically rely on robust frameworks, this project builds the mechanism from scratch for educational purposes. You will learn how to handle credentials, parse HTTP headers, and protect API endpoints.

Key topics include:

- Understanding and implementing the HTTP Basic Authentication scheme.
- Handling the `Authorization` HTTP header.
- Encoding and decoding credentials using `Base64`.
- Creating a flexible and extensible authentication class structure in Python.
- Filtering requests to protect specific API endpoints in a Flask application.
- Implementing custom error handlers for `401 Unauthorized` and `403 Forbidden` responses.

---

## Project Structure

The project is built incrementally, with each task adding a new layer to the authentication system:

|Step|File(s)|Description|
|:--|:--|:--|
|0|(Project Archive)|Initial project setup from an archive, including a simple User model and a basic Flask API.|
|1|`api/v1/app.py api/v1/views/index.py`|Implements a `401 Unauthorized` error handler and a test route (`/api/v1/unauthorized`) to trigger it.|
|2|`api/v1/app.py api/v1/views/index.py`|Implements a `403 Forbidden` error handler and a test route (`/api/v1/forbidden`) to trigger it.|
|3|`api/v1/auth/auth.py`|Creates a base `Auth` class with placeholder methods (`require_auth`, `authorization_header`, `current_user`) as a template for authentication mechanisms.|
|4|`api/v1/auth/auth.py`|Implements the logic for `require_auth` to check if a given path is in a list of excluded paths, with slash tolerance.|
|5|`api/v1/app.py api/v1/auth/auth.py`|Implements `authorization_header` and uses a Flask `before_request` hook to protect all endpoints based on the `Auth` class logic.|
|6|`api/v1/app.py api/v1/auth/basic_auth.py`|Creates an empty `BasicAuth` class inheriting from `Auth`and updates the app to use it based on the `AUTH_TYPE`environment variable.|
|7|`api/v1/auth/basic_auth.py`|Implements `extract_base64_authorization_header` to parse the token from a 'Basic' authorization header.|
|8|`api/v1/auth/basic_auth.py`|Implements `decode_base64_authorization_header` to decode the Base64 token into a UTF-8 string.|
|9|`api/v1/auth/basic_auth.py`|Implements `extract_user_credentials` to split the decoded string into an `(email, password)` tuple.|
|10|`api/v1/auth/basic_auth.py`|Implements `user_object_from_credentials` to retrieve a `User` instance from the database by matching email and validating the password.|
|11|`api/v1/auth/basic_auth.py`|Overloads `current_user` in `BasicAuth` to tie all previous methods together and perform a full authentication check for a request.|
|12|`api/v1/auth/basic_auth.py`|Improves `extract_user_credentials` to correctly handle passwords that contain colon (`:`) characters.|
|13|`api/v1/auth/auth.py`|Improves `require_auth` to support wildcard matching (`*`) at the end of excluded path patterns.|

---

## Learning Objectives

By the end of this project, you should be able to explain without the help of Google:

- What authentication means.
- What Base64 is and how to encode a string in Base64.
- What Basic Authentication means.
- How to send and use the `Authorization` HTTP header.
