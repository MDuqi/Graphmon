from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/')
def home():
    return "Welcome to the Graphmon API!"

@app.route('/<digimon_name>', methods=['GET'])
def get_digimon(digimon_name):
    conn = sqlite3.connect('../DB/digimon.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM digimon WHERE Name = ?", (digimon_name,))
    digimon = cursor.fetchone()
    print(digimon)
    conn.close()

    if digimon:
        digimon_data = {
            'Number': digimon[0],
            'Image': digimon[1],
            'Name': digimon[2],
            'Stage': digimon[3],
            'StageLevel': digimon[4],
            'Attribute': digimon[5],
            'HP': digimon[6],
            'SP': digimon[7],
            'ATK': digimon[8],
            'DEF': digimon[9],
            'INT': digimon[10],
            'SPI': digimon[11],
            'SPD': digimon[12],

        }
        return jsonify(digimon_data), 200
    else:
        return jsonify({'error': 'Digimon not found'}), 404


if __name__ == "__main__":
    
    app.run(debug=True)