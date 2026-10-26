from flask import Flask
import pymysql
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        # Conexión a la base de datos usando las variables del docker-compose
        connection = pymysql.connect(
            host=os.environ.get('DB_HOST', 'db'),
            user=os.environ.get('DB_USER', 'root'),
            password=os.environ.get('DB_PASSWORD', 'root'),
            database=os.environ.get('DB_NAME', 'testdb')
        )
        return "<h1>Hola Mundo!</h1><p>¡Conexión a MySQL exitosa! 🚀</p>"
    except Exception as e:
        return f"<h1>Hola Mundo!</h1><p>Error conectando a MySQL: {e}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)