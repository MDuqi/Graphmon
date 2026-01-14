from CreateDB import connect_db, create_cursor, create_digimon_table, create_evolution_table, empty_tables
import os

def add_digimon_image(cur, name, image_data):
    cur.execute('''
    UPDATE digimon
    SET Image = ?
    WHERE Name = ?
    ''', (image_data, name))

def add_all_digimon_images(cur):
    image_folder = '../Scraping/digimon_images'
    for filename in os.listdir(image_folder):
        if filename.endswith('.webp'):
            name = filename[:-5]  # Remove .webp extension
            filepath = os.path.join(image_folder, filename)
            with open(filepath, 'rb') as img_file:
                image_data = img_file.read()
                add_digimon_image(cur, name, image_data)


def delete_digimon_image(cur, name):
    cur.execute('''
    UPDATE digimon
    SET Image = NULL
    WHERE Name = ?
    ''', (name,))

if __name__ == '__main__':
    conn = connect_db()
    cur = create_cursor(conn)

    # Example usage: add image data to a Digimon named 'Agumon'
    with open('../Scraping/digimon_images/Agumon.webp', 'rb') as img_file:
        image_data = img_file.read()
        add_all_digimon_images(cur)

    conn.commit()
    conn.close()

