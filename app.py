from flask import Flask, render_template
from flask_sqlalchemy import sqlalchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or "sqlite:///notepad.sqlite" 

db = sqlalchemy(app)

class Duties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)

    
@app.route('/')
def index():
    return render_template('index.html', name="Janani")

if __name__ == '__main__':
    app.run(debug=True)