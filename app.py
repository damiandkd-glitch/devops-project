from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Cześć! Moja aplikacja działa w Kubernetes! Wersja 2 - GitOps działa!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)