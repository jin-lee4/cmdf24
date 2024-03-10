import os, sys

from flask import Flask

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

if __name__ == "__main__":
    app.run()