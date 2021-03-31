import sqlite3
import _config

database = _config.DATABASE_FILE

with sqlite3.connect(database) as connection:
    cursor = connection.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                      (task_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       due_date TEXT NOT NULL,
                       priority INT NOT NULL,
                       status INT NOT NULL)''')
    
    tasks_one = ('test 1', '03/30/2021', 1, 1)
    tasks_two = ('test 2', '03/31/2021', 2, 1)
    
    cursor.execute('INSERT INTO tasks VALUES (null, ?, ?, ?, ?)', tasks_one)
    cursor.execute('INSERT INTO tasks VALUES (null, ?, ?, ?, ?)', tasks_two)