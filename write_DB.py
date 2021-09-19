# from re import S
# from flask import Flask, render_template, request, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap, is_hidden_field_filter

# from flask_wtf import FlaskForm
# from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
# from wtforms.validators import InputRequired, Length, Regexp, NumberRange

# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'pitons'

# Bootstrap(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ieraksti.db'

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# db = SQLAlchemy(app)

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
#         vards = request.form['vards']
#         uzvards = request.form['uzvards']
#         epasts = request.form['epasts']
#         record = Ieraksts(vards, uzvards, epasts)
#         db.session.add(record)
#         db.session.commit()
#     else:
#         print('kaut kas ne tā!')