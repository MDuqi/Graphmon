from CreateDB import connect_db, create_cursor

def change_digimon_name(cur, old_name, new_name):
    cur.execute('''
    UPDATE digimon
    SET Name = ?
    WHERE Name = ?
    ''', (new_name, old_name))
    print(f"Changed Digimon name from '{old_name}' to '{new_name}'.")


if __name__ == '__main__':
    conn = connect_db()
    cur = create_cursor(conn)

    # Example usage: Change Digimon name from 'Hackmon' to 'Huckmon'
    change_digimon_name(cur, 'Hackmon', 'Huckmon')
    
    conn.commit()
    conn.close()