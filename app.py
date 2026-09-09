import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    db_password = os.environ.get('DB_PASSWORD', 'BRAK - zmienna nie znaleziona')
    dlugosc_hasla = len(db_password)
    return f'Cześć! Moja aplikacja działa w Kubernetes! Sekret DB_PASSWORD ma {dlugosc_hasla} znaków.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)