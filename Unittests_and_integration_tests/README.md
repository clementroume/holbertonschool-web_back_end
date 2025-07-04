# Unittests and Integration Tests - Holberton School

Welcome to the **Unittests and Integration Tests** project repository. This project is part of the **Holberton School Full-Stack** curriculum and focuses on the principles and practices of unit and integration testing in Python.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project aims to introduce the fundamental concepts of software testing, distinguishing between **unit tests** and **integration tests**.

A **unit test** is designed to validate the behavior of an isolated unit of code, such as a function or method. It ensures that for a given set of inputs, the function produces the expected results. To guarantee isolation, external dependencies (network calls, database access, etc.) are typically "mocked" (simulated).

An **integration test**, on the other hand, aims to verify that multiple modules or components of the system work correctly together. It tests the interactions and end-to-end data flows, mocking only low-level external services.

This project utilizes key tools from the Python testing ecosystem, including the `unittest`, `unittest.mock`, and `parameterized` libraries.

---

## Project Structure

The project is organized around the following files:

|File|Description|
|---|---|
|`utils.py`|Provided module containing utility functions like `access_nested_map`, `get_json`, and the `memoize`decorator.|
|`client.py`|Provided module containing the `GithubOrgClient` class for interacting with the GitHub API.|
|`fixtures.py`|Provided module containing test data (fixtures) used for the integration tests.|
|`test_utils.py`|Contains the unit tests for the `utils.py` module. It tests the `access_nested_map` function (including exception handling), `get_json` by mocking HTTP calls, and the `memoize` decorator.|
|`test_client.py`|Contains the unit and integration tests for the `client.py` module. This file tests the `GithubOrgClient` class, using method and property patching, parameterization, and setting up full integration tests with fixtures.|

Exporter vers Sheets

---

## Learning Objectives

The following concepts are covered within the scope of this project:

- The fundamental difference between **unit tests** and **integration tests**.
- Common testing patterns, such as:
  - **Mocking** to isolate components under test.
  - **Parameterization** to run the same test with different datasets.
  - Using **fixtures** to provide a consistent baseline state or data for tests.
- Usage of Python's `unittest` framework.
- Implementation of mocks with `unittest.mock`, including `@patch` and `patch` as a context manager.
- The ability to mock read-only properties.
- Memoization and how to test it.

---
