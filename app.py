from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

app = Flask(__name__)
app.secret_key = "CHAVE_SECRETA"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form['email']
        telephone = request.form['telephone']
        name = request.form['name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        existing_user = User.get_by_email(email)
        if existing_user:
            flash("E-mail já está em uso!", "error")
            return render_template('register.html')

        if password != confirm_password:
            flash("As senhas não coincidem!", "error")
            return render_template('register.html')

        hashed_password = generate_password_hash(password)

        User.create(name=name, email=email, telephone=telephone, password=hashed_password)

        flash("Cadastro realizado com sucesso! Faça login.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        senha = request.form.get('password')

        user = User.get_by_email(email)

        if not user:
            flash("E-mail não cadastrado!", "error")
            return render_template('login.html')

        if not check_password_hash(user.password, senha):
            flash("Senha incorreta!", "error")
            return render_template('login.html')

        login_user(user, remember=True)

        flash("Login realizado com sucesso!", "success")
        return redirect(url_for('index'))

    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for('login'))

@app.route("/")
@login_required
def index():
    return render_template('index.html')

@app.route("/conjuntos")
@login_required
def conjuntos():
    return render_template('conjuntos.html')

@app.route("/brincos")
@login_required
def brincos():
    return render_template('brincos.html')

@app.route("/colares")
@login_required
def colares():
    return render_template('colares.html')

@app.route("/pulseiras")
@login_required
def pulseiras():
    return render_template('pulseiras.html')

@app.route("/aneis")
@login_required
def aneis():
    return render_template('aneis.html')

if __name__ == "__main__":
    app.run(debug=True)
