from flask import Flask, render_template

app_guilherme = Flask(__name__, template_folder="templates")

@app_guilherme.route('/')
def home():
    return render_template('index.html')

@app_guilherme.route('/contato')
def contato():
    return render_template('contato.html')

@app_guilherme.route('/usuario')
def usuario():
    return render_template('usuario.html')

@app_guilherme.route('/homepage')
def homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
    app_guilherme.run(port=8080, debug=True)
