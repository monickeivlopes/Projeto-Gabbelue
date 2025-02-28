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
    def __init__(self, id, nome, tipo, preco, image, user_id, estoque):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.image = image
        self.user_id = user_id
        self.estoque = estoque
    
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
        query = "SELECT pro_id, pro_nome, pro_tipo, pro_preco, pro_imagem, pro_descricao, pro_estoque FROM tb_produtos JOIN tb_usr_produtos on usp_pro_id = pro_id WHERE usp_usr_id = %s AND usp_carrinho = TRUE;"
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
        query = "SELECT pro_id, pro_nome, pro_tipo, pro_descricao, pro_preco, pro_imagem, pro_estoque FROM tb_produtos JOIN tb_usr_produtos on usp_pro_id = pro_id WHERE usp_usr_id = %s AND usp_favoritos = TRUE;"
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

class Compra():
    def __init__(self, id, user_id, valor, data):
        self.id = id
        self.user_id = user_id
        self.valor = valor
        self.data = data
        
    @staticmethod
    def get(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tb_compras WHERE com_usr_id=%s ",(user_id,))
        result = cursor.fetchall()

        cursor.close()
        conexao.close()
        if result:
            return Compra(*result) 
        return None
    @staticmethod
    def get_compra(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT com_id, com_valor, com_data FROM tb_compras WHERE com_usr_id=%s ",(user_id,))
        result = cursor.fetchall()

        cursor.close()
        conexao.close()
        
        return result
    @staticmethod
    def get_produto(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT com_id, pro_nome, pro_preco, pro_imagem, pro_estoque FROM tb_produtos join tb_com_produtos on cop_pro_id=pro_id join tb_compras on cop_com_id=com_id WHERE com_usr_id=%s",(user_id,))
        result = cursor.fetchall()

        return result
        
    @staticmethod
    def get_id(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT com_id FROM tb_compras WHERE com_usr_id=%s",(user_id,))
        result = cursor.fetchall()

        cursor.close()
        conexao.close()
        return result
    
    def valor_compra(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("select sum(pro_preco) from tb_produtos join tb_usr_produtos on usp_pro_id=pro_id where usp_usr_id=%s and usp_carrinho=1 group by usp_usr_id",(user_id,))
        result = cursor.fetchall()

        cursor.close()
        conexao.close()
        return result
    
    @staticmethod
    def create(user_id, valor):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO tb_compras (com_usr_id, com_valor) VALUES (%s, %s)",
            (user_id, valor)
        )

        conexao.commit()
        cursor.close()
        conexao.close()

    @staticmethod
    def create_com_pro(com_id,pro_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO tb_com_produtos (cop_com_id,cop_pro_id) VALUES (%s, %s)",
            (com_id,pro_id)
        )

        conexao.commit()
        cursor.close()
        conexao.close()
    
    @staticmethod
    def excluir(user_id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("UPDATE tb_usr_produtos SET usp_carrinho = FALSE WHERE usp_usr_id = %s",(user_id,))

        conexao.commit()
        cursor.close()
        conexao.close()