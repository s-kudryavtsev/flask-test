from flask import Flask, render_template, request, redirect 
from flask_sqlalchemy import SQLAlchemy 
import os
import logging
from logging.handlers import TimedRotatingFileHandler


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 

app_context = app.app_context()
app_context.push()


logs_path = 'c:\logs\\'

os.makedirs(logs_path, exist_ok=True)
logging.basicConfig(level=logging.DEBUG,
                    handlers=[TimedRotatingFileHandler(logs_path + '/app.log', when='D', interval=1, backupCount=10)],
                    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                    datefmt='%Y-%m-%dT%H:%M:%S'
                    )
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)


class Item(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False) 
    price = db.Column(db.Integer, nullable=False)
    isActve = db.Column(db.Boolean, default=True) 
   

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create',methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']

        item = Item(title=title, price=price)

        try:
            db.session.add(item)
            db.session.commit
            return redirect ('/')
        except:
            return "Где-то ошибка!"
    else:
        return render_template('create.html')

if  __name__ == '__main__':
    app.run(debug=True)
