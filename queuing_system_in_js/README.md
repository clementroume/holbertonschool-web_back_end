# Queuing System in JS

Welcome to the **Queuing System in JS** project repository. This project, part of the Holberton School curriculum, is designed to teach you how to implement and manage background job processing systems using Node.js, Redis, and the Kue library. You will learn to handle asynchronous tasks efficiently, ensuring your applications remain responsive and scalable.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project provides a comprehensive introduction to message queuing in JavaScript. You will start by interacting directly with a Redis server, performing basic to advanced operations. Then, you'll use Kue, a feature-rich job queue library, to create, process, and monitor background jobs. Finally, you'll integrate these concepts into a web application built with Express.

The tasks cover a range of essential concepts:

- **Redis Client:** Connecting to a Redis server from a Node.js application and handling basic data operations (strings, hashes).
- **Asynchronous Handling:** Managing asynchronous Redis commands using both callbacks and modern `async/await` syntax with promises.
- **Publisher/Subscriber:** Implementing a basic messaging system using Redis's Pub/Sub features.
- **Job Queues with Kue:** Creating job producers and consumers, and tracking job lifecycle events (creation, completion, failure, progress).
- **Integration with Express:** Building a small e-commerce API that manages product stock and seat reservations by leveraging Redis for data storage and Kue for handling asynchronous requests.

Each task builds upon the previous one, providing a solid, hands-on foundation in building robust back-end systems.

---

## Project Structure

The project consists of several JavaScript scripts, each corresponding to a specific task that explores a different aspect of Redis and Kue.

|Task|File(s)|Description|
|---|---|---|
|0|`README.md`, `dump.rdb`|Installs and runs a local Redis server, performing basic `SET`/`GET` operations via the CLI.|
|1|`0-redis_client.js`|Creates a Node.js Redis client that connects to the local server and logs connection status.|
|2|`1-redis_op.js`|Implements functions for setting and getting values in Redis using callbacks.|
|3|`2-redis_op_async.js`|Refactors the previous script's functions to use `async/await` for cleaner asynchronous code.|
|4|`4-redis_advanced_op.js`|Uses Redis hashes to store and retrieve a collection of related data (`hset`, `hgetall`).|
|5|`5-subscriber.js`, `5-publisher.js`|Implements a simple publisher/subscriber pattern where one script sends messages and another receives them.|
|6|`6-job_creator.js`|Creates a basic job and adds it to a Kue queue, logging its creation and completion status.|
|7|`6-job_processor.js`|Creates a worker script to process jobs from the queue created in the previous task.|
|8|`7-job_creator.js`|Creates multiple jobs from an array and listens for their lifecycle events (progress, completion, failure).|
|9|`7-job_processor.js`|Builds a more advanced worker that processes multiple jobs concurrently and can blacklist certain jobs.|
|10|`8-job.js`|Encapsulates the job creation logic into a single, reusable function that handles an array of jobs.|
|11|`8-job.test.js`|Writes unit tests for the job creation function using Kue's test mode and the Mocha/Chai frameworks.|
|12|`9-stock.js`|Builds an Express API to manage product stock, using Redis to store and reserve items.|
|13|`100-seat.js`|Creates an Express API for a seat reservation system, using Kue to queue reservation requests.|

Exporter vers Sheets

---

## Learning Objectives

At the end of this project, you will be able to explain and implement the following without the help of Google:

- How to run a Redis server on your machine.
- How to run simple operations with the Redis client.
- How to use a Redis client with Node JS for basic operations.
- How to store hash values in Redis.
- How to deal with async operations with Redis.
- How to use Kue as a queue system.
- How to build a basic Express app interacting with a Redis server.
- How to build a basic Express app interacting with a Redis server and queue.

---
