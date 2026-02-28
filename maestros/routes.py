from flask import render_template, request, redirect, url_for
from . import maestros
import forms
from models import db, Maestros

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"

@maestros.route('/maestros', methods=['GET', 'POST'])
@maestros.route("/index")
def index():
    create_form = forms.UserForm(request.form)
    maestros_list = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=maestros_list)

@app.route("/detalles", methods=['GET', 'POST'])
def detalles():
    id = request.args.get('id')
    alumno1 = Alumnos.query.get(id)
    if alumno1:
        # Actualizado para usar los nuevos nombres de columna
        return render_template("detalles.html", 
                               id=id, 
                               nombre=alumno1.nombre, 
                               apellidos=alumno1.apellidos, 
                               email=alumno1.email,
                               telefono=alumno1.telefono)
    return redirect(url_for('index'))

@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            # Llenamos el formulario con los nuevos campos
            create_form.id.data = alum1.id
            create_form.nombre.data = alum1.nombre
            create_form.apellidos.data = alum1.apellidos
            create_form.email.data = alum1.email
            create_form.telefono.data = alum1.telefono
        return render_template("modificar.html", form=create_form)

    if request.method == 'POST':
        id = create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        
        if alum1:
            # Actualizamos todos los datos en la DB
            alum1.nombre = create_form.nombre.data
            alum1.apellidos = create_form.apellidos.data
            alum1.email = create_form.email.data
            alum1.telefono = create_form.telefono.data
            db.session.commit()
        
        return redirect(url_for('index'))

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            create_form.id.data = alum1.id
            create_form.nombre.data = alum1.nombre
            create_form.apellidos.data = alum1.apellidos
            create_form.email.data = alum1.email
            create_form.telefono.data = alum1.telefono
        return render_template("eliminar.html", form=create_form)

    if request.method == 'POST':
        id = create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        
        if alum1:
            db.session.delete(alum1)
            db.session.commit()
            
        return redirect(url_for('index'))
