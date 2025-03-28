from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import sqlite3

app = Flask(__name__)

# Métricas do Prometheus
REQUEST_COUNT = Counter('request_count', 'Total number of requests')

# Conexão com o banco SQLite
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota para home
@app.route('/')
def home():
    return "Bem-vindo à API DevLukeOps! Use /api para ver as visitas."

# Rota para a API
@app.route('/api', methods=['GET'])
def api():
    REQUEST_COUNT.inc()  # Incrementa o contador de requisições
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS visits (id INTEGER PRIMARY KEY, count INTEGER)')
    cursor.execute('INSERT OR IGNORE INTO visits (id, count) VALUES (1, 0)')
    cursor.execute('UPDATE visits SET count = count + 1 WHERE id = 1')
    result = cursor.execute('SELECT count FROM visits WHERE id = 1').fetchone()
    conn.commit()
    conn.close()
    # Retorna uma página HTML com a contagem e um botão de reset
    return f"""
    <html>
        <body>
            <h1>Visitas: {result['count']}</h1>
            <form action="/reset" method="post">
                <button type="submit">Reiniciar Contagem</button>
            </form>
        </body>
    </html>
    """

# Rota para reiniciar a contagem
@app.route('/reset', methods=['POST'])
def reset():
    # Zera o contador do banco SQLite
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE visits SET count = 0 WHERE id = 1')
    conn.commit()
    conn.close()
    # Zera o contador do Prometheus
    REQUEST_COUNT.set(0)
    return "Contagem reiniciada! <a href='/api'>Voltar</a>"

# Rota para métricas do Prometheus
@app.route('/metrics')
def metrics():
    return Response(generate_latest(REQUEST_COUNT), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5110)
    