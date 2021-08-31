import flask, os # ON iporte le module flask 
from flask import Flask ,render_template , make_response, request, redirect, url_for, session
from flask.helpers import make_response
from werkzeug.utils import redirect
from werkzeug.wrappers import response #on crée un objet qui contiendra les donnees de l'application 
app = flask.Flask (__name__)  #on précise l endroit où la fction s appliquera, ici racine 

app.config["DEBUG"]="True"
@app.route('/')
@app.secret_key=os.unrandom(24)
def page_1():
    username=request.cookies.get('username')
    return "Hi"
 
@app.route('/page2/') 
def page2():
    return"<strong>welcome</strong>"

@app.route('/next/') 
def next():
    return render_template ("next.html") #intégrer un fichier html 

@app.route('/suiv/') 
def suiv():
    return render_template ("next.html", message = "Laure" ) 

@app.route('/cookies') 
def pageCookies():
    response=make_response("<h1> cette page crée des cookies<h1>")
    response.set_cookie('username', 'Laure')
    return response

@app.route('/ExGet',methods=['POST]'] )
def signup():
    session['username']=request.form['login']
   # return redirect(url_for('ExGet.html'))  
    return "<h1> BIENVENUE <h1>"

@app.route('/ExGet/', methods=['POST']) 
def se_loger():
    return redirect(url_for('page2'))

  

if __name__=="__main__":
   app.run()