# User Authentication Service - Holberton School

Welcome to the **User Authentication Service** project repository. This project is part of the **Holberton School Full-Stack** curriculum and focuses on building a complete user authentication system from the ground up using Python, Flask, and SQLAlchemy.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project provides a hands-on approach to creating a secure and functional user authentication service. While production environments often use pre-built frameworks, this project builds each component manually for a deeper understanding of the underlying mechanics. It covers user registration, login, session management, password hashing, and password reset functionalities.

Key topics covered include:

- Defining a user data model with SQLAlchemy for database interaction.
- Abstracting database logic into a dedicated class.
- Securely hashing and verifying passwords with the `bcrypt` library.
- Implementing user registration and login workflows.
- Managing user sessions with UUIDs and HTTP cookies.
- Building a complete password reset flow, from token generation to validation.
- Developing a Flask API with endpoints for all authentication-related actions.

---

## Project Structure

The project is broken down into several key components, each building upon the last to create a full-featured service:

|File|Description|
|---|---|
|`user.py`|Defines the SQLAlchemy `User` model for the `users` database table, including id, email, and fields for session and token management.|
|`db.py`|Implements a `DB` class to abstract all database interactions, including methods to add, find, and update users.|
|`auth.py`|Contains the `Auth` class, which orchestrates all authentication logic, such as password hashing, user registration, and session management.|
|`app.py`|Sets up the Flask web application and defines all API endpoints for user interaction (`/users`, `/sessions`, `/profile`, `/reset_password`).|
|`main.py`|(Advanced) Provides an end-to-end integration test script to validate the functionality of the entire service.|

---

## Learning Objectives

By the end of this project, the following concept should be mastered:

- How to declare API routes in a Flask application.
- How to get form data from an incoming request.
- How to get and set cookies in an HTTP response.
- How to return various HTTP status codes to signify success or failure.
- How to define a data model and interact with a database using SQLAlchemy.
- The principles of hashing passwords for secure storage.
- The complete lifecycle of a user session, from login to logout.

---
