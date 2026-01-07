from CreateDB import connect_db, create_cursor, create_table
import csv

def add_digimon(cur,number, image, name, stage, attribute):
    cur.execute('''
    INSERT INTO digimon (Number, Image, Name, Stage, Attribute)
    VALUES (?, ?, ?, ?, ?)
    ''', (number, image, name, stage, attribute))
    

def add_all_digimon(cur):
    with open('Digimon.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        for row in reader:
            number = int(row[0])
            image = None  # Placeholder for image data
            name = row[2]
            stage = row[3]
            attribute = row[4]
            add_digimon(cur, number, image, name, stage, attribute)


if __name__ == '__main__':
    # Create database and table if they don't exist
    conn = connect_db()
    cur = create_cursor(conn)
    create_table(cur)

    # Add a single Digimon
    #add_digimon(cur, 1, None, 'Agumon', 'Rookie', 'Vaccine')  

    # Add all Digimon from csv file one by one
    add_all_digimon(cur)    

    conn.commit()
    conn.close()