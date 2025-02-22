from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Produto

app = Flask(__name__)
app.secret_key = "CHAVE_SECRETA"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/carrinho", methods=['GET', 'POST'])
@login_required
def carrinho():
    user_id = current_user.id
    carrinho = Produto.select_carrinho(user_id)

    return render_template('carrinho.html',carrinho=carrinho)


@app.route("/favoritos", methods=['GET', 'POST'])
@login_required
def favoritos():
    user_id = current_user.id
    favoritos = Produto.select_favoritos(user_id)

    return render_template('favoritos.html',favoritos=favoritos)


@app.route("/excluir_carrinho/<int:id>", methods=['GET', 'POST'])
@login_required
def excluir_carrinho(id):
    if request.method=='POST':
        Produto.excluir_carrinho(id)
    
    return redirect(url_for('carrinho'))


@app.route("/add_carrinho", methods=['GET', 'POST'])
def add_carrinho():   
    user_id = current_user.id
    produto = request.form['id']
    Produto.add_carrinho(produto,user_id)
    carrinho = Produto.select_carrinho(user_id)
    return render_template('carrinho.html',carrinho=carrinho)


@app.route("/add_favoritos", methods=['POST'])
@login_required
def add_favoritos():
    user_id = current_user.id
    produto = request.form.get('id')

    if not produto:
        flash("Erro: Produto não especificado.", "danger")
        return redirect(url_for('exibir_produtos'))

    produto = int(produto)
    favoritos = Produto.select_favoritos(user_id)

    if any(produto == fav[0] for fav in favoritos):
        Produto.excluir_favoritos(produto)
        favorito = Produto.select_favoritos(user_id)
        flash("Produto removido dos favoritos.", "success")
        sucesso = False
        return render_template('favoritos.html',sucesso=sucesso,favoritos=favorito)
    else:
        sucesso = True
        Produto.add_favoritos(produto, user_id)
        favorito = Produto.select_favoritos(user_id)
        flash("Produto adicionado aos favoritos!", "success")
        return render_template('favoritos.html',sucesso=sucesso,favoritos=favorito)

    


@app.route("/excluir_favoritos/<int:id>", methods=['POST'])
@login_required
def excluir_favoritos(id):
    Produto.excluir_favoritos(id)
    flash("Produto removido dos favoritos.", "success")
    return redirect(url_for('favoritos'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form['email']
        telephone = request.form['telephone']
        name = request.form['name']
        password = request.form['senha']
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


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        senha = request.form.get('senha')

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


@app.route("/index")

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


@app.route("/info")
@login_required
def info():
    return render_template('infos.html')

@app.route("/sobre")
@login_required
def sobre():
    return render_template('sobrenos.html')   

@app.route("/produtos/<int:id>")
@login_required
def produtos(id):
    produtos = Produto.get_id(id)
    return render_template('produtos.html',produto=produtos)


if __name__ == "__main__":
    app.run(debug=True)


