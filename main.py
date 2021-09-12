from flask import Flask, render_template, request, redirect
from flask.scaffold import F
from file_proc import pievienot
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.ieraksti'


db = SQLAlchemy(app)
dati = []





class Ieraksti(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vards = db.Column(db.String(100), nullable=False)
    uzvards = db.Column(db.String(100), nullable=False)
    epasts = db.Column(db.String(100), nullable=False)
    datums = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return '<Vards %r>' % self.id



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/kontakti')
def kontakti():
    return render_template('kontakti.html')

@app.route('/par_mani')
def par_mani():
    return render_template('par_mani.html')

@app.route('/jaunumi')
def jaunumi():
    return render_template('jaunumi.html')


@app.route('/form', methods=["POST"]) 
def form():
    vards = request.form.get("vards")
    uzvards = request.form.get("uzvards")
    epasts = request.form.get("epasts")
    dati.append(F"{vards} {uzvards} {epasts}")
    title = "Paldies!"
    return render_template('form.html', dati=dati)

if __name__ == '__main__':
    app.run(port=80, debug=True)

