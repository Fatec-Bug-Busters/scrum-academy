
from flask import Flask, render_template, jsonify, request, session
from flask_mysqldb import MySQL
import os
import datetime

app = Flask(__name__)
app.secret_key = "12345678"


app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASS")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
mysql = MySQL(app)

# now = datetime.datetime.now()


@app.route("/")
def index():
    name_now = session.get('name_now')
    return render_template("index.html", name_now=name_now)


@app.route("/sobre_nos")
def sobre_nos():
    name_now = session.get('name_now')
    return render_template("sobre_nos.html", name_now=name_now)


@app.route("/exame")
def exame():
    name_now = session.get('name_now')
    return render_template("exame.html", name_now=name_now)


@app.route("/resultados")
def resultados():
    name_now = session.get('name_now')
    return render_template("resultados.html", name_now=name_now)


@app.route("/artefatos-e-eventos-1")
def artefatoseeventos1():
    name_now = session.get('name_now')
    return render_template("conteudos/artefatos-e-eventos-1.html", name_now=name_now)


@app.route("/introducao")
def introducao():
    name_now = session.get('name_now')
    return render_template("conteudos/introducao.html", name_now=name_now)


@app.route("/artefatos-e-eventos-2")
def artefatoseeventos2():
    name_now = session.get('name_now')
    return render_template("conteudos/artefatos-e-eventos-2.html", name_now=name_now)


@app.route("/papeis-e-pilares")
def papeisepilares():
    name_now = session.get('name_now')
    return render_template("conteudos/papeis-e-pilares.html", name_now=name_now)


@app.route("/exemplo")
def conteudo():
    name_now = session.get('name_now')
    return render_template("conteudos/exemplo.html", name_now=name_now)


@app.route("/questoes")
def questoes():

    name_now = session.get('name_now')
    return render_template("components/questoes.html", name_now=name_now)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    

    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, name FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user:
            session['user_id'] = user[0]
            session['name_now'] = user[1]
            session['email'] = email
            return jsonify({'success': True})
        else:
            return jsonify({'success': False})
    except Exception as e:
        return jsonify({'success': False})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    NameUser = data['NameUser']
    email = data['email']
    created_at = datetime.datetime.now()
    if len(NameUser.split()) > 1:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, created_at) VALUES (%s, %s,%s)", (NameUser, email, created_at))
        mysql.connection.commit()
        cur.close()
        session['name_now'] = NameUser
        session['email'] = email
        return jsonify({'NameUser': NameUser, 'email': email})
    else:
        return jsonify({'success': False, 'message': 'Invalid name'}), 400



@app.route('/logout', methods=['POST'])
def logout():
    session.pop('name_now', None)
    session.pop('email', None)
    return jsonify({'success': True})

# Testes para salvar o quizz
@app.route("/introducao-teste")
def introducaoteste():
    name_now = session.get('name_now')
    return render_template("conteudos/introducao-teste.html", name_now=name_now)

@app.route('/submit-score', methods=['POST'])
def submit_score():
    data = request.json
    total_correct = data.get("totalCorrect")
    user_answers = data.get("userAnswers")
    print(f"Quantidade de questões corretas recebidas: {total_correct}")
    return jsonify(
        {"status": "success", "totalCorrect": total_correct, "userAnswer": user_answers}
    )


@app.route("/certificado")
def certificado():
    return render_template("components/certificado.html")

if __name__ == "__main__":
    app.run(debug=True)
