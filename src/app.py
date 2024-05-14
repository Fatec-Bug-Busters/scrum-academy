from flask import Flask, render_template

app = Flask(__name__)


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

@app.route("/certificado")
def certificado():
    return render_template("components/certificado.html")

if __name__ == "__main__":
    app.run(debug=True)
