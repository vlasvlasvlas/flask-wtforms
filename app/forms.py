from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class MyForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])


class DocumentForm(FlaskForm):
    document = FileField('Documento', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'txt', 'pdf','csv','xls'])
    ])
    description = StringField('Description', validators=[DataRequired()])