# Python-SQL-Challenge

An interactive computer science quiz built using Python and MySQL. The project tests users' knowledge of Python programming and SQL through multiple-choice questions.

## Features

- **User Registration:** New users can create an account.
- **Login System:** Existing users can log in using their credentials.
- **Interactive Quiz:** 20 multiple-choice questions covering Python and SQL.
- **Score Tracking:** Quiz scores are stored in a MySQL database.
- **Leaderboard:** Displays players ranked according to their scores.
- **Password Management:** Users can change their passwords.

## Technologies Used

- Python
- MySQL
- MySQL Connector for Python

## Database Setup

Before running the program, create the required database and table in MySQL using the following commands:

```sql
CREATE DATABASE query;

USE query;

CREATE TABLE login_info (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255),
    score INT
);
```

## How to Run

1. Install Python and MySQL on your computer.
2. Install the MySQL Connector for Python:

   ```bash
   pip install mysql-connector-python
   ```

3. Set up the database using the SQL commands given above.
4. Configure your MySQL username, password and host in `main.py`.
5. Run the program:

   ```bash
   python main.py
   ```

## Contributors

- Anirudh Saraf
- Samarth Kejriwal

This project was developed collaboratively to explore Python programming, SQL and database connectivity.
