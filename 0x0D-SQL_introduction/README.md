# Project: 0x0D - SQL Introduction

## Overview
This project focuses on introducing you to the fundamentals of databases and SQL (Structured Query Language). By the end of this project, you should have a clear understanding of databases, relational databases, SQL, and the basics of MySQL. The tasks cover creating databases, performing queries, understanding DDL (Data Definition Language) and DML (Data Manipulation Language), and utilizing MySQL functions.

## Learning Objectives
- **What’s a database:** Understand the concept of a database and its significance.
- **What’s a relational database:** Grasp the concept of relational databases and their role in data organization.
- **What does SQL stand for:** Learn the meaning of SQL and its purpose in database management.
- **What’s MySQL:** Familiarize yourself with MySQL, a popular relational database management system.
- **How to create a database in MySQL:** Learn the process of creating a database using MySQL.
- **What does DDL and DML stand for:** Understand the distinction between Data Definition Language and Data Manipulation Language.
- **How to CREATE or ALTER a table:** Explore the commands for creating and altering tables in MySQL.
- **How to SELECT data from a table:** Master the art of retrieving data from tables using SQL SELECT statements.
- **How to INSERT, UPDATE, or DELETE data:** Understand the operations for modifying data within tables.
- **What are subqueries:** Learn about subqueries and their role in SQL queries.
- **How to use MySQL functions:** Explore the usage of MySQL functions for data manipulation.

## Requirements
- **Allowed editors:** vi, vim, emacs
- **Environment:** Ubuntu 20.04 LTS with MySQL 8.0 (version 8.0.25)
- **File format:** All files should end with a new line
- **SQL queries:** Should have comments just before them explaining the syntax
- **File start:** All files should start with a comment describing the task
- **SQL keywords:** Should be in uppercase (SELECT, WHERE, etc.)
- **README.md:** Mandatory, providing an overview of the project
- **File length:** Will be tested using wc

## Usage Example
```sql
-- Retrieve 3 first students in the Batch ID=3
-- Because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

## Installation
- Install MySQL 8.0 on Ubuntu 20.04 LTS using the provided commands.
- Connect to your MySQL server using `sudo mysql`.
- Use "container-on-demand" for running MySQL in a container with credentials root/root.

## Notes
- Comments for SQL files should be included to provide context and explanations.
- Follow the specified format and conventions for SQL queries.
- Refer to the provided resources for further learning.

**Important:** Avoid plagiarism, and ensure that you understand and can explain the concepts covered in this project without relying on external sources.
