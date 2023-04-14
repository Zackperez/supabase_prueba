import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

def get_db_connection():
    conn = psycopg2.connect(host='db.ykydzxmejqirzlwbzyti.supabase.co',
                            database='postgres',
                            port=5432,
                            user='postgres',
                            password='Zacksykes.2018*')
    return conn




@app.route('/getall')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM cliente')
        rv = cur.fetchall()
        conn.close()
        payload = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'cedula': result[3],'telefono': result[4]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
