##### IMPORT DE FONCTION() ########

from flask import Flask,g, render_template, request, url_for, redirect
#from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql



app = Flask(__name__)



###### lien vers les differentes pages #######"debut"
@app.route('/')
def home():
    statut = str('déconecter')

    return render_template('index.html',statut = statut,)

@app.route('/connecter')
def connecter():
    statut = str('connecter')
    return render_template('index.html',statut = statut,)


@app.route('/login')
def log():
   return render_template('login.html')

@app.route('/apple_bitcon')
def page_I():
    return render_template('/apple_bitcon.html')

@app.route('/purchase')
def aller_page_achats():
    #ici les variables sont la par default permetent d'afficher un tableau avec des variables qui n'ont pas encore ete definis.
    variété = str("#")
    prix = list([0,0])
    v = 0
    ########################


    return render_template('purchase.html', prix = prix, v = v, variété = variété)

#################################################" fin "

### partie connexion ### work in porgress
@app.route("/redirection")
def redirection_login():
    return render_template("/redirection_apres_login.html")
### partie connexion ### work in porgress

## partie inscription  debut ##

@app.route("/inscription", methods = ["GET","POST"])
def  inscription():
         nm = request.form['name']
         pin = request.form['pin']
         print (nm , pin)
         with sql.connect("db/Users.db") as con:
             try:
                 cur = con.cursor()
                 cur.execute("INSERT INTO student (name,pin) VALUES (?,?)",(nm,pin) )
                 con.commit()
                 msg = (",vous avez bien été inscrit, retounez a la page du site")
             finally:
                 return render_template("redirection.html",msg = msg, nm = nm)
         con.close()

######  partie incrition fin ####################

###### achats pommes #########

@app.route('/prix_pommes', methods = ["POST", "GET"] )
def prix_pomme():
        variété = request.form["variété_pomme"]
        kilo_pommes = request.form["kilo"]
        print (variété)
        with sql.connect("db/list_pommes.db") as con:
            cur = con.cursor()
            cur.execute('Select DISTINCT prix from pommes where variété = ? ', (variété,))
            prix = cur.fetchall()
            print (variété, prix  , kilo_pommes)

            return render_template ("purchase.html", prix = prix, variété = variété, kilo_pommes = kilo_pommes )





### lancer flask app ##

if __name__ == '__main__':
   app.run(debug = True)

######################################
