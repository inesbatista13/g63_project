from flask import Flask, render_template, request, session
from datafile import filename

from classes.supermarket import Supermarket
from classes.department  import Department
from classes.supplier    import Supplier
from classes.transation  import Transation
from classes.userlogin   import Userlogin

from subs.apps_gform       import apps_gform
from subs.apps_supermarket import apps_supermarket   # Membro 1
from subs.apps_department  import apps_department    # Membro 2
from subs.apps_supplier    import apps_supplier      # Membro 3
from subs.apps_transation  import apps_transation    # Membro 3
from subs.apps_plot        import apps_plot          # Membro 4
from subs.apps_plotly      import apps_plotly        # Membro 4
from subs.apps_userlogin   import apps_userlogin

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

Supermarket.read(filename + 'g63_database.db')
Department.read(filename  + 'g63_database.db')
Supplier.read(filename    + 'g63_database.db')
Transation.read(filename  + 'g63_database.db')
Userlogin.read(filename   + 'g63_database.db')

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/login")
def login():
    return render_template("login.html", user="", password="",
                           ulogin=session.get("user"), resul="")

@app.route("/logoff")
def logoff():
    session.pop("user", None)
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post", "get"])
def chklogin():
    user     = request.form["user"]
    password = request.form["password"]
    resul    = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password=password,
                           ulogin=session.get("user"), resul=resul)

@app.route("/Supermarket", methods=["post", "get"])
def supermarket():
    return apps_supermarket()

@app.route("/Department", methods=["post", "get"])
def department():
    return apps_department()

@app.route("/Supplier", methods=["post", "get"])
def supplier():
    return apps_supplier()

@app.route("/Transation", methods=["post", "get"])
def transation():
    return apps_transation()

@app.route("/gform/<cname>", methods=["post", "get"])
def gform(cname):
    return apps_gform(cname)

@app.route("/plot", methods=["post", "get"])
def plot():
    return apps_plot()

@app.route("/plotly", methods=["post", "get"])
def plotly():
    return apps_plotly()

@app.route("/Userlogin", methods=["post", "get"])
def userlogin():
    return apps_userlogin()

if __name__ == '__main__':
    app.run()
