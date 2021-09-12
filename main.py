from flask import Flask, render_template, request, redirect
from flask.scaffold import F
from file_proc import pievienot

dati = []

app = Flask(__name__)

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

