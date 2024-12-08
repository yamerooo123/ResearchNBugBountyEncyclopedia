<h1>Steps to set up the environment</h1>

1. Install the following packages Think of it as a SQL CLI
 ``` 
sudo apt install iodbc iodbc-dev
sudo apt install iodbctest
sudo apt install sqlite3 libsqliteodbc
 ```
The ODBC driver we use is SQLite3. (I tried MySQL ODBC driver but it was not easy to set up lol.)

2. Configure odbcinst.ini
```
nano ~/.odbcinst.ini
```
Then paste this.
```
[SQLiteDriver]
Description = SQLite ODBC Driver
Driver = /usr/lib/x86_64-linux-gnu/odbc/libsqlite3odbc.so
```
3. Configure odbc.ini
```
nano ~/.odbc.ini
```
Then paste this(make sure you create database.db with **touch database.db** or any method you prefer).
```
[SQLiteDataSource]
Description = My SQLite Database
Driver = SQLiteDriver
Database = /path/to/your/database.db
```
4. Test IODBC with iodbctest
```
sqlite3 test.db
```
Then create a sample database.
```
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO users (name) VALUES ('Alice'), ('Bob');
.exit
```
5. Open iodbctest
```
iodbctest
```
Run the following command for SQlite3
```
DSN=SQLiteDataSource;
```
If success you will be greet with **SQL >** or something similar.

Query the table to ensure it works.
```
SELECT * FROM users;
```
