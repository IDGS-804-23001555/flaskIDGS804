from wtforms import Form
from wtforms import StringField, IntegerField, EmailField
from wtforms import validators

from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, EmailField, validators

class UserForm(Form):
    id = IntegerField('id', [
        validators.Optional()  # Se usa Optional porque al registrar uno nuevo el ID suele estar vacío
    ])
   
    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='Requiere min=4 max=20')
    ])
   
    apellidos = StringField('apellidos', [
        validators.DataRequired(message='El apellido es requerido')
    ])
   
    email = EmailField('correo', [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo válido')
    ])

    telefono = StringField('telefono', [
        validators.DataRequired(message='El teléfono es requerido'),
        validators.length(min=10, max=10, message='El teléfono debe tener 10 dígitos')
    ])

class MaestroForm(Form):
    matricula = IntegerField('matricula', [
        validators.DataRequired(message='La matricula es requerida')
    ])
   
    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere min=4 max=20')
    ])
   
    apellidos = StringField('apellidos', [
        validators.DataRequired(message='Los apellidos son requeridos')
    ])
   
    email = EmailField('correo', [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])

    especialidad = StringField('especialidad', [
        validators.DataRequired(message='La especialidad es requerida')
    ])