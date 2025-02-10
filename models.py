from flask_login import UserMixin
from database.db_config import obter_conexao


class User(UserMixin):
    def __init__(self, id, name, email, telephone, password):
        self.id = id
        self.name = name
        self.email = email
        self.telephone = telephone
        self.password = password

    @staticmethod
    def get(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT usr_id, usr_name, usr_email, usr_telephone, usr_password FROM tb_users WHERE usr_id = %s", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        conexao.close()
        if result:
            return User(*result) 
        return None

    @staticmethod
    def get_by_email(email):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT usr_id, usr_name, usr_email, usr_telephone, usr_password FROM tb_users WHERE usr_email = %s", (email,))
        result = cursor.fetchone()
        cursor.close()
        conexao.close()
        if result:
            return User(*result)
        return None

    @staticmethod
    def create(name, email, telephone, password):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO tb_users (usr_name, usr_email, usr_telephone, usr_password) VALUES (%s, %s, %s, %s)",
            (name, email, telephone, password)
        )
        conexao.commit()
        cursor.close()
        conexao.close()

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False
