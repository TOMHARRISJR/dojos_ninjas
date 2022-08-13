
from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojos_Model import Dojo
from flask_app.models.ninjas_Model import Ninja

@app.route('/')
@app.route('/dojos')
def index():
    dojos = Dojo.display_dojos()
    return render_template("dojos.html",dojos=dojos)

@app.route("/dojos", methods=["POST"])  # The form for creating a new dojo
def form():
    Dojo.add_Dojo(request.form) 
    return redirect('/dojos')

@app.route("/dojos/<int:id>")
def ninjas_in_dojo(id):
    dojo = Dojo.get_one({"id": id})
    ninjas = Dojo.get_all_ninjas({"id": id})
    if not ninjas:
        ninjas = []
    return render_template("show_dojo.html", dojo=dojo, ninjas=ninjas)

@app.route("/ninjas/create" )
def create_ninja():
    all_dojos = Dojo.display_dojos()
    return render_template("ninja.html",dojos = all_dojos)

@app.route("/ninjas/create/process", methods=['POST'])
def create_ninja_process():
    data = {
        **request.form
    }
    Ninja.add_ninja(data)
    return redirect("/dojos")



