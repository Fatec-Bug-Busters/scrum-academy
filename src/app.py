from flask import Flask, render_template, request, jsonify, session, redirect, url_for
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

#Quizz ainda nao funcionando pois falta o interaction_id
@app.route('/submit-score', methods=['POST'])
def submit_score():
    data = request.json
    total_correct = data.get("totalCorrect")
    user_answers = data.get("userAnswers")
    print(f"Quantidade de questões corretas recebidas: {total_correct}")

    # cursor = mysql.connection.cursor()
    # cursor.execute(''' 
    #     INSERT INTO quizzes (score, users_answer) 
    #     VALUES (%s, %s) 
    # ''', (total_correct, user_answers))
    # mysql.connection.commit()
    # cursor.close()

    return jsonify({"status": "success", "totalCorrect": total_correct, "userAnswer": user_answers})

@app.route('/submit-score-exame', methods=['POST'])
def submit_score_exame():
    data = request.json
    total_correct = data.get("totalCorrect")
    users_answer = data.get("userAnswers")

    try:
        cursor = mysql.connection.cursor()
        cursor.execute('''
            INSERT INTO exams (score, users_answer, created_at)
            VALUES (%s, %s, NOW())
        ''', (total_correct, users_answer))
        mysql.connection.commit()
        cursor.close()

        return jsonify({"status": "success", "totalCorrect": total_correct, "userAnswers": users_answer})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@app.route('/submit-avaliacao', methods=['POST'])
def submit_avaliacao():
    comentario = request.form['comentario']
    estrelas = request.form['fb']

    print(f"Comentário: {comentario}, Estrelas: {estrelas}")
    
    
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO iterations(review_comment, review_score, created_at) VALUES(%s, %s, NOW()) ''', (comentario, estrelas))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('resultados'))

if __name__ == "__main__":
    app.run(debug=True)
