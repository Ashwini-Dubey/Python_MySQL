
# SQL Connection with Python

This repository provides an example of how to connect to a MySQL database using Python. It demonstrates how to perform basic CRUD (Create, Read, Update, Delete) operations, including creating tables, inserting data, and reading records from the database.

## Prerequisites

- **Python 3.x** installed on your machine.
- **MySQL Server** running locally or remotely.
- **MySQL Connector** for Python installed.

### Install MySQL Connector for Python
Before you start, ensure you have the MySQL connector installed:

```bash
pip install mysql-connector-python
```

## Setting Up the Database

1. **Install MySQL Server** (if you don’t have it already).
   - Download and install MySQL from https://dev.mysql.com/downloads/installer/
   - Start the MySQL service.

2. **Create a Database (`test_db`)**:
   You can use the MySQL Workbench or MySQL CLI to create the `test_db` database.

```sql
CREATE DATABASE test_db;
```

3. **Create Tables**:
   Inside the `test_db` database, create the **`users`** and **`orders`** tables.

### `users` Table Schema:
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone_number VARCHAR(15)
);
```

### `orders` Table Schema:
```sql
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_price DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Code Breakdown:

1. **Establishing Connection to MySQL Database:**
```python
db_conn = mysql.connector.connect(host='localhost', database='test_db', user='root', password='root')
```

2. **Checking Connection:**
```python
print(db_conn.is_connected())
```

3. **Creating a Cursor Object:**
```python
cursor = db_conn.cursor()
```

4. **Fetching Data from the `users` Table:**
```python
cursor.execute("Select * FROM test_db.users")
user_row = cursor.fetchone()
print(user_row[0:3])
```

5. **Fetching All Data from the `users` Table:**
```python
user_rows = cursor.fetchall()
print(user_rows[1][0])
```

6. **Fetching Data from the `orders` Table:**
```python
cursor.execute("Select * FROM test_db.orders")
order_rows = cursor.fetchall()
print(order_rows)
```

7**Closing the Database Connection:**
```python
db_conn.close()
```
