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
def create_digimon_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS digimon (
        Number INTEGER PRIMARY KEY AUTOINCREMENT,
        Image IMAGE NULL,
        Name TEXT NOT NULL,
        Stage TEXT NOT NULL,
        StageLevel INTEGER NOT NULL,
        Attribute TEXT NOT NULL,
        HP INTEGER NOT NULL,
        SP INTEGER NOT NULL,
        ATK INTEGER NOT NULL,
        DEF INTEGER NOT NULL,
        INT INTEGER NOT NULL,
        SPI INTEGER NOT NULL,
        SPD INTEGER NOT NULL
    )''')

def create_evolution_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS evolution (
        FromNumber INTEGER,
        ToNumber INTEGER,
        EvoCost INTEGER NOT NULL,
        FOREIGN KEY (FromNumber) REFERENCES digimon(Number),
        FOREIGN KEY (ToNumber) REFERENCES digimon(Number),
        PRIMARY KEY (FromNumber, ToNumber)
    )''')

def empty_tables(cursor):
    cursor.execute('DELETE FROM digimon')
    cursor.execute('DELETE FROM evolution')

def delete_tables(cursor):
    cursor.execute('DROP TABLE IF EXISTS evolution')
    cursor.execute('DROP TABLE IF EXISTS digimon')

if __name__ == '__main__':
    conn = connect_db()
    cur = create_cursor(conn)
    
    # Check if digimon table exists
    table_names = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='digimon'")
    print(table_names)
    if table_names.fetchone() is not None:
        print("Tables already exist. Deleting tables...")
        delete_tables(cur)

    print("Creating tables...")
    create_digimon_table(cur)
    create_evolution_table(cur)
      
    conn.commit()
    conn.close()

