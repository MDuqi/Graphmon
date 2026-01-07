from CreateDB import connect_db, create_cursor, create_digimon_table, create_evolution_table, empty_tables
import csv

def find_digimon_number_by_name(cur, name):
    cur.execute('''
    SELECT Number FROM digimon WHERE Name = ?
    ''', (name,))
    result = cur.fetchone()
    return result[0] if result else None


def add_digimon(cur,number, image, name, stage, attribute):
    cur.execute('''
    INSERT INTO digimon (Number, Image, Name, Stage, Attribute)
    VALUES (?, ?, ?, ?, ?)
    ''', (number, image, name, stage, attribute))
    

def add_evolution(cur, from_number, to_number):
    cur.execute('''
    INSERT INTO evolution (FromNumber, ToNumber)
    VALUES (?, ?)
    ''', (from_number, to_number))


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


def add_all_evolutions(cur):
    with open('Digimon.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        for row in reader:
            from_number = int(row[0])
            evolutions = row[5:11]
            for evo in evolutions:
                if evo != '':
                    to_number = find_digimon_number_by_name(cur, evo)
                    if to_number:
                        add_evolution(cur, from_number, to_number)
        

if __name__ == '__main__':
    # Create database and table if they don't exist
    conn = connect_db()
    cur = create_cursor(conn)
    empty_tables(cur)
    create_digimon_table(cur)
    create_evolution_table(cur)

    # Add a single Digimon
    #add_digimon(cur, 1, None, 'Agumon', 'Rookie', 'Vaccine')  

    # Add all Digimon from csv file one by one
    add_all_digimon(cur)    

    #test find_digimon_number_by_name
    #print(find_digimon_number_by_name(cur, 'Agumon'))  # Should print 21

    # Add all evolutions from csv file
    add_all_evolutions(cur)

    conn.commit()
    conn.close()