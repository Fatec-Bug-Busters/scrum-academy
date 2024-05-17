from flask import Flask, render_template, jsonify, request
from datetime import date

app = Flask(__name__)



lst_user = {
    "user1@example.com": {"NameUser": "Alice","CreatedAtDate" : "2022-12-01","id": 1},
    "user2@example.com": {"NameUser": "Bob","CreatedAtDate" : "2022-11-01", "id": 2},
    "user3@example.com": {"NameUser": "Charlie","CreatedAtDate" : "2022-10-01", "id": 3}
}

name_now = None

def return_template(template, **kwargs):
    return render_template(template, name_now=name_now, **kwargs)

@app.route("/")
def index():
    global name_now
    return return_template("index.html")


@app.route("/sobre_nos")
def sobre_nos():
    return return_template("sobre_nos.html")


@app.route("/exame")
def exame():
    return return_template("exame.html")


@app.route("/resultados")
def resultados():
    return return_template("resultados.html")


@app.route("/artefatos-e-eventos-1")
def artefatoseeventos1():
    return return_template("conteudos/artefatos-e-eventos-1.html")


@app.route("/introducao")
def introducao():
    return return_template("conteudos/introducao.html")


@app.route("/artefatos-e-eventos-2")
def artefatoseeventos2():
    return return_template("conteudos/artefatos-e-eventos-2.html")


@app.route("/papeis-e-pilares")
def papeisepilares():
    return return_template("conteudos/papeis-e-pilares.html")


@app.route("/exemplo")
def conteudo():
    return return_template("conteudos/exemplo.html")


@app.route("/questoes")
def questoes():
    return return_template("components/questoes.html")

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data['email']
        
        # Simples verificação de usuário e senha (aqui você pode conectar ao banco de dados para uma verificação real)
        if email in lst_user:
            global name_now
            name_now = lst_user[email]["NameUser"]
            return jsonify({'success': True})
        else:
            return jsonify({'success': False})

# Rota para o registro
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        NameUser = data['NameUser']
        email = data['email']
        if len(NameUser.split()) > 1:
            lst_user[email] = {"NameUser": NameUser, "CreatedAtDate" : date.today(), "id": 4}
        else:
            ErrorName = ErrorName
        global name_now
        name_now = lst_user[email]["NameUser"]
    return jsonify({'NameUser': NameUser, 'email': email})

# Rota para o registro
@app.route('/logout', methods=['POST'])
def logout():
    global name_now
    if request.method == 'POST':
        name_now = None
    return 


if __name__ == "__main__":
    app.run(debug=True)
