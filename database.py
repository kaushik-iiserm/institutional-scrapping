import sqlite3
conn = sqlite3.connect('wikipedia.db')

# cursor = conn.cursor()

# cursor.execute('''
#                CREATE TABLE WIKI (
#                    id INTEGER PRIMARY KEY,
#                    name TEXT                 
#                )
# ''')

# conn.commit()
conn.close()
print(conn)

# You can then use SQL queries to retrieve and manipulate the data as needed.