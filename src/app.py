from flask import Flask, request, render_template, redirect, url_for

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


@app.route("/avaliar")
def avaliar():
    return render_template("components/avaliar.html")

@app.route("/submit", methods=["POST"])
def form1():
    nome = request.form.get("nome")
    q1 = request.form.get("q1")
    q2 = request.form.get("q2")
    q3 = request.form.get("q3")
    q4 = request.form.get("q4")
    q5 = request.form.get("q5")
    q6 = request.form.get("q6")
    q7 = request.form.get("q7")
    q8 = request.form.get("q8")
    q9 = request.form.get("q9")
    q10 = request.form.get("q10")
    return redirect(
        url_for(
            "avaliar",
            nome=nome,
            q1=q1,
            q2=q2,
            q3=q3,
            q4=q4,
            q5=q5,
            q6=q6,
            q7=q7,
            q8=q8,
            q9=q9,
            q10=q10,
        )
    )


@app.route("/avaliar")
def result_form1():
    nome = request.args.get("nome")
    q1 = request.args.get("q1")
    q2 = request.args.get("q2")
    q3 = request.args.get("q3")
    q4 = request.args.get("q4")
    q5 = request.args.get("q5")
    q6 = request.args.get("q6")
    q7 = request.args.get("q7")
    q8 = request.args.get("q8")
    q9 = request.args.get("q9")
    q10 = request.args.get("q10")
    return render_template(
        "avaliar.html",
        nome=nome,
        q1=q1,
        q2=q2,
        q3=q3,
        q4=q4,
        q5=q5,
        q6=q6,
        q7=q7,
        q8=q8,
        q9=q9,
        q10=q10,
    )


@app.route("/submit2", methods=["POST"])
def form2():
    nome = request.form.get("nome")
    q1 = request.form.get("q1")
    q2 = request.form.get("q2")
    q3 = request.form.get("q3")
    q4 = request.form.get("q4")
    q5 = request.form.get("q5")
    q6 = request.form.get("q6")
    q7 = request.form.get("q7")
    q8 = request.form.get("q8")
    q9 = request.form.get("q9")
    q10 = request.form.get("q10")
    comentario = request.form.get("comentario")
    fb = request.form.get("fb")
    return redirect(
        url_for(
            "result",
            nome=nome,
            q1=q1,
            q2=q2,
            q3=q3,
            q4=q4,
            q5=q5,
            q6=q6,
            q7=q7,
            q8=q8,
            q9=q9,
            q10=q10,
            comentario=comentario,
            fb=fb,
        )
    )


@app.route("/result")
def result():
    nome = request.args.get("nome")
    q1 = request.args.get("q1")
    q2 = request.args.get("q2")
    q3 = request.args.get("q3")
    q4 = request.args.get("q4")
    q5 = request.args.get("q5")
    q6 = request.args.get("q6")
    q7 = request.args.get("q7")
    q8 = request.args.get("q8")
    q9 = request.args.get("q9")
    q10 = request.args.get("q10")
    comentario = request.args.get("comentario")
    fb = request.args.get("fb")
    return render_template(
        "result.html",
        nome=nome,
        q1=q1,
        q2=q2,
        q3=q3,
        q4=q4,
        q5=q5,
        q6=q6,
        q7=q7,
        q8=q8,
        q9=q9,
        q10=q10,
        comentario=comentario,
        fb=fb,
    )

if __name__ == "__main__":
    app.run(debug=True)
