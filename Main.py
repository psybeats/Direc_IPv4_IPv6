# Alejandro Alan Gutierrez Cortes, Mie, 07/07/2021, 11:57:00, Construcción del server con flask.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
