from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

app = Flask(__name__)
app.secret_key = "CHAVE_SECRETA"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"