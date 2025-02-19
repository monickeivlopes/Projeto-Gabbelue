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

class Produto():
    def __init__(self, id, name, tipo, preco, favoritos, carrinho, image, user_id):
        self.id = id
        self.name = name
        self.tipo = tipo
        self.preco = preco
        self.favoritos = favoritos
        self.carrinho = carrinho
        self.image = image
        self.user_id = user_id
    
    @staticmethod
    def get(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tb_produtos WHERE usr_id = %s", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        conexao.close()
        if result:
            return User(*result) 
        return None
    
    @staticmethod
    def select_carrinho(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        query = "SELECT * FROM tb_produtos WHERE pro_usr_id = %s AND pro_carrinho = True"
        cursor.execute(query, (user_id,))
        carrinho = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        return carrinho
    
    @staticmethod
    def add_carrinho(pro_id, user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE tb_produtos SET pro_carrinho = TRUE, pro_usr_id = %s WHERE pro_id = %s;",
            (user_id,pro_id)
        )
        conexao.commit()
        cursor.close()
        conexao.close()
    
    @staticmethod
    def excluir_carrinho(pro_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE tb_produtos SET pro_carrinho = False, pro_usr_id = NULL WHERE pro_id =%s ;",
            (pro_id,)
        )
        conexao.commit()
        cursor.close()
        conexao.close()

    @staticmethod
    def select_favoritos(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        query = "SELECT * FROM tb_produtos WHERE pro_usr_id = %s AND pro_favoritos = True"
        cursor.execute(query, (user_id,))
        favoritos = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        return favoritos
    
    @staticmethod
    def add_favoritos(pro_id, user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE tb_produtos SET pro_favoritos = TRUE, pro_usr_id = %s WHERE pro_id = %s;",
            (user_id,pro_id)
        )
        conexao.commit()
        cursor.close()
        conexao.close()
    
    @staticmethod
    def excluir_favoritos(pro_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "update tb_produtos set pro_favoritos=False, pro_usr_id=NULL where pro_id=%s;",
            (pro_id,)
        )
        conexao.commit()
        cursor.close()
        conexao.close()