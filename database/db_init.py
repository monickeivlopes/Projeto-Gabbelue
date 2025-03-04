import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conexao.cursor()

cursor.execute("DROP DATABASE IF EXISTS db_gabbelue")
cursor.execute("CREATE DATABASE IF NOT EXISTS db_gabbelue")
cursor.execute("USE db_gabbelue")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_users (
        usr_id INT AUTO_INCREMENT PRIMARY KEY,
        usr_nome VARCHAR(100) NOT NULL,
        usr_email VARCHAR(100) UNIQUE NOT NULL,
        usr_telefone VARCHAR(20) NOT NULL,
        usr_senha VARCHAR(255) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_produtos (
        pro_id INT AUTO_INCREMENT PRIMARY KEY,
        pro_nome VARCHAR(100) NOT NULL,
        pro_tipo VARCHAR(50) NOT NULL,
        pro_preco DECIMAL(10,2) NOT NULL,
        pro_imagem VARCHAR(255) NULL,
        pro_estoque INT NOT NULL DEFAULT 20,
        pro_descricao TEXT NULL,
        pro_usr_id INT NULL,
        FOREIGN KEY (pro_usr_id) REFERENCES tb_users(usr_id) ON DELETE SET NULL ON UPDATE CASCADE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_usr_produtos (
        usp_id INT AUTO_INCREMENT PRIMARY KEY,
        usp_usr_id INT NOT NULL,
        usp_pro_id INT NOT NULL,
        usp_carrinho BOOLEAN NOT NULL DEFAULT FALSE,
        usp_favoritos BOOLEAN NOT NULL DEFAULT FALSE,
        FOREIGN KEY (usp_usr_id) REFERENCES tb_users(usr_id) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (usp_pro_id) REFERENCES tb_produtos(pro_id) ON DELETE CASCADE ON UPDATE CASCADE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_compras (
        com_id INT AUTO_INCREMENT PRIMARY KEY,
        com_usr_id INT NOT NULL,
        com_valor DECIMAL(10,2) NOT NULL,
        com_data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (com_usr_id) REFERENCES tb_users(usr_id) ON DELETE CASCADE ON UPDATE CASCADE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_com_produtos (
        cop_id INT AUTO_INCREMENT PRIMARY KEY,
        cop_com_id INT NOT NULL,
        cop_pro_id INT NOT NULL,
        FOREIGN KEY (cop_com_id) REFERENCES tb_compras(com_id) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (cop_pro_id) REFERENCES tb_produtos(pro_id) ON DELETE CASCADE ON UPDATE CASCADE
    )   
""")

cursor.execute("""
        INSERT INTO tb_produtos (pro_nome, pro_tipo, pro_preco, pro_imagem, pro_descricao) 
        VALUES ('Conjunto Anna', 'Conjunto',82.00,'../static/images/conjuntoanna.jpg',' Um conjunto elegante e sofisticado, perfeito para ocasiões especiais. Com detalhes delicados e um design moderno, ele adiciona um toque de brilho ao seu visual.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Conjunto Lara', 'Conjunto',115.90, '../static/images/conjuntolara.jpg','Um conjunto refinado que combina sofisticação e estilo. Ideal para quem busca um acessório marcante e elegante.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Conjunto Liz', 'Conjunto',72.90, '../static/images/conjuntotrevo.jpg','Inspirado na beleza natural, este conjunto traz um charme delicado e romântico, perfeito para looks casuais e sofisticados.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Conjunto Eunice', 'Conjunto',69.90, '../static/images/conjuntoeunice.jpg','Com design minimalista e acabamento impecável, este conjunto é a escolha ideal para quem gosta de acessórios discretos, mas cheios de personalidade.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Conjunto Luiza', 'Conjunto',57.90, '../static/images/conjuntoluiza1.jpg','Um conjunto versátil e charmoso, que combina perfeitamente com diferentes estilos e ocasiões.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Conjunto Livia', 'Conjunto',99.90, '../static/images/conjuntolivia.jpg',' A união do clássico com o moderno. Seu brilho discreto e design inovador fazem dele um item essencial para qualquer coleção de joias.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Argola Concha', 'Brinco',39.90, '../static/images/argola1.jpg','Brinco em formato de argola com detalhe em concha, trazendo um toque praiano e sofisticado ao seu look.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Brinco Pétala Dourado', 'Brinco',42.00, '../static/images/brincopetala1.jpg',' Inspirado na delicadeza das pétalas, este brinco dourado é ideal para quem busca um acessório elegante e romântico.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Brinco Pétala Prata', 'Brinco',42.00, '../static/images/brincopetala2.jpg',' A versão prateada do Brinco Pétala, oferecendo sofisticação e leveza para compor qualquer visual.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Brinco Bola Dourado', 'Brinco',49.99, '../static/images/brincobola1.jpg','Um brinco clássico e atemporal, com um toque de brilho dourado que combina com qualquer ocasião.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Brinco Bola Prata', 'Brinco',49.99, '../static/images/brincobola2.jpg','A versão prateada do Brinco Bola, perfeito para quem prefere acessórios discretos, mas com muito charme.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Brinco Pérola', 'Brinco',51.99, '../static/images/brincoperola.jpg','Um brinco clássico com pérolas, trazendo sofisticação e elegância para qualquer look.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Colar Vivian', 'Colar',92.00, '../static/images/colarvivian.jpg','Um colar delicado e sofisticado, perfeito para realçar a feminilidade e a elegância do seu visual.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Mix Colar Lavinia', 'Colar',99.99, '../static/images/colarlavinia.jpg','Uma combinação moderna de colares em camadas, ideal para um look estiloso e contemporâneo.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Colar Chocker', 'Colar',69.99, '../static/images/chocker.jpg','Um chocker moderno e versátil, perfeito para quem quer um toque fashion no dia a dia.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Mix Colar Melissa', 'Colar',102.00, '../static/images/mixmelissa.jpg','Um mix de colares que une diferentes texturas e estilos, criando um visual único e sofisticado.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Duo Pulseira Mazé','Pulseira',95.00, '../static/images/pulseiramaze.jpg',' Um conjunto de pulseiras que trazem delicadeza e sofisticação, perfeito para compor um visual elegante.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Duo Pulseira Trevo','Pulseira',89.99, '../static/images/pulseiratrevo.jpg',' Um duo de pulseiras inspirado na sorte e no equilíbrio, ideal para quem gosta de acessórios com significado.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Bracelete Nó Ouro','Pulseira',129.99, '../static/images/pulseirano1.jpg',' Com um design moderno e sofisticado, este bracelete dourado traz um toque de classe e elegância.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Bracelete Nó Prata','Pulseira',119.00, '../static/images/pulseirano2.jpg',' A versão prateada do Bracelete Nó, perfeito para compor looks sofisticados e discretos.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Delicado Prata','Anel',35.00, '../static/images/anelprata1.jpg',' Um anel minimalista e delicado, ideal para compor looks discretos e elegantes.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Coração','Anel',48.00, '../static/images/anelcoracao.jpg','Com um design romântico e sofisticado, este anel em formato de coração é perfeito para expressar amor e carinho.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Delicado Dourado','Anel',35.00, '../static/images/anel1.jpg','Uma peça fina e versátil, trazendo um toque de charme ao seu visual.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Gota Boleado','Anel',52.00, '../static/images/anelboleado.jpg','Um anel diferenciado, com uma pedra em formato de gota que destaca sua beleza única.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Dedinho Coração','Anel',39.00, '../static/images/aneldedinho.jpg',' Um anel delicado para o dedo mínimo, com um design de coração charmoso e romântico.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Zircônia Coração','Anel',57.90, '../static/images/anelzirconia.jpg','Uma peça brilhante e elegante, com uma zircônia central em formato de coração.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Solitário Brilhante','Anel',99.90, '../static/images/anelbrilhante.jpg','Um anel clássico e sofisticado, com uma pedra central brilhante que exala elegância.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.')
               """)

conexao.commit()


cursor.close()
conexao.close()

print("Banco de dados e tabela criados com sucesso!")

