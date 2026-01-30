# MySQL Advanced

Welcome to the **MySQL Advanced** project repository. This project is part of the **Holberton School** curriculum and is designed to deepen your understanding of advanced database management concepts in MySQL. You'll move beyond basic CRUD operations to explore database optimization, automation, and complex data manipulation.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project introduces powerful MySQL features that are essential for building robust and efficient backend systems. The tasks cover a range of advanced topics, including:

- **Database Optimization:** Creating indexes to speed up query execution.
- **Automation:** Using triggers to automatically update data in response to events.
- **Code Reusability:** Implementing stored procedures and functions to encapsulate complex logic.
- **Data Abstraction:** Using views to simplify complex queries and control data access.

Each task presents a practical problem that requires a specific SQL solution, reinforcing key concepts through hands-on practice.

---

## Project Structure

The project consists of several SQL scripts, each addressing a specific task.

|Task|File|Description|
|---|---|---|
|0|`0-uniq_users.sql`|Creates a `users` table with an `id`, a unique `email`, and a `name`.|
|1|`1-country_users.sql`|Creates a `users` table with a `country` column defined as an `ENUM` of ('US', 'CO', 'TN') with a default value.|
|2|`2-fans.sql`|Ranks country origins of bands by their total number of non-unique fans.|
|3|`3-glam_rock.sql`|Lists all "Glam rock" bands, ranked by their longevity (lifespan in years).|
|4|`4-store.sql`|Creates a trigger that decreases the quantity of an item after a new order is placed.|
|5|`5-valid_email.sql`|Creates a trigger that resets the `valid_email` attribute only when the user's `email` has been changed.|
|6|`6-bonus.sql`|Creates a stored procedure `AddBonus` that adds a new correction for a student.|
|7|`7-average_score.sql`|Creates a stored procedure `ComputeAverageScoreForUser` that calculates and stores the average score for a student.|
|8|`8-index_my_names.sql`|Creates an index `idx_name_first` on the first letter of the `name` column to optimize search queries.|
|9|`9-index_name_score.sql`|Creates a composite index `idx_name_first_score` on the first letter of `name` and the `score` column.|
|10|`10-div.sql`|Creates a function `SafeDiv` that divides two numbers, returning `0` if the second number is `0`.|
|11|`11-need_meeting.sql`|Creates a view `need_meeting` that lists all students with a score below 80 and no recent meetings.|
|12|`100-average_weighted_score.sql`|(Advanced) Creates a stored procedure `ComputeAverageWeightedScoreForUser`to calculate a user's average weighted score.|
|13|`101-average_weighted_score.sql`|(Advanced) Creates a stored procedure `ComputeAverageWeightedScoreForUsers` to compute the average weighted score for all users.|

---

## Learning Objectives

By the end of this project, you will be able to explain and implement the following without relying on external resources:

- How to create tables with advanced constraints like `UNIQUE` and `ENUM`.
- How to optimize queries by adding single-column and composite indexes.
- What stored procedures and functions are, and how to implement them in MySQL.
- What views are and how to use them to abstract underlying table structures.
- What triggers are and how to implement them to enforce business rules at the database level.

---
