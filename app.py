from flask import Flask, render_template, request, redirect 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

db = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)

    with app.app_context():
        db()

    return app
