from wtforms import Form
from wtforms import StringField, IntegerField, EmailField
from wtforms import validators

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