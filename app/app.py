from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Response
import sqlite3

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total number of requests')

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return "Bem-vindo à API DevLukeOps! Use /api para ver as visitas."

@app.route('/api', methods=['GET'])
def api():
    REQUEST_COUNT.inc()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS visits (id INTEGER PRIMARY KEY, count INTEGER)')
    cursor.execute('INSERT INTO visits (count) VALUES (1) ON CONFLICT(id) DO UPDATE SET count=count+1')
    result = cursor.execute('SELECT count FROM visits WHERE id = 1').fetchone()
    conn.commit()
    conn.close()
    return f"Visitas: {result['count']}"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(REQUEST_COUNT), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5110)
