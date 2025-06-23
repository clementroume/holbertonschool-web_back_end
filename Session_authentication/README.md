# Session Authentication - Holberton School

Welcome to the **Session Authentication** project repository. This project is part of the **Holberton School Full-Stack**curriculum and focuses on building a session-based authentication mechanism using Python and Flask.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project aims to build a complete session authentication system from scratch, building upon the concepts of a basic authentication mechanism. It explores how to manage user state across multiple requests by using session IDs stored in cookies. This project simulates real-world scenarios where persistent authentication is necessary to protect API endpoints.

Key topics include:

- Building a flexible authentication system that can be switched via environment variables.
- Using cookies to manage user sessions.
- Creating, retrieving, and destroying session IDs.
- Implementing session expiration to enhance security.
- Persisting sessions by storing them in a database.

---

## Project Structure

The project evolves across several files to incrementally build the authentication system:

| Step | File(s)                                                                               | Description                                                                                                                                          |
| :--- | :------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0    | `api/v1/app.py api/v1/views/users.py`                                              | Updates the basic authentication to support a new `GET /api/v1/users/me` endpoint to retrieve the authenticated user.                                |
| 1    | `api/v1/auth/session_auth.py api/v1/app.py`                                   | Creates an empty `SessionAuth`class and implements a mechanism to switch to this new authentication system via the `AUTH_TYPE` environment variable. |
| 2    | `api/v1/auth/session_auth.py`                                                         | Implements `create_session` to generate a unique session ID (UUID) for a `user_id` and store it in an in-memory dictionary.                          |
| 3    | `api/v1/auth/session_auth.py`                                                         | Implements `user_id_for_session_id` to retrieve a `user_id` from the in-memory stored session ID.                                                    |
| 4    | `api/v1/auth/auth.py`                                                                 | Adds the `session_cookie`method to extract the session cookie value from an HTTP request.                                                            |
| 5    | `api/v1/app.py`                                                                       | Updates the `before_request`handler to check for the presence of either an authorization header or a session cookie.                                 |
| 6    | `api/v1/auth/session_auth.py`                                                         | Overloads the `current_user`method to identify and return a `User` instance based on the request's session cookie.                                   |
| 7    | `api/v1/views/session_auth.py api/v1/views/__init__.py`                       | Creates a new `POST /api/v1/auth_session/login`view to handle user login, create a session, and set the response cookie.                             |
| 8    | `api/v1/auth/session_auth.py api/v1/views/session_auth.py`                    | Implements the logout logic with `destroy_session` and exposes a `DELETE /api/v1/auth_session/logout`endpoint.                                       |
| 9    | `api/v1/auth/session_exp_auth.py api/v1/app.py`                               | Creates `SessionExpAuth`inheriting from `SessionAuth` to add an expiration duration to sessions, configurable via `SESSION_DURATION`.                |
| 10   | `models/user_session.py api/v1/auth/session_db_auth.py api/v1/app.py` | Implements `SessionDBAuth` to store session information in a database (file) to make them persistent.                                                |

---

## Learning Objectives

By the end of this project, you should be able to explain without the help of Google:

- What authentication means.
- What session authentication means.
- What Cookies are and how they work.
- How to send Cookies in an HTTP response.
- How to parse Cookies from an HTTP request.
