from CreateDB import connect_db, create_cursor, create_digimon_table, create_evolution_table, empty_tables
import csv

def find_digimon_number_by_name(cur, name):
    cur.execute('''
    SELECT Number FROM digimon WHERE Name = ?
    ''', (name,))
    result = cur.fetchone()
    return result[0] if result else None

def get_stage_level(stage):
    stage_levels = {
        'In-Training I': 1,
        'In-Training II': 2,
        'Rookie': 3,
        'Champion': 4,
        'Ultimate': 5,
        'Mega': 6,
        'Mega+': 7,
        'Armor': 8,
        'Human Hybrid': 9,
        'Beast Hybrid': 10,
        'Fusion Hybrid': 11,
        'Golden Armor': 12,
        'Transcendent Hybrid': 13
    }
    return stage_levels.get(stage, 0)  # Return 0 if stage not found


def add_digimon(cur,number, image, name, stage, stage_level, attribute):
    cur.execute('''
    INSERT INTO digimon (Number, Image, Name, Stage, StageLevel, Attribute, HP, SP, ATK, DEF, INT, SPI, SPD)
    VALUES (?, ?, ?, ?, ?, ?, 0, 0, 0, 0, 0, 0, 0)
    ''', (number, image, name, stage, stage_level, attribute))


def add_evolution(cur, from_number, to_number):
    cur.execute('''
    INSERT INTO evolution (FromNumber, ToNumber, EvoCost)
    VALUES (?, ?, 0)
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
            stage_level = get_stage_level(stage)
            attribute = row[4]
            add_digimon(cur, number, image, name, stage, stage_level, attribute)


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
    
    create_digimon_table(cur)
    create_evolution_table(cur)
    empty_tables(cur)  # Clear existing data in tables

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