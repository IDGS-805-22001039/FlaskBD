from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from config import DevelopmentConfig
import forms
 
 
from models import db
from models import Alumnos
 
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()
 
 
@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'), 404
 
""" @app.route("/")
@app.route("/index")
def index():
    return render_template("index.html") """
 
 
@app.route("/",methods=['GET','POST'])
@app.route("/index")
def index():
    create_form=forms.UserForm2(request.form)
    alumno=Alumnos.query.all() #Select  *  from alumnos
   
    return render_template("index.html",form=create_form,alumnos=alumno)
 
@app.route("/detalles",methods=['GET','POST'])
def detalles():
    create_form = forms.UserForm2(request.form)
    if request.method == "GET":
        id=request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        nom = alum1.nombre
        ape = alum1.apaterno
        email = alum1.email
    return render_template("detalles.html", form=create_form,nombre=nom, apellido=ape, email=email)

@app.route('/Alumnos1', methods=['GET','POST'])
def Alumnos1():
    create_form=forms.UserForm2(request.form)
    if request.method == "POST":
        alum=Alumnos(nombre=create_form.nombre.data,
                     apaterno=cre)
    return render_template("detalles.html", form=create_form,nombre=nom, apellido=ape, email=email)
 
if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
