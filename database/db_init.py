import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conexao.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS db_gabbelue")
cursor.execute("USE db_gabbelue")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_users (
        usr_id INT AUTO_INCREMENT PRIMARY KEY,
        usr_name VARCHAR(100) NOT NULL,
        usr_email VARCHAR(100) UNIQUE NOT NULL,
        usr_telephone VARCHAR(20) NOT NULL,
        usr_password VARCHAR(255) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_produtos (
        pro_id INT AUTO_INCREMENT PRIMARY KEY,
        pro_name VARCHAR(100) NOT NULL,
        pro_tipo VARCHAR(50) NOT NULL,
        pro_carrinho BOOLEAN NULL,
        pro_favoritos BOOLEAN NULL,
        pro_preco FLOAT NOT NULL,
        pro_image VARCHAR(255) NULL,
        pro_usr_id INT NULL
        
        
    )
""")
cursor.execute("""
        INSERT INTO tb_produtos (pro_name, pro_tipo, pro_carrinho, pro_favoritos, pro_preco, pro_image) 
    VALUES ('Conjunto Anna', 'Conjunto', FALSE, FALSE,82.00,default),
               ('Conjunto Lara', 'Conjunto', FALSE, FALSE,115.90, default),
               ('Conjunto Liz', 'Conjunto', FALSE, FALSE,72.90, default),
               ('Conjunto Eunice', 'Conjunto', FALSE, FALSE,69.90, default),
               ('Conjunto Luiza', 'Conjunto', FALSE, FALSE,57.90, default),
               ('Conjunto Livia', 'Conjunto', FALSE, FALSE,99.90, default),
               ('Argola Concha', 'Brinco', FALSE, FALSE,39.90, '../static/images/argola1.jpg'),
               ('Brinco Pétala Dourado', 'Brinco', FALSE, FALSE,42.00, '../static/images/brincopetala1.jpg'),
               ('Brinco Pétala Prata', 'Brinco', FALSE, FALSE,42.00, '../static/images/brincopetala2.jpg'),
               ('Brinco Bola Dourado', 'Brinco', FALSE, FALSE,49.99, '../static/images/brincobola1.jpg'),
               ('Brinco Bola Prata', 'Brinco', FALSE, FALSE,49.99, '../static/images/brincobola2.jpg'),
               ('Brinco Pérola', 'Brinco', FALSE, FALSE,51.99, '../static/images/brincoperola.jpg'),
               ('Colar Vivian', 'Colar', FALSE, FALSE,92.00, default),
               ('Mix Colar Lavinia', 'Colar', FALSE, FALSE,99.99, default),
               ('Colar Chocker', 'Colar', FALSE, FALSE,69.99, '../static/images/chocker.jpg'),
               ('Mix Colar Melissa', 'Colar', FALSE, FALSE,102.00, default),
               ('Duo Pulseira Mazé','Pulseira',False,False,95.00, default),
               ('Duo Pulseira Trevo','Pulseira',False,False,89.99, default),
               ('Bracelete Nó Ouro','Pulseira',False,False,129.99, default),
               ('Bracelete Nó Prata','Pulseira',False,False,119.00, default),
               ('Anel Delicado Prata','Anel',False,False,35.00, '../static/images/anelprata.jpg'),
               ('Anel Coração','Anel',False,False,48.00, '../static/images/anelcoracao.jpg'),
               ('Anel Delicado Dourado','Anel',False,False,35.00, '../static/images/anel1.jpg'),
                ('Anel Gota Boleado','Anel',False,False,52.00, '../static/images/anelboleano.jpg'),
               ('Anel Dedinho Coração','Anel',False,False,39.00, '../static/images/aneldedinho.jpg'),
               ('Anel Zircônia Coração','Anel',False,False,57.90, '../static/images/anelzirconia.jpg'),
               ('Anel Solitário Brilhante','Anel',False,False,99.90, '../static/images/anelbrilhante.jpg');
               """)

conexao.commit()


cursor.close()
conexao.close()

print("Banco de dados e tabela criados com sucesso!")
