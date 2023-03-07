from . import db
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed


class Property(db.Model):

    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    bedrooms = db.Column(db.String)
    bathrooms = db.Column(db.String)
    location = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    photo_path = db.Column(db.String(255), nullable=False)

    def __init__(self, title, description, bedrooms, bathrooms, location, price, type, photo_path):
        self.title = title
        self.description = description
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.location = location
        self.price = price
        self.type = type
        self.photo_path = photo_path        

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    bedrooms = StringField('No. of Bedrooms', validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    description = TextAreaField('Description', validators=[DataRequired()])
    photo_path = FileField('Photo', validators=[DataRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
