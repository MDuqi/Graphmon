from CreateDB import connect_db, create_cursor, create_table

def add_digimon(cur,number, image, name, stage, attribute):
    cur.execute('''
    INSERT INTO digimon (Number, Image, Name, Stage, Attribute)
    VALUES (?, ?, ?, ?, ?)
    ''', (number, image, name, stage, attribute))
    

if __name__ == '__main__':
    # Example usage
    conn = connect_db()
    cur = create_cursor(conn)
    create_table(cur)
    # Add Agumon as test data
    add_digimon(cur, 1, None, 'Agumon', 'Rookie', 'Vaccine')   
    conn.commit()
    conn.close()