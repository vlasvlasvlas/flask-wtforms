from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email

# FlaskForm
class Formulario1(FlaskForm):
    
    firstname = StringField('First Name', validators=[DataRequired()])
    
    lastname = StringField('Last Name', validators=[DataRequired()])
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    document = FileField('Documento', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'txt', 'pdf','csv','xls'])
    ])
