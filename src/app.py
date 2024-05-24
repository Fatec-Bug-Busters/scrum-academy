from flask import Flask, render_template, request, jsonify, session
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


@app.route("/avaliar")
def avaliar():
    return render_template("components/avaliar.html")

@app.route("/certificado")
def certificado():
    return render_template("components/certificado.html")

@app.route('/submit-score', methods=['POST'])
def submit_score():
    data = request.json
    total_correct = data.get("totalCorrect")
    user_answers = data.get("userAnswers")
    print(f"Quantidade de questões corretas recebidas: {total_correct}")
    return jsonify(
        {"status": "success", "totalCorrect": total_correct, "userAnswer": user_answers}
    )

if __name__ == "__main__":
    app.run(debug=True)
