from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    session,
    redirect,
    url_for,
    send_file,
)
from flask_mysqldb import MySQL
import os
import datetime
import matplotlib

matplotlib.use("Agg")
from matplotlib.backend_tools import cursors
import matplotlib.pyplot as plt
import io
from functools import wraps

app = Flask(__name__)
app.secret_key = "12345678"

app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASS")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
mysql = MySQL(app)


@app.route("/")
def index():

    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]

    else:
        name_now = None
    return render_template("index.html", name_now=name_now)


@app.route("/ferramentas")
def ferramentas():

    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]

    else:
        name_now = None
    return render_template("ferramentas.html", name_now=name_now)


@app.route("/sobre_nos")
def sobre_nos():
    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]
    else:
        name_now = None
    return render_template("sobre_nos.html", name_now=name_now)


@app.route("/resultados")
def resultados():
    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]
    else:
        name_now = None
    user_id = session.get("user_id")
    cur = mysql.connection.cursor()
    cur.execute(
        """SELECT
        u.id, u.name, e.score, e.users_answer, e.review_score, e.review_comment, e.created_at
        FROM exams AS e
        INNER JOIN users AS u ON u.id = e.user_id
        ORDER BY e.created_at DESC;"""
    )
    exams = cur.fetchall()
    cur.close()

    data = []
    for ex in exams:
        res = {
            "user_id": ex[0],
            "user_name": ex[1],
            "score": ex[2],
            "review_score": ex[4],
            "review_comment": ex[5],
        }
        data.append(res)

    return render_template(
        "resultados.html", name_now=name_now, data=data, user_id=user_id
    )


@app.route("/artefatos-e-eventos-1")
def artefatoseeventos1():
    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]
    else:
        name_now = None
    return render_template("conteudos/artefatos-e-eventos-1.html", name_now=name_now)


@app.route("/introducao")
def introducao():
    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]
    else:
        name_now = None
    return render_template("conteudos/introducao.html", name_now=name_now)


@app.route("/artefatos-e-eventos-2")
def artefatoseeventos2():
    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]
    else:
        name_now = None
    return render_template("conteudos/artefatos-e-eventos-2.html", name_now=name_now)


@app.route("/papeis-e-pilares")
def papeisepilares():
    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]
    else:
        name_now = None
    return render_template("conteudos/papeis-e-pilares.html", name_now=name_now)


@app.route("/exemplo")
def conteudo():
    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]
    else:
        name_now = None
    return render_template("conteudos/exemplo.html", name_now=name_now)


@app.route("/questoes")
def questoes():
    return render_template("samples/questoes.html")


@app.route("/cadastro")
def cadastro():
    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]
    else:
        name_now = None
    return render_template("components/questoes.html", name_now=name_now)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]

    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, name FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user:
            session["user_id"] = user[0]
            session["name_now"] = user[1]
            session["email"] = email
            return jsonify({"success": True})
        else:
            return jsonify({"success": False})
    except Exception as e:
        return jsonify({"success": False})


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    NameUser = data["NameUser"]
    email = data["email"]
    created_at = datetime.datetime.now()
    if len(NameUser.split()) > 1:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users (name, email, created_at) VALUES (%s, %s,%s)",
            (NameUser, email, created_at),
        )
        mysql.connection.commit()
        cur.execute("SELECT id FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()
        session["user_id"] = user[0]
        session["name_now"] = NameUser
        session["email"] = email
        return jsonify({"NameUser": NameUser, "email": email})
    else:
        return jsonify({"success": False, "message": "Invalid name"}), 400


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("name_now", None)
    session.pop("email", None)
    session.pop("user_id", None)
    return jsonify({"success": True})


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "name_now" not in session:
            return redirect(url_for("index", require_login=True, redirect_for="/exame"))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/exame")
@login_required
def exame():
    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]
    else:
        name_now = None
    return render_template("exame.html", name_now=name_now)


@app.route("/avaliar")
@login_required
def avaliar():
    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]
    else:
        name_now = None
    return render_template("components/avaliar.html", name_now=name_now)


@app.route("/certificado")
@login_required
def certificado():
    user_name = session.get("name_now")
    return render_template("components/certificado.html", user_name=user_name)


@app.route("/submit-score-exame", methods=["POST"])
def submit_score_exame():
    data = request.json
    total_correct = data.get("totalCorrect")
    users_answer = data.get("userAnswers")
    user_id = session.get("user_id")

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO exams (user_id, score, users_answer, created_at)
            VALUES (%s, %s, %s, NOW())
            """,
            (user_id, total_correct, users_answer),
        )
        mysql.connection.commit()
        cursor.close()

        return jsonify(
            {
                "status": "success",
                "totalCorrect": total_correct,
                "userAnswers": users_answer,
            }
        )
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/submit-avaliacao", methods=["POST"])
def submit_avaliacao():
    comentario = request.form["comentario"]
    estrelas = request.form["fb"]

    id_user = session.get("user_id")

    print(f"Comentário: {comentario}, Estrelas: {estrelas}")
    print(id_user)
    cursor = mysql.connection.cursor()
    cursor.execute(
        """ UPDATE exams
        SET review_comment = %s, review_score = %s
        WHERE user_id = %s AND review_score IS NULL""",
        (comentario, estrelas, id_user),
    )
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for("resultados"))


@app.route("/estimativas")
def estimativas():
    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]
    else:
        name_now = None
    return render_template("conteudos/estimativas.html", name_now=name_now)


@app.route("/artefatos-e-eventos-3")
def artefatoseeventos3():
    if session.get("name_now"):
        name_now = session.get("name_now").split()[0]
    else:
        name_now = None
    return render_template("conteudos/artefatos-e-eventos-3.html", name_now=name_now)


# Função para calcular a média de acertos
def calcular_media_acertos():
    cursor = mysql.connection.cursor()
    cursor.execute(
        """
        SELECT AVG(score) AS media_total_score
        FROM exams
        """
    )

    media_de_acertos = cursor.fetchone()[0]
    media_de_acertos = (media_de_acertos / 10) * 100
    cursor.close()

    return media_de_acertos


@app.route("/plot.png")
def plot_png():

    media_de_acertos = calcular_media_acertos()

    values = [100 - media_de_acertos, media_de_acertos]
    labels = ["Erros", "Acertos"]
    colors = ["red", "green"]

    img = io.BytesIO()
    plt.figure(figsize=(5, 5))
    plt.pie(
        values,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        startangle=140,
        textprops={"color": "white", "fontweight": "bold"},
        labeldistance=1.1,
    )
    plt.axis("equal")
    plt.title("Média de Aproveitamento", color="white", fontweight="bold")
    plt.savefig(img, format="png", transparent=True)
    img.seek(0)
    plt.close()

    return send_file(img, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
