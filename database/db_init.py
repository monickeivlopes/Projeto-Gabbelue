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
        pro_descricao VARCHAR(255) NULL,
        pro_usr_id INT NULL
               
        
        
    )
""")
cursor.execute("""
        INSERT INTO tb_produtos (pro_name, pro_tipo, pro_carrinho, pro_favoritos, pro_preco, pro_image,pro_descricao) 
    VALUES ('Conjunto Anna', 'Conjunto', FALSE, FALSE,82.00,'../static/images/conjuntoanna.jpg',' Um conjunto elegante e sofisticado, perfeito para ocasiões especiais. Com detalhes delicados e um design moderno, ele adiciona um toque de brilho ao seu visual.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Conjunto Lara', 'Conjunto', FALSE, FALSE,115.90, '../static/images/conjuntolara.jpg','Um conjunto refinado que combina sofisticação e estilo. Ideal para quem busca um acessório marcante e elegante.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Conjunto Liz', 'Conjunto', FALSE, FALSE,72.90, '../static/images/conjuntotrevo.jpg','Inspirado na beleza natural, este conjunto traz um charme delicado e romântico, perfeito para looks casuais e sofisticados.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Conjunto Eunice', 'Conjunto', FALSE, FALSE,69.90, '../static/images/conjuntoeunice.jpg','Com design minimalista e acabamento impecável, este conjunto é a escolha ideal para quem gosta de acessórios discretos, mas cheios de personalidade.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Conjunto Luiza', 'Conjunto', FALSE, FALSE,57.90, '../static/images/conjuntoluiza1.jpg','Um conjunto versátil e charmoso, que combina perfeitamente com diferentes estilos e ocasiões.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Conjunto Livia', 'Conjunto', FALSE, FALSE,99.90, '../static/images/conjuntolivia.jpg',' A união do clássico com o moderno. Seu brilho discreto e design inovador fazem dele um item essencial para qualquer coleção de joias.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Argola Concha', 'Brinco', FALSE, FALSE,39.90, '../static/images/argola1.jpg','Brinco em formato de argola com detalhe em concha, trazendo um toque praiano e sofisticado ao seu look.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Brinco Pétala Dourado', 'Brinco', FALSE, FALSE,42.00, '../static/images/brincopetala1.jpg',' Inspirado na delicadeza das pétalas, este brinco dourado é ideal para quem busca um acessório elegante e romântico.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Brinco Pétala Prata', 'Brinco', FALSE, FALSE,42.00, '../static/images/brincopetala2.jpg',' A versão prateada do Brinco Pétala, oferecendo sofisticação e leveza para compor qualquer visual.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Brinco Bola Dourado', 'Brinco', FALSE, FALSE,49.99, '../static/images/brincobola1.jpg','Um brinco clássico e atemporal, com um toque de brilho dourado que combina com qualquer ocasião.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Brinco Bola Prata', 'Brinco', FALSE, FALSE,49.99, '../static/images/brincobola2.jpg','A versão prateada do Brinco Bola, perfeito para quem prefere acessórios discretos, mas com muito charme.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Brinco Pérola', 'Brinco', FALSE, FALSE,51.99, '../static/images/brincoperola.jpg','Um brinco clássico com pérolas, trazendo sofisticação e elegância para qualquer look.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Colar Vivian', 'Colar', FALSE, FALSE,92.00, '../static/images/colarvivian.jpg','Um colar delicado e sofisticado, perfeito para realçar a feminilidade e a elegância do seu visual.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Mix Colar Lavinia', 'Colar', FALSE, FALSE,99.99, '../static/images/colarlavinia.jpg','Uma combinação moderna de colares em camadas, ideal para um look estiloso e contemporâneo.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Colar Chocker', 'Colar', FALSE, FALSE,69.99, '../static/images/chocker.jpg','Um chocker moderno e versátil, perfeito para quem quer um toque fashion no dia a dia.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Mix Colar Melissa', 'Colar', FALSE, FALSE,102.00, '../static/images/mixmelissa.jpg','Um mix de colares que une diferentes texturas e estilos, criando um visual único e sofisticado.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Duo Pulseira Mazé','Pulseira',False,False,95.00, '../static/images/pulseiramaze.jpg',' Um conjunto de pulseiras que trazem delicadeza e sofisticação, perfeito para compor um visual elegante.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Duo Pulseira Trevo','Pulseira',False,False,89.99, '../static/images/pulseiratrevo.jpg',' Um duo de pulseiras inspirado na sorte e no equilíbrio, ideal para quem gosta de acessórios com significado.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Bracelete Nó Ouro','Pulseira',False,False,129.99, '../static/images/pulseirano1.jpg',' Com um design moderno e sofisticado, este bracelete dourado traz um toque de classe e elegância.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Bracelete Nó Prata','Pulseira',False,False,119.00, '../static/images/pulseirano2.jpg',' A versão prateada do Bracelete Nó, perfeito para compor looks sofisticados e discretos.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Delicado Prata','Anel',False,False,35.00, '../static/images/anelprata1.jpg',' Um anel minimalista e delicado, ideal para compor looks discretos e elegantes.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Coração','Anel',False,False,48.00, '../static/images/anelcoracao.jpg','Com um design romântico e sofisticado, este anel em formato de coração é perfeito para expressar amor e carinho.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Delicado Dourado','Anel',False,False,35.00, '../static/images/anel1.jpg','Uma peça fina e versátil, trazendo um toque de charme ao seu visual.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
                ('Anel Gota Boleado','Anel',False,False,52.00, '../static/images/anelboleano.jpg','Um anel diferenciado, com uma pedra em formato de gota que destaca sua beleza única.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Dedinho Coração','Anel',False,False,39.00, '../static/images/aneldedinho.jpg',' Um anel delicado para o dedo mínimo, com um design de coração charmoso e romântico.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Zircônia Coração','Anel',False,False,57.90, '../static/images/anelzirconia.jpg','Uma peça brilhante e elegante, com uma zircônia central em formato de coração.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.'),
               ('Anel Solitário Brilhante','Anel',False,False,99.90, '../static/images/anelbrilhante.jpg','Um anel clássico e sofisticado, com uma pedra central brilhante que exala elegância.Nossos acessórios são confeccionados com materiais de alta qualidade, combinando a durabilidade da prata 925 e a sofisticação do banho a ouro, com detalhes em zircônia e pedras naturais que garantem brilho e elegância para qualquer ocasião.');
               """)

conexao.commit()


cursor.close()
conexao.close()

print("Banco de dados e tabela criados com sucesso!")
