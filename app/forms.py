from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email

# FlaskForm, example form
class Formulario1(FlaskForm):
    
    # questions with validators
    
    # string questions
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    # attachment questions
    document = FileField('Adjunte un documento', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'txt', 'pdf','csv','xls'])
    ])
