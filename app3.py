import flask, os # ON iporte le module flask 
from flask import Flask ,render_template , make_response, request, redirect, url_for, session
from flask.helpers import make_response
from werkzeug.utils import redirect
from werkzeug.wrappers import response #on crée un objet qui contiendra les donnees de l'application 
app = flask.Flask (__name__)  #on précise l endroit où la fction s appliquera, ici racine 

app.config["DEBUG"]="True"
@app.route('/')
def index():
    return render_template('testform.html')

@app.route('/testform',methods=['POST','GET']) 
def signin():
    if request.method=='POST':
        return "hi"
    else: 
        form_nom= request.form['nom']
        form_prenom= request.form['prenom'] 
        form_age= request.form['age'] 
        return render_template("bienvenue.html",nom=form_nom, prenom=form_prenom, age=form_age)
if __name__=="__main__":
   app.run()