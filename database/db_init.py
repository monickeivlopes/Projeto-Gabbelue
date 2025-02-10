import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conexao.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS db_mais_unidos")
cursor.execute("USE db_mais_unidos")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        telephone VARCHAR(20) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

cursor.close()
conexao.close()

print("Banco de dados e tabela criados com sucesso!")
