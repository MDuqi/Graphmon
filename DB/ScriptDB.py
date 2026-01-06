import sqlite3
import csv

# Create a connection to the database
connection = sqlite3.connect('Digimon.db')

# Create cursor object
cursor = connection.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS digimon (
    Number INTEGER PRIMARY KEY AUTOINCREMENT,
    Image IMAGE NOT NULL,
    Name TEXT NOT NULL,
    Stage TEXT NOT NULL,
    Attribute TEXT NOT NULL
)''')

from pathlib import Path

with open('Digimon.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute('''
        INSERT INTO digimon (Number, Image, Name, Stage, Attribute)
        VALUES (?, ?, ?, ?, ?)
        ''', (row['Number'], row['Image'], row['Name'], row['Stage'], row['Attribute']))

# get all digimon ==============================================================
cursor.execute('SELECT * FROM digimon')
digimon = cursor.fetchall()
print(digimon)