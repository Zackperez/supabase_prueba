import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='db.ykydzxmejqirzlwbzyti.supabase.co',
                            database='postgres',
                            port=5432,
                            user='postgres',
                            password='Zacksykes.2018*')
    return conn




@app.route('/getall')
def index():
    conn = get_db_connection()
    cur = conn.cursor()


# starting the app
if __name__ == "__main__":
    app.run(port=5432, debug=True)
