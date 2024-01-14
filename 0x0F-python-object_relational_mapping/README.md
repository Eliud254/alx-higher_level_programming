# Python ORM Project: Database Connectivity with MySQL and SQLAlchemy

## Project Overview:

This project is an exciting journey into the intersection of Python programming and databases, specifically focusing on Object-Relational Mapping (ORM). The primary goal is to seamlessly connect Python to a MySQL database using the MySQLdb module for executing SQL queries in the first part. The second part introduces the power of SQLAlchemy, an ORM that liberates developers from the intricacies of SQL, making the focus on Python code rather than database storage details.

## Prerequisites:

Before diving into the project, ensure your MySQL server is version 8.0. Refer to the guide "How to install MySQL 8.0 in Ubuntu 20.04" to set up your environment properly.

## Project Objectives:

1. **MySQL Connectivity with MySQLdb:**
   - Establish a connection to a MySQL database using MySQLdb.
   - Execute SQL queries seamlessly within Python code.

2. **Introduction to SQLAlchemy ORM:**
   - Implement SQLAlchemy, an Object-Relational Mapper (ORM).
   - Understand the abstraction of storage, focusing on Python code rather than SQL queries.
   - Experience the flexibility of changing storage without rewriting the entire project.

## Code Comparison:

### Without ORM:
```python
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

### With SQLAlchemy ORM:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, State  # Import your SQLAlchemy models

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
```

## Getting Started:

1. Clone this repository to your local machine.
2. Set up your MySQL server as per the provided guide.
3. Review the code examples and project structure.
4. Dive into the MySQLdb and SQLAlchemy sections, focusing on Pythonic interactions with databases.
5. Experiment with the provided code, and don't hesitate to explore the ORM syntax.

## Tips:

- **Syntax Challenges:**
  - ORM syntax can be challenging initially. Start coding without reading the entire documentation. Jump in and explore as you encounter difficulties.
  
- **Tutorials:**
  - Read tutorials on MySQLdb and SQLAlchemy to enhance your understanding.

## Conclusion:

Embark on this project to bridge the gap between databases and Python seamlessly. The skills gained in MySQLdb and SQLAlchemy will empower you to interact with databases effortlessly, opening doors to flexible and efficient data management. Happy coding!
