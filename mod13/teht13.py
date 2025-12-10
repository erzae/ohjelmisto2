# tehtävä-2

from flask import Flask, jsonify
import mariadb

app = Flask(__name__)

#tietokanta
conn = mariadb.connect(
    user="erzae",
    password="aechei6o",
    host="localhost",
    database="flight_game"
)
cursor = conn.cursor()

@app.route("/kenttä/<icao>")
def hae_kenttä(icao):
    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident = ?", (icao,))
    result = cursor.fetchone()
    if result:
        return jsonify({
            "ICAO": result[0],
            "Name": result[1],
            "Municipality": result[2]
        })
    else:
        return jsonify({"error": "Lentokenttää ei löytynyt"}), 404

if __name__ == "__main__":
    app.run(port=3000)