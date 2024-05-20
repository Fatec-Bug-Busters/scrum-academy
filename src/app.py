
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from flask_mysqldb import MySQL
import os
import datetime import date

app = Flask(__name__)
app.secret_key = "12345678"


lst_user = {
    "user1@example.com": {"NameUser": "Alice", "CreatedAtDate": "2022-12-01", "id": 1},
    "user2@example.com": {"NameUser": "Bob", "CreatedAtDate": "2022-11-01", "id": 2},
    "user3@example.com": {"NameUser": "Charlie", "CreatedAtDate": "2022-10-01", "id": 3}
}

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
    

    if email in lst_user:
        session['name_now'] = lst_user[email]["NameUser"]
        session['email'] = email
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    NameUser = data['NameUser']
    email = data['email']
    
    if len(NameUser.split()) > 1:
        lst_user[email] = {"NameUser": NameUser, "CreatedAtDate": date.today().strftime("%Y-%m-%d"), "id": 4}
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



if __name__ == "__main__":
    app.run(debug=True)
