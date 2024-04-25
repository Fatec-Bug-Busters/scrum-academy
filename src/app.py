from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sobre_nos')
def sobre_nos():
    return render_template("sobre_nos.html")

@app.route('/exame_pg1')
def exame_pg1():
    return render_template("exame_pg1.html")

@app.route('/exame_pg2')
def exame_pg2():
    return render_template("exame_pg2.html")

@app.route('/exame_pg3')
def exame_pg3():
    return render_template("exame_pg3.html")

if __name__ == '__main__':
    app.run(debug=True)