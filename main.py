from flask import Flask, render_template, request, redirect
from file_proc import pievienot, lasitRindinas

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text
# from flask_wtf import FlaskForm
# from flask_bootstrap import Bootstrap

# from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
# from wtforms.validators import InputRequired, Length, Regexp, NumberRange

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'pitons'


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ieraksti.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Bootstrap(app)

# db = SQLAlchemy(app)

#db.create_all()

# dati = []

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/results', methods=["POST", "GET"]) 
# def results():
#     #vards = request.form['vards']
#     #uzvards = request.form['uzvards']
#     #epasts = request.form['epasts']
#     #jauns_vards = Ieraksti(name=vards)
#     #jauns_uzvards = Ieraksti(name=uzvards)
#     #jauns_epasts = Ieraksti(name=epasts)

#     #db.session.add()
#     #db.session.commit()

#     #ieraksti = Ieraksti.query
#     return render_template('results.html')

@app.route('/kontakti', methods=["POST", "GET"])
def kontakti():
    #print(request.form)
    # ieraksts = request.form.get('vards', 'uzvards', 'epasts')
    # pievienot(ieraksts)
    return render_template('kontakti.html')

@app.route('/par_mani')
def par_mani():
    return render_template('par_mani.html')

@app.route('/dati', methods=["POST", "GET"])
def dati():
    return render_template('dati.html')

@app.route('/asv', methods = ['GET'])
def asv():
    return render_template('asv.html')

@app.route('/indija', methods = ['GET'])
def indija():
    return render_template('indija.html')

@app.route('/form', methods=["POST", "GET"]) 
def form():
    vards = request.form.get['vards']
    uzvards = request.form.get['uzvards']
    epasts = request.form.get['epasts']
    title = "Paldies!"
    return render_template('form.html', vards=vards, uzvards=uzvards, epasts=epasts)

@app.route('/result',methods = ['POST', 'GET']) 
def result(): 
   if request.method == 'POST': 
      result = request.form 
      return render_template("result.html",result = result) 


# pārbaudu konekciju ar DB
# @app.route('/test')
# def testdb():
#     try:
#         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text

# spēlējos ar ievadlaukiem
# class Ieraksts(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     vards = db.Column(db.String(100), nullable=False)
#     uzvards = db.Column(db.String(100), nullable=False)
#     epasts = db.Column(db.String(100), nullable=False)
#     def __init__(self, vards, uzvards, epasts):
#         self.vards = vards
#         self.uzvards = uzvards
#         self.epasts = epasts

# class AddRecord(FlaskForm):
#     id_field = HiddenField()
#     vards = StringField('vards')
#     uzvards = StringField('uzvards')
#     epasts = StringField('epasts')
#     pievienot = SubmitField('Pievienot')

# @app.route('/pievienot', methods=['GET', 'POST'])
# def add_record():
#     form1 = AddRecord()
#     if form1.validate_on_submit():
#             vards = request.form['vards']
#             uzvards = request.form['uzvards']
#             epasts = request.form['epasts']
#             record = Ieraksts(vards, uzvards, epasts)
#             db.session.add(record)
#             db.session.commit()
#     else:
    
#         return render_template('pievienot.html')

@app.errorhandler(404)
def page_not_found(e):
       return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(port=80, debug=True)

