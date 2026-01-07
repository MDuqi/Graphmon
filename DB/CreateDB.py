import sqlite3

# Create a connection to the database/ create the database if it doesn't exist
def connect_db():
    connection = sqlite3.connect('Digimon.db')
    return connection

# Create cursor object
def create_cursor(connection):
    cursor = connection.cursor()
    return cursor

# Create a table
def create_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS digimon (
        Number INTEGER PRIMARY KEY AUTOINCREMENT,
        Image IMAGE NULL,
        Name TEXT NOT NULL,
        Stage TEXT NOT NULL,
        Attribute TEXT NOT NULL
    )''')

if __name__ == '__main__':
    conn = connect_db()
    cur = create_cursor(conn)
    create_table(cur)
    conn.commit()

