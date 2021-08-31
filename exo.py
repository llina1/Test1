import flask, os # ON iporte le module flask 
from flask import Flask ,render_template , make_response, request, redirect, url_for, session
from flask.helpers import make_response
from werkzeug.utils import redirect
from werkzeug.wrappers import response #on crée un objet qui contiendra les donnees de l'application 
app = flask.Flask (__name__)  #on précise l endroit où la fction s appliquera, ici racine 

app.config["DEBUG"]="True"

@app.route('/page1/') 
def page1():
    return render_template('exoPage1.html',message="Bienvenu sur la page d'accueil") #intégrer un fichier html 

@app.route('/page2/')  
def page2():
    return render_template ('exoPage2.html',message="Se connecter") 
 
@app.route('/page3/') 
def page3():
    return render_template('exoPage3.html',message="se déconnecter")

# @app.route('/ExGet/') 
# def page4():
#     return render_template('ExGet.html')



# @app.route('/ExGet',methods=['POST]'] )
# def signup():
#     session['username']=request.form['login']
#    # return redirect(url_for('ExGet.html'))  
#     return "<h1> BIENVENUE <h1>"

@app.route('/ExGet/', methods=['POST']) 
def se_loger():
   return redirect(url_for('page2'))
    return "<h1> BIENVENUE <h1>"
if __name__=="__main__":
   app.run()