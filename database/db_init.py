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

cursor.close()
conexao.close()

print("Banco de dados e tabela criados com sucesso!")
