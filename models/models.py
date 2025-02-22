from flask_login import UserMixin
from ..database import obter_conexao


class User(UserMixin):
    def __init__(self, id, nome, email, telefone, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha

    @staticmethod
    def get(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT usr_id, usr_nome, usr_email, usr_telefone, usr_senha FROM tb_users WHERE usr_id = %s", (user_id,))
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
        cursor.execute("SELECT usr_id, usr_nome, usr_email, usr_telefone, usr_senha FROM tb_users WHERE usr_email = %s", (email,))
        result = cursor.fetchone()

        cursor.close()
        conexao.close()
        if result:
            return User(*result)
        return None

    @staticmethod
    def create(nome, email, telefone, senha):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO tb_users (usr_nome, usr_email, usr_telefone, usr_senha) VALUES (%s, %s, %s, %s)",
            (nome, email, telefone, senha)
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
    def __init__(self, id, nome, tipo, preco, image, user_id):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.image = image
        self.user_id = user_id
    
    @staticmethod
    def get():
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tb_produtos")
        result = cursor.fetchone()

        cursor.close()
        conexao.close()
        if result:
            return Produto(*result) 
        return None
        
    @staticmethod
    def get_id(id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tb_produtos where pro_id = %s",(id,))
        result = cursor.fetchone()

        cursor.close()
        conexao.close()
        return result
    
    @staticmethod
    def select_carrinho(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        query = "SELECT pro_id, pro_nome, pro_tipo, pro_preco, pro_imagem, pro_descricao FROM tb_produtos JOIN tb_usr_produtos on usp_pro_id = pro_id WHERE usp_usr_id = %s AND usp_carrinho = TRUE;"
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
            "SELECT usp_id FROM tb_usr_produtos WHERE usp_pro_id = %s AND usp_usr_id = %s;",
            (pro_id, user_id)
        )
        resultado = cursor.fetchone()

        if resultado:
            cursor.execute(
                "UPDATE tb_usr_produtos SET usp_carrinho = TRUE WHERE usp_pro_id = %s AND usp_usr_id = %s;",
                (pro_id, user_id)
            )
        else:
            cursor.execute(
                "INSERT INTO tb_usr_produtos (usp_usr_id, usp_pro_id, usp_carrinho) VALUES (%s, %s, TRUE);",
                (user_id, pro_id)
            )

        conexao.commit()
        cursor.close()
        conexao.close()
    
    @staticmethod
    def excluir_carrinho(pro_id, user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE tb_usr_produtos SET usp_carrinho = FALSE WHERE usp_pro_id = %s and usp_usr_id = %s;",
            (pro_id, user_id)
        )

        conexao.commit()
        cursor.close()
        conexao.close()

    @staticmethod
    def select_favoritos(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        query = "SELECT pro_id, pro_nome, pro_tipo, pro_preco, pro_imagem, pro_descricao FROM tb_produtos JOIN tb_usr_produtos on usp_pro_id = pro_id WHERE usp_usr_id = %s AND usp_favoritos = TRUE;"
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
            "SELECT usp_id FROM tb_usr_produtos WHERE usp_pro_id = %s AND usp_usr_id = %s;",
            (pro_id, user_id)
        )
        resultado = cursor.fetchone()

        if resultado:
            cursor.execute(
                "UPDATE tb_usr_produtos SET usp_favoritos = TRUE WHERE usp_pro_id = %s AND usp_usr_id = %s;",
                (pro_id, user_id)
            )
        else:
            cursor.execute(
                "INSERT INTO tb_usr_produtos (usp_usr_id, usp_pro_id, usp_favoritos) VALUES (%s, %s, TRUE);",
                (user_id, pro_id)
            )

        conexao.commit()
        cursor.close()
        conexao.close()
    
    @staticmethod
    def excluir_favoritos(pro_id, user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE tb_usr_produtos SET usp_favoritos = FALSE WHERE usp_pro_id = %s and usp_usr_id = %s;",
            (pro_id, user_id)
        )
        
        conexao.commit()
        cursor.close()
        conexao.close()