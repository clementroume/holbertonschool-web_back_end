# Unittests in JS

Welcome to the **Unittests in JS** project repository. This project, part of the Holberton School curriculum, is designed to introduce you to unit and integration testing within the JavaScript/Node.js ecosystem. You will learn to ensure the quality and reliability of your code using popular testing frameworks like Mocha, Chai, and Sinon.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project guides you through the fundamental principles of testing in JavaScript. Starting with simple unit tests, you will progress to more complex scenarios, including asynchronous functions, dependency mocking, and integration testing of a web API.

The tasks cover a range of essential concepts:

- **Testing Frameworks:** Using **Mocha** as a test runner.
- **Assertion Libraries:** Practicing with Node.js's native assertions (`assert`) and a popular BDD/TDD style library (**Chai**).
- **Test Doubles:** Using **Sinon** to create spies and stubs to isolate code and simulate specific behaviors.
- **Integration Testing:** Writing tests for a small API built with **Express**, checking status codes, responses, and endpoint behavior.

Each task is designed to reinforce a key concept through hands-on practice.

---

## Project Structure

The project consists of several JavaScript scripts and test files, each corresponding to a specific task.

|Task|File(s)|Description|
|---|---|---|
|0|`0-calcul.js`, `0-calcul.test.js`|Creates a simple function and writes a basic test with Mocha and Node.js's `assert` library.|
|1|`1-calcul.js`, `1-calcul.test.js`|Upgrades the function to handle different types of operations and organizes tests with `describe`.|
|2|`2-calcul_chai.js`, `2-calcul_chai.test.js`|Rewrites the previous test suite using the `expect` syntax from the Chai assertion library.|
|3|`3-payment.js`, `utils.js`, ...|Introduces Sinon spies to verify that one function calls another correctly.|
|4|`4-payment.js`, `4-payment.test.js`|Uses Sinon stubs to replace a function, control its output, and test code behavior in isolation.|
|5|`5-payment.js`, `5-payment.test.js`|Implements hooks (`beforeEach`, `afterEach`) to manage test setup and teardown.|
|6|`6-payment_token.js`, ...|Writes a test for an asynchronous function that returns a Promise, using the `done` callback.|
|7|`7-skip.test.js`|Shows how to skip a failing test in a suite without deleting or commenting it out.|
|8|`8-api/api.js`, `8-api/api.test.js`|Creates a basic Express API and writes a first integration test to check its root endpoint.|
|9|`9-api/api.js`, `9-api/api.test.js`|Adds an endpoint with regex parameter validation and tests both valid and invalid cases.|
|10|`10-api/api.js`, `10-api/api.test.js`|Adds `GET` and `POST` endpoints, and tests deep object equality and requests with a body.|

Exporter vers Sheets

---

## Learning Objectives

At the end of this project, you will be able to explain and implement the following without the help of Google:

- How to use Mocha to write a test suite.
- How to use different assertion libraries (Node's `assert` or Chai).
- How to present long test suites for clarity.
- When and how to use spies.
- When and how to use stubs.
- What hooks are and when to use them.
- How to conduct unit testing with asynchronous functions.
- How to write integration tests with a small Node.js server.

---
