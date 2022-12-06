import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return f"hello world: {os.getenv('DB_HOST')}"


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
