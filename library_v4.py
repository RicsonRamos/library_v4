import os
import time 
from datetime import datetime, timedelta

usuarios = {
    '01': ['Ana Silva', 'Rua das Flores', '876', '16738716789', 'ana_silva@mail.com', '(31) 99876-5674', '05/05/1985', 'Engenheira'],
    '02': ['Pedro Santos', 'Avenida Central', '543', '16738716790', 'pedro_santos@mail.com', '(31) 99876-5674', '20/03/1992', 'Estudante'],
    '03': ['Carla Oliveira', 'Praça da Liberdade', '321', '16738716789', 'carla_o@mail.com', '(31) 99876-5674', '15/09/1988', 'Advogada'],
    '04': ['Lucas Fernandes', 'Rua dos Girassóis', '432', '16738716789', 'lucas_f@mail.com', '(31) 99876-5674', '23/07/1995', 'Estudante'],
    '05': ['Mariana Lima', 'Avenida Paulista', '789', '16738716790', 'mariana_l@mail.com', '(31) 99876-5674', '10/12/1983', 'Médica'],
    '06': ['Rafaela Costa', 'Rua das Palmeiras', '654', '16738716789', 'rafaela_c@mail.com', '(31) 99876-5674', '02/04/1990', 'Engenheira Civil'],
    '07': ['Bruno Santos', 'Rua do Sol', '987', '16738716790', 'bruno_s@mail.com', '(31) 99876-5674', '18/11/1980', 'Programador'],
    '08': ['Fernanda Almeida', 'Avenida Atlântica', '123', '16738716789', 'fernanda_a@mail.com', '(31) 99876-5674', '07/06/1993', 'Designer'],
    '09': ['Mariana Oliveira', 'Avenida das Flores', '345', '16738716789', 'mariana_o@mail.com', '(31) 99876-5674', '15/09/1987', 'Arquiteta'],
    '10': ['Gustavo Silva', 'Rua dos Passarinhos', '567', '16738716790', 'gustavo_s@mail.com', '(31) 99876-5674', '29/02/1992', 'Biólogo'],
    '11': ['Roberta Mendonça', 'Rua da Paz', '876', '16738716789', 'roberta_m@mail.com', '(31) 99876-5674', '11/03/1986', 'Farmacêutica'],
    '12': ['Ricardo Pereira', 'Avenida das Palmeiras', '321', '16738716789', 'ricardo_p@mail.com', '(31) 99876-5674', '25/08/1990', 'Engenheiro Civil'],
    '13': ['Isabela Lima', 'Rua dos Coqueiros', '654', '16738716789', 'isabela_l@mail.com', '(31) 99876-5674', '03/12/1983', 'Psicóloga'],
    '14': ['Paulo Oliveira', 'Avenida dos Pássaros', '987', '16738716790', 'paulo_o@mail.com', '(31) 99876-5674', '19/07/1980', 'Professor'],
    '15': ['Fernanda Costa', 'Rua dos Cravos', '123', '16738716789', 'fernanda_c@mail.com', '(31) 99876-5674', '12/05/1989', 'Fotógrafa'],
    '16': ['Diego Santos', 'Avenida dos Girassóis', '345', '16738716790', 'diego_s@mail.com', '(31) 99876-5674', '28/09/1984', 'Engenheiro Eletricista'],
    '17': ['Aline Ferreira', 'Rua das Margaridas', '567', '16738716789', 'aline_f@mail.com', '(31) 99876-5674', '06/02/1991', 'Nutricionista'],
    '18': ['Rodrigo Oliveira', 'Avenida dos Ipês', '876', '16738716790', 'rodrigo_o@mail.com', '(31) 99876-5674', '17/10/1982', 'Analista de Sistemas'],
    '19': ['Tatiana Lima', 'Rua das Orquídeas', '321', '16738716789', 'tatiana_l@mail.com', '(31) 99876-5674', '21/06/1987', 'Designer de Interiores'],
    '20': ['Marcos Silva', 'Avenida das Tulipas', '654', '16738716790', 'marcos_s@mail.com', '(31) 99876-5674', '14/04/1981', 'Advogado'],
    '21': ['Juliana Ferreira', 'Rua dos Jasmins', '987', '16738716789', 'juliana_f@mail.com', '(31) 99876-5674', '09/11/1986', 'Biomédica'],
    '22': ['Gabriel Oliveira', 'Avenida das Rosas', '123', '16738716790', 'gabriel_o@mail.com', '(31) 99876-5674', '30/08/1991', 'Arquiteto'],
    '23': ['Amanda Santos', 'Rua das Violetas', '345', '16738716789', 'amanda_s@mail.com', '(31) 99876-5674', '05/03/1985', 'Enfermeira'],
    '24': ['Vinícius Lima', 'Avenida das Bromélias', '567', '16738716790', 'vinicius_l@mail.com', '(31) 99876-5674', '22/01/1989', 'Analista Financeiro'],
    '25': ['Renata Ferreira', 'Rua das Begônias', '876', '16738716789', 'renata_f@mail.com', '(31) 99876-5674', '28/06/1984', 'Química'],
    '26': ['Thiago Oliveira', 'Avenida dos Crisântemos', '321', '16738716790', 'thiago_o@mail.com', '(31) 99876-5674', '03/09/1989', 'Engenheiro de Software'],
    '27': ['Vanessa Lima', 'Rua das Azaléias', '654', '16738716789', 'vanessa_l@mail.com', '(31) 99876-5674', '08/05/1983', 'Arquiteta de Interiores'],
    '28': ['Alexandre Silva', 'Avenida dos Lírios', '987', '16738716790', 'alexandre_s@mail.com', '(31) 99876-5674', '15/02/1988', 'Consultor de Marketing'],
    '29': ['Camila Santos', 'Rua das Camélias', '123', '16738716789', 'camila_s@mail.com', '(31) 99876-5674', '27/07/1982', 'Psiquiatra'],
    '30': ['Marcelo Oliveira', 'Avenida das Papoulas', '345', '16738716790', 'marcelo_o@mail.com', '(31) 99876-5674', '10/04/1987', 'Biomédico']
}
    
livros = {
    'Dom Casmurro': ['Machado de Assis', '9788538068834', 'Romance', '1899'],
    'O Pequeno Príncipe': ['Antoine de Saint-Exupéry', '9788572329593', 'Fábula', '1943'],
    '1984': ['George Orwell', '9788535914849', 'Ficção Científica', '1949'],
    'A Metamorfose': ['Franz Kafka', '9788525416595', 'Ficção', '1915', '4'],
    'Cem Anos de Solidão': ['Gabriel García Márquez', '9788535901450', 'Realismo Mágico', '1967'],
    'A Revolução dos Bichos': ['George Orwell', '9788525433141', 'Sátira', '1945'],
    'Crime e Castigo': ['Fiódor Dostoiévski', '9788573261865', 'Romance', '1866'],
    'Orgulho e Preconceito': ['Jane Austen', '9788535909722', 'Romance', '1813'],
    'Fahrenheit 451': ['Ray Bradbury', '9788576571478', 'Ficção Científica', '1953'],
    'O Senhor dos Anéis: A Sociedade do Anel': ['J.R.R. Tolkien', '9788578270692', 'Fantasia', '1954'],
    'O Apanhador no Campo de Centeio': ['J.D. Salinger', '9788532501951', 'Romance', '1951'],
    '2001: Uma Odisséia no Espaço': ['Arthur C. Clarke', '9788576570556', 'Ficção Científica', '1968'],
    'As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa': ['C.S. Lewis', '9788578270692', 'Fantasia', '1950'],
    'O Senhor dos Anéis': ['J.R.R. Tolkien', '9788533615244', 'Fantasia', '1954'],
    'Harry Potter e a Pedra Filosofal': ['J.K. Rowling', '9788532530782', 'Fantasia', '1997'],
    'Cem Anos de Solidão': ['Gabriel García Márquez', '9788501109650', 'Realismo Mágico', '1967'],
    'A Metamorfose': ['Franz Kafka', '9788537803981', 'Ficção Absurda', '1915'],
    'Orgulho e Preconceito': ['Jane Austen', '9788535909531', 'Romance', '1813'],
    'Crime e Castigo': ['Fiódor Dostoiévski', '9788573261860', 'Romance Psicológico', '1866'],
    'A Revolução dos Bichos': ['George Orwell', '9788520933945', 'Sátira Política', '1945'],
    'A Ilha do Tesouro': ['Robert Louis Stevenson', '9788582181118', 'Aventura', '1883'],
    'A Arte da Guerra': ['Sun Tzu', '9788539302753', 'Estratégia Militar', 'século IV a.C.'],
    'A Culpa é das Estrelas': ['John Green', '9788580572180', 'Romance', '2012'],
    '1984': ['George Orwell', '9788535914849', 'Ficção Distópica', '1949'],
    'O Código Da Vinci': ['Dan Brown', '9788532525610', 'Mistério', '2003'],
    'O Diário de Anne Frank': ['Anne Frank', '9788580572890', 'Autobiografia', '1947'],
    'Drácula': ['Bram Stoker', '9788563560002', 'Terror Gótico', '1897'],
    'O Hobbit': ['J.R.R. Tolkien', '9788595083647', 'Fantasia', '1937'],
    'O Grande Gatsby': ['F. Scott Fitzgerald', '9788535906943', 'Romance', '1925'],
    'As Aventuras de Sherlock Holmes': ['Arthur Conan Doyle', '9788572329661', 'Romance Policial', '1892'],
    'Dom Quixote': ['Miguel de Cervantes', '9788572322655', 'Romance de Cavalaria', '1605'],
    'O Retrato de Dorian Gray': ['Oscar Wilde', '9788525406490', 'Romance Gótico', '1890'],
    'Frankenstein': ['Mary Shelley', '9788537813553', 'Ficção Científica', '1818']
}

emprestimos = {
    'Dom Casmurro':['9788538068833', 'Ana paula' , '2024-04-29', '2024-05-13'],
    'Frankenstein':['9788537813553', 'Paulo Vieira', '2024-04-29', '2024-05-13'],
    'As Aventuras de PI':['9788538068834', 'Ana flávia' , '2024-04-29', '2024-05-13'],
    'Pequeno Príncipe':[ '9788537813555', 'João Victor', '2024-04-29', '2024-05-13'],
    'Up':[ '9788537813557', 'Paulo Vitor', '2024-04-29', '2024-05-13']
}

qte_usuarios =  len(usuarios)
qte_livros = len(livros)
qte_acervo = len(livros) + len(emprestimos)

def cabecalho(titulo, subtitulo):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=' * 80)
    print(titulo.center(80))
    print(subtitulo.center(80))
    print('=' * 80)
cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")

def lista_usuarios(usuarios):
    opcao = 0
    while opcao != "6":
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
        print("Usuários\n".center(80))
        print(
              "1. Listar todos\n"
              "2. Pesquisa Usuário \n"
              "3. Incluir\n"
              "4. Alterar\n"
              "5. Excluir\n"
              "\n6. Voltar\n")
        opcao = input("Digite a opcao desejada: ")
        while opcao not in "123456":
            opcao = input("Opção inválida! Digite a opcao desejada de 1 à 6: ")

           
        if opcao == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
            print("Usuários\n".center(80))
            print('ID    CPF        Nome\n') 
            for ID in usuarios.keys():
                print(f'{ID}    {usuarios[ID][3]}   {usuarios[ID][0]}')

                '''
                print(f"\n  -- Usuário {contagem} --\n")
                print(f"CPF: {pessoa}\n"
                      f"Nome: {usuarios[pessoa][0]}\n"
                      f"Rua: {usuarios[pessoa][1]}\n"
                      f"Número: {usuarios[pessoa][2]}\n"
                      f"CEP: {usuarios[pessoa][3]}")
                print("E-mail(s):")
                for endereço in usuarios[pessoa][4]:
                    print(f"\t{endereço}")
                print("Telefone(s):")
                for telefone in usuarios[pessoa][5]:
                    print(f"\t{telefone}")
                print(f"Data de nascimento: {usuarios[pessoa][6]}\n"
                      f"Profissão: {usuarios[pessoa][7]}")
                contagem += 1
              '''
            if len(usuarios) == 0:
                print("Não existem usuarios cadastrados")
          

            voltar = print(input("\nAperte enter para voltar: "))
          
                      
        if opcao == "2":
            pessoa = input("\nDigite o ID: ").strip()
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
            print("Usuários\n".center(80))
            if pessoa not in usuarios.keys():
                print("ID não cadastrado.")
            else:
                print(f"\nNome: {usuarios[pessoa][0]}")
                print(f"Rua: {usuarios[pessoa][1]}")
                print(f"Número: {usuarios[pessoa][2]}")
                print(f"CEP: {usuarios[pessoa][3]}")
                for end in usuarios[pessoa][4]:
                    print(f"E-mail(s): {end}")
                for num in usuarios[pessoa][5]:
                    print(f"Telefone(s): {num}")
                print(f"Data de nascimento: {usuarios[pessoa][6]}")
                print(f"Profissão: {usuarios[pessoa][7]}")

            voltar = print(input("\nAperte enter para voltar: "))   
                            

        if opcao == "3":
            num_cpf = input("CPF (somente números): ").strip()
            while len(num_cpf) != 11 or num_cpf.isdigit() == False :
                num_cpf = input("CPF inválido. Digite o CPF (somente números): ").strip()
            for num_cpf, dados in usuarios.items():
                nome, rua, numero, cpf, email,  telefone, nascimento, profissao = dados
                if num_cpf == cpf:
                    print("CPF já cadastrado.")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
                    print('Usuários'.center(80))
                    usuario_novo = {}
                    id = len(usuarios) + 1
                    nome = input("\nInsira o Nome do Usuário: ")
                    rua = input("Insira o Endereço do Usuário: ")
                    numero = input("Insira o número da residência do Usuário: ")
                    cpf = input("Insira o CPF do Usuário: ")
                    email = input("Insira o email 1 do Usuário: ")
                    telefone = input("Insira o telefone 1 do Usuário: ")
                    nascimento = input("Insira a data de nascimento do Usuário: ") 
                    profissao = input("Insira a profissão do Usuário: ")

                    usuario_novo[id] = [nome, rua, numero, cpf, email, telefone, nascimento, profissao]

                    os.system('cls' if os.name == 'nt' else 'clear')
                    cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
                    print('Usuários'.center(80))
                    print("\nNovo Usuário adicionado:")
                    print(f"Nome: {nome}")
                    print(f"Rua: {rua}")
                    print(f"Número: {numero}")
                    print(f"CPF: {cpf}")
                    print(f"Email: {email}")
                    print(f"Telefone: {telefone}")
                    print(f"Data de Nascimento: {nascimento}")
                    print(f"Profissão: {profissao}")

                    print("\nLivro Adicionado com Sucesso!")
                
                    time.sleep(3)
                    break
            usuarios.update(usuario_novo)
                

            print(input("\nAperte enter para voltar: "))
            
        if opcao == "4":
            pessoa = input("Digite o CPF: ").strip()
            if pessoa not in usuarios.keys():
                print("CPF não cadastrado.")
            else:
                print(f"\nUsuário: {usuarios[pessoa][0]}\n"
                      "-- Digite apenas os dados que serão alterados: ")
                nome = input("Nome: ").strip()
                if len(nome) > 0:
                    usuarios[pessoa][0] = nome
                rua = input("Rua: ").strip()
                if len(rua) > 0:
                    usuarios[pessoa][1] = rua
                número = input("Número: ").strip()
                if len(número) > 0:
                    usuarios[pessoa][2] = número
                CEP = input("CEP: ")
                if len(CEP) > 0:
                    while len(CEP) != 8 or CEP.isdigit() == False:
                        CEP = input("CEP inválido. Digite o CEP (somente números): ").strip()
                    usuarios[pessoa][3] = CEP
                email = input("E-mail: ").strip()
                if email not in usuarios[pessoa][4]:
                    if len(email) != 0:
                        usuarios[pessoa][4].append(email)
                else:
                    print("E-mail já cadastrado.")
                telefone = input("Telefone: ")
                if telefone not in usuarios[pessoa][5]:
                    if len(telefone) != 0:
                        usuarios[pessoa][5].append(telefone)
                else:
                    print("Telefone já cadastrado.")
                data_nascimento = input("Data de nascimento: ")
                if len(data_nascimento) > 0:
                    usuarios[pessoa][6] = data_nascimento
                profissão = input("Profissão: ")
                if len(profissão) > 0:
                    usuarios[pessoa][7] = profissão
                print("Dados alterados com sucesso!")

            voltar = print(input("\nAperte enter para voltar: "))
                                
        if opcao == "5":
            pessoa = input("Digite o CPF: ").strip()
            if pessoa not in usuarios:
                print("CPF não cadastrado.")
                time.sleep(2)
              
            else:
                print(f"\nExcluir usuário: {usuarios[pessoa][0]}")
                resposta = input("Confirmar? [S/N]: ").upper().strip()
                while resposta not in "SN":
                    resposta = input("Resposta inválida. Responda S ou N: ").upper().strip()
                if resposta == "S":
                    print(f"Usuário --{usuarios[pessoa][0]}-- excluído com sucesso.")
                    del usuarios[pessoa]

#Concertar validacao cpf antes de inlcuir usuario, excluir opcao de alterar, configurar opçao de excluir

def lista_livros(livros):
    opcao = 0
    while opcao != "6":
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
        print('Livros'.center(80))
        print(
              "1. Listar todos\n"
              "2. Pesquisa Livro \n"
              "3. Incluir\n"
              "4. Excluir\n"
              "\n6. Voltar\n")
        opcao = input("Digite a opcao desejada: ")
        while opcao not in "123456":
            opcao = input("Opção inválida! Digite a opcao desejada de 1 à 6: ")
            
        if opcao == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
            print('Livros'.center(80))
            print("\nISBN                   Titulo\n")
            for livro, dados in sorted(livros.items()):
                autor, isbn, genero, ano = dados
                print(f'{isbn}      {livro} - {autor}')
            if len(livros) == 0:
                print("Não existem livros cadastrados.")
            
            print(input("\nAperte enter para voltar: "))
    
        elif opcao == "2":        
            isbn_livro = input("\nDigite o ISBN do livro que deseja listar: ").strip()
            livro_encontrado = False

            for livro, dados in livros.items():
                autor, isbn, genero, ano = dados
                if isbn_livro == isbn:
                    livro_encontrado = True
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
                    print('Livros'.center(80))
                    print('Livros'.center(80))
                    print(f"\n\nTítulo: {livro}")
                    print(f"Autor: {autor}")
                    print(f"ISBN: {isbn}")
                    print(f"Gênero: {genero}")
                    print(f"Ano: {ano}")
                    break

            if not livro_encontrado:
                os.system('cls' if os.name == 'nt' else 'clear')
                cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
                print('Livros'.center(80))
                print("\n\nLivro não cadastrado!")


            input("\nAperte enter para voltar: ")

        elif opcao == "3":
            for livro, dados in livros.items():
                autor, isbn, genero, ano = dados
                isbn_livro = input("\nISBN do livro a ser cadastrado: ").strip()
                while len(isbn_livro) != 13 or not isbn_livro.isdigit():
                    isbn_livro = input("ISBN inválido. Digite o ISBN do Livro (somente números): ").strip()
                
                if isbn_livro in isbn:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
                    print('Livros'.center(80))
                    print("Livro já cadastrado")
                    time.sleep(3)
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
                    print('Livros'.center(80))
                    livro_novo = {}
                    titulo = input("\nInsira o Título do livro: ")
                    autor = input("Insira o Autor do livro: ")
                    genero = input("Insira o Gênero do livro: ")
                    ano = input("Insira o Ano de publicação do livro: ")

                    livro_novo[titulo] = [autor, isbn_livro, genero, ano]

                    os.system('cls' if os.name == 'nt' else 'clear')
                    cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
                    print('Livros'.center(80))
                    print("\nNovo livro adicionado:")
                    print(f"Título: {titulo}")
                    print(f"Autor: {autor}")
                    print(f"ISBN: {isbn_livro}")
                    print(f"Gênero: {genero}")
                    print(f"Ano: {ano}")

                    print("\nLivro Adicionado com Sucesso!")
                    time.sleep(3)
                    break
            livros.update(livro_novo)

        elif opcao == "4":
            isbn_livro = input("\nDigite o ISBN do livro que deseja listar: ").strip()
            livro_encontrado = False

            for livro, dados in livros.items():
                autor, isbn, genero, ano = dados
                if isbn_livro == isbn:
                    livro_encontrado = True
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
                    print('Livros'.center(80))
                    print("ISBN não cadastrado.")

            if livro_encontrado:
                print(f"\n\nLivro encontrado:")
                print(f"Título: {livro}")
                print(f"Autor: {autor}")
                print(f"ISBN: {isbn}")
                print(f"Gênero: {genero}")
                print(f"Ano: {ano}")

                confirmacao = input("\nDeseja excluir este livro? [S/N]: ").upper().strip()
                if confirmacao == "S":
                    print(f"\nExcluindo livro: {livro}")
                    del livros[livro]
                    print("Livro excluído com sucesso.")
                else:
                    print("Operação de exclusão cancelada.")
            if not livro_encontrado:
                print("Livro não encontrado!")

#completo 

def sub_emprestimos(usuarios, livros):
    os.system('cls' if os.name == 'nt' else 'clear')
    cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
    print("Empréstimos\n".center(80))
    print(
          "1. Listar todos\n"
          "2. Pesquisa Empréstimo \n"
          "3. Realizar Empréstimo\n"
          "4. Realizar Devolução\n"
          "\n6. Voltar\n")
    opcao = input("Digite a opcao desejada: ")
    while opcao not in "123456":
        opcao = input("Opção inválida! Digite a opcao desejada de 1 à 6: ")

    if opcao == "1": 
        for emprestimo in emprestimos:
            print(emprestimo)
        if len(emprestimos) == 0:
            print("Não existem emprestimos cadastrados.")
            
    if opcao == "2":
        titulo_livro = input("Digite o Título do livro emprestado: ")

        if titulo_livro in emprestimos:
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
            print("Empréstimo\n".center(80))
            print(f'\n\nO livro "{titulo_livro}" foi emprestado.')
            time.sleep(3)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
            print("Empréstimo\n".center(80))
            print("\n\nEste empréstimo não está registrado.")
            time.sleep(3)

                
    if opcao == "3":
        emprest = {}      
        titulo_empre = input("Digite o Título do livro: ")

        if titulo_empre not in livros:
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
            print("Empréstimos\n".center(80))
            print("Empréstimo não cadastrado.")
            time.sleep(3)
        elif emprestimos.get(titulo_empre) is not None:
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
            print("Empréstimos\n".center(80))
            print("Este livro já está emprestado.")
            time.sleep(3)
        else:
            print(f"Realizar empréstimo: {livros[titulo_empre]}")
            resposta = input("Confirmar? [S/N]: ").upper().strip()
            while resposta not in "SN":
                resposta = input("Resposta inválida. Responda S ou N: ").upper().strip()
            if resposta == "S":
                os.system('cls' if os.name == 'nt' else 'clear')
                cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
                print("Empréstimos\n".center(80))
                print("Empréstimo realizado com sucesso.")
                time.sleep(3)
                del livros[titulo_empre]

    
            
    if opcao == "4":
        emprest_dev = {}      
        titulo_dev = input("Digite o Título do livro: ")

        if titulo_dev not in emprestimos:
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
            print("Empréstimos\n".center(80))
            print("Empréstimo não cadastrado.")
            time.sleep(3)
        elif emprestimos[titulo_dev] is None:
            os.system('cls' if os.name == 'nt' else 'clear')
            cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
            print("Empréstimos\n".center(80))
            print("Este livro não está emprestado.")
            time.sleep(3)
        else:
            print(f"Realizar devolução: {emprestimos[titulo_dev]}")
            resposta = input("Confirmar? [S/N]: ").upper().strip()
            while resposta not in "SN":
                resposta = input("Resposta inválida. Responda S ou N: ").upper().strip()
            if resposta == "S":
                os.system('cls' if os.name == 'nt' else 'clear')
                cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
                print("Empréstimos\n".center(80))
                print("Devolução realizada com sucesso.")
                time.sleep(3)
                del emprestimos[titulo_dev]

    

def usuarios_idade(usuarios, idade):
    
    quantidade = 0
    for pessoa in usuarios.keys():
        idade_usuário = datetime.now().year - int(usuarios[pessoa][6][-4:])
        if idade_usuário > idade:
            print(f"\nNome: {usuarios[pessoa][0]}\n"
                  f"Rua: {usuarios[pessoa][1]}\n"
                  f"Número: {usuarios[pessoa][2]}\n"
                  f"CEP: {usuarios[pessoa][3]}\n"
                  "E-mail(s):")
            for end in usuarios[pessoa][4]:
                print(f"\t{end}")
            print("Telefone(s): ")
            for tel in usuarios[pessoa][5]:
                print(f"\t{tel}")
            print(f"Data de nascimento: {usuarios[pessoa][6]}\n"
                  f"Profissão: {usuarios[pessoa][7]}")
            quantidade += 1
    print(f"\nQuantidade de usuarios com idade maior que {idade} anos: {quantidade}.")
    if quantidade == 0:
        print(f"Não existem usuarios cadastrados com mais de {idade} anos.")

#falta mexer
def autores_livro(livros, quantidade):
    quant_livros = 0
    for livro in livros:
        quant_autores = 0
        for autores in livros[livro][2]:
            quant_autores += 1
        if quant_autores >= quantidade:
            print(f"\nISBN: {livro}\n"
                  f"Título: {livros[livro][0]}\n"
                  f"Gênero: {livros[livro][1]}\n"
                  "Autor(es):")
            for nome in livros[livro][2]:
                print(f"\t{nome}")
            print(f"Número de páginas: {livros[livro][3]}")
            quant_livros += 1
    if quant_livros == 0:
        print(f"Não existem livros cadastrados com mais que {quantidade} autores.")
#falta mexer

def dados_emprestimos():
    # Obter a data atual
    data_atual = datetime.now().strftime("%Y-%m-%d")

    # Calcular a data de devolução (5 dias a partir da data atual)
    data_devolucao = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")

    # Verificar se o livro e o usuário existem nos dicionários
    novo_emprestimo = {}

    for livro, dados_livro in livros.items():
        autor, isbn, genero, ano = dados_livro
        
    for usuario, dados_usuarios in usuarios.items():
        nome, endereco, num, cpf, email, tel, nasciumento, profissao  = dados_usuarios

    if livro in livros.items() and usuario in usuarios.items():
        # Adicionar o empréstimo ao dicionário novo_emprestimo
        print("Empréstimo realizado com sucesso!")
        print("Detalhes do empréstimo:")
        print(f"Título: {livro}")
        print(f"ISBN: {isbn}")
        print(f"Nome do usuário: {nome}")
        print(f"Data de empréstimo: {data_atual}")
        print(f"Data de devolução: {data_devolucao}")
    else:
        print("Livro ou usuário não encontrado!")


#falta mexer             

def relatorios():
    os.system('cls' if os.name == 'nt' else 'clear')
    cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
    print("Relatórios\n".center(80))
    print(
          "1. Lista livros emprestados\n"
          "2. Qte Livros emprestados\n"
          "3. Qte acervo\n"
          "4. Qte Usuários\n"
          "\n6. Voltar\n")
    
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
        print("Relatórios\n".center(80))
        print('Titulo       ISBN           USUÁRIO     EMPRESTIMO    DEVOLUÇÃO\n')
        for livros, dados in emprestimos.items():
            isbn, usuario, data_inicial, data_final = dados
            print(f'{livros} {isbn} {usuario}  {data_inicial}  {data_final} ')
        input("\n\nAperte ENTER para: ")

    if opcao == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
        print("Relatórios\n".center(80))
        print(F'Há {len(emprestimos)} emprestados atualmente!\n\n')
        input("\n\nAperte ENTER para: ")
    
    if opcao == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
        print("Relatórios\n".center(80))
        print(F'Há {qte_acervo} no acervo atualmente!, sendo {qte_livros} disponíveis para emprestimos! \n\n')
        input("\n\nAperte ENTER para: ")
    
    if opcao == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
        print("Relatórios\n".center(80))
        #print(len(emprestimos))
        #print(len(livros))
        print(F'Há atualmente {qte_usuarios} cadastrados no sistema! \n\n')
        input("\n\nAperte ENTER para: ")
       

opcao = 0
while opcao != "6":
    os.system('cls' if os.name == 'nt' else 'clear')
    cabecalho("BIBLIOTECA FACULDADE ANHANGUERA", "GESTÃO DO ACERVO")
    print("Menu de opções\n".center(80))
    print(
              "1. Usuários\n"
              "2. Livros\n"
              "3. Empréstimos\n"
              "4. Relatórios\n"
              
              "\n6. Sair\n")
    opcao = input("Digite a opcao desejada: ")
    while opcao not in "123456":
        opcao = input("Opção inválida! Digite a opcao desejada de 1 à 5: ")
        
    if opcao == "1":
        lista_usuarios(usuarios)
         
    if opcao == "2":
       lista_livros(livros)
        
    if opcao == "3":
        sub_emprestimos(usuarios, livros)
        
    if opcao == "4":
        relatorios()
        
    if opcao == "5":
        print("\n  ---  ENCERRANDO  ---")