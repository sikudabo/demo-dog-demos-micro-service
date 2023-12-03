from flask import Flask

app = Flask(__name__)

@app.get('/')
def home_page():
    return "<h1>Home Page</h1>"

