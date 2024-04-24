from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sobre_nos')
def sobre_nos():
    return render_template("sobre_nos.html")

if __name__ == '__main__':
    app.run(debug=True)