from flask import Flask, render_template
from flask_mysqldb import MySQL
import os
import datetime

app = Flask(__name__)

app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASS")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
mysql = MySQL(app)

# now = datetime.datetime.now()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sobre_nos")
def sobre_nos():
    return render_template("sobre_nos.html")


@app.route("/exame")
def exame():
    return render_template("exame.html")


@app.route("/resultados")
def resultados():
    return render_template("resultados.html")


@app.route("/artefatos-e-eventos-1")
def artefatoseeventos1():
    return render_template("conteudos/artefatos-e-eventos-1.html")


@app.route("/introducao")
def introducao():
    return render_template("conteudos/introducao.html")


@app.route("/artefatos-e-eventos-2")
def artefatoseeventos2():
    return render_template("conteudos/artefatos-e-eventos-2.html")


@app.route("/papeis-e-pilares")
def papeisepilares():
    return render_template("conteudos/papeis-e-pilares.html")


@app.route("/exemplo")
def conteudo():
    return render_template("conteudos/exemplo.html")


@app.route("/questoes")
def questoes():
    return render_template("components/questoes.html")


@app.route("/cadastro")
def cadastro():
    return render_template("components/cadastro.html")


if __name__ == "__main__":
    app.run(debug=True)
