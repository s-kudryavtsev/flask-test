from flask import Flask, render_template, request, redirect 
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 

app_context = app.app_context()
app_context.push()

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
