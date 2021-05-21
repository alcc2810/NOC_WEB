from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    var_lista = ['leo', 2810, 'said', 306, 'ariel', 2106]
    return render_template('index.html', var2html = var_lista)

if __name__ == '__main__':
    app.run(port=2810, debug=True)