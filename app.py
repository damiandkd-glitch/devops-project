import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    db_password = os.environ.get('DB_PASSWORD', 'BgownozieloneRAK - zmienna nie znaleziona')
    dlugosc_hasla = len(db_password)
    environment = os.environ.get('ENVIRONMENT', 'nieznane')
    return f'Cześć! Środowisko: {environment}. Sekret DB_PASSWORD ma {dlugosc_hasla} znaków. Wersja aplikacji: 3.0'
    return f'Cześć! Środowisko: {environment}. Sekret DB_PASSWORD ma {dlugosc_hasla} znaków. Wersja aplikacji: 3.0'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)