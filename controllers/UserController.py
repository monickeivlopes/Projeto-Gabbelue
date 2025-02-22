from flask import request, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.models import User, Produto
from .. import app, login_manager



@login_manager.user_loader
def load_user(usuario_id):
    return User.get(usuario_id)


@app.route("/carrinho", methods=['GET', 'POST'])
@login_required
def carrinho():
    usuario_id = current_user.id
    carrinho = Produto.select_carrinho(usuario_id)

    return render_template('carrinho.html',carrinho=carrinho)


@app.route("/favoritos", methods=['GET', 'POST'])
@login_required
def favoritos():
    usuario_id = current_user.id
    favoritos = Produto.select_favoritos(usuario_id)

    return render_template('favoritos.html',favoritos=favoritos)


@app.route("/excluir_carrinho/<int:id>", methods=['POST'])
@login_required
def excluir_carrinho(id):
    Produto.excluir_carrinho(id, current_user.id)
    flash("Produto removido do carrinho.", "success")
    return redirect(url_for('carrinho'))


@app.route("/add_carrinho", methods=['GET', 'POST'])
def add_carrinho():   
    usuario_id = current_user.id
    produto = request.form['id']
    Produto.add_carrinho(produto, usuario_id)
    carrinho = Produto.select_carrinho(usuario_id)
    return render_template('carrinho.html',carrinho=carrinho)


@app.route("/add_favoritos", methods=['POST'])
@login_required
def add_favoritos():
    usuario_id = current_user.id
    produto = request.form.get('id')

    if not produto:
        flash("Erro: Produto não especificado.", "danger")
        return redirect(url_for('index'))

    produto = int(produto)
    favoritos = Produto.select_favoritos(usuario_id)

    if any(produto == fav[0] for fav in favoritos):
        Produto.excluir_favoritos(produto, usuario_id)
        favorito = Produto.select_favoritos(usuario_id)
        flash("Produto removido dos favoritos.", "success")
        sucesso = False
        return render_template('favoritos.html',sucesso=sucesso,favoritos=favorito)
    else:
        sucesso = True
        Produto.add_favoritos(produto, usuario_id)
        favorito = Produto.select_favoritos(usuario_id)
        flash("Produto adicionado aos favoritos!", "success")
        return render_template('favoritos.html',sucesso=sucesso,favoritos=favorito)


@app.route("/excluir_favoritos/<int:id>", methods=['POST'])
@login_required
def excluir_favoritos(id):
    Produto.excluir_favoritos(id, current_user.id)
    flash("Produto removido dos favoritos.", "success")
    return redirect(url_for('favoritos'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form['email']
        telefone = request.form['telefone']
        nome = request.form['nome']
        senha = request.form['senha']
        confirmar_senha = request.form['confirmar_senha']

        usuario = User.get_by_email(email)
        if usuario:
            flash("E-mail já está em uso!", "error")
            return render_template('register.html')

        if senha != confirmar_senha:
            flash("As senhas não coincidem!", "error")
            return render_template('register.html')

        hashed_senha = generate_password_hash(senha)

        User.create(nome=nome, email=email, telefone=telefone, senha=hashed_senha)

        flash("Cadastro realizado com sucesso! Faça login.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = User.get_by_email(email)

        if not usuario:
            flash("E-mail não cadastrado!", "error")
            return render_template('login.html')

        if not check_password_hash(usuario.senha, senha):
            flash("Senha incorreta!", "error")
            return render_template('login.html')

        login_user(usuario, remember=True)

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
    return render_template('produtos.html', produto=produtos)


if __name__ == "__main__":
    app.run(debug=True)


