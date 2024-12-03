from flask import Flask, render_template, request, redirect

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

@app_guilherme.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if email == "admin@example.com" and senha == "123456":
            return redirect('/homepage')  
        else:
            return "<script>alert('E-mail ou senha inválidos!'); window.history.back();</script>"

    return render_template('login.html')  

if __name__ == '__main__':
    app_guilherme.run(port=8080, debug=True)
