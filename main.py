from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ieraksti.db'


db = SQLAlchemy(app)
#db.create_all()
dati = []

class Ieraksti(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vards = db.Column(db.String(100), nullable=False)
    uzvards = db.Column(db.String(100), nullable=False)
    epasts = db.Column(db.String(100), nullable=False)
    datums = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return f"Ieraksti('{self.vards}', '{self.uzvards}', '{self.epasts}', '{self.datums}')"



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=["POST", "GET"]) 
def results():
    vards = Request.form['vards']
    uzvards = request.form['uzvards']
    epasts = request.form['epasts']
    datums = request.form['datums']
    jauns_vards = Ieraksti(name=vards)
    jauns_uzvards = Ieraksti(name=uzvards)
    jauns_epasts = Ieraksti(name=epasts)
    jauns_datums = Ieraksti(name=datums)

    db.session.add()
    db.session.commit()

    ieraksti = Ieraksti.query
    return render_template('results.html')

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

