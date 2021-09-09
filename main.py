from src.classes.cidade import Cidade
from src.db.manipulabanco import add_cidade, get_lista_cidade

def cadastra_cidade():   
    print("### Cadastro de cidade ###")
    nome_cidade = input('Digite o nome da cidade: ').title()
    populacao_cidade = (input('Digite a população da cidade: '))
    
    while not populacao_cidade.isnumeric():
        print('Numero inválido')
        populacao_cidade = (input('Digite a população da cidade: '))
    
    sigla_estado = input('Digite a sigla do estado: ').upper()
    
    while not sigla_estado.isalpha() or len(sigla_estado) > 2:
        print('Sigla inválida')
        sigla_estado = input('Digite a sigla do estado: ').upper()
   
    nome_estado = input('Digite o nome do estado: ').title()

    uf = {'sigla': sigla_estado, 'nome': nome_estado}
    nova_cidade = Cidade(nome_cidade, populacao_cidade, uf)

    add_cidade(nova_cidade)

def imprime_menu():
    print(''' 
    ######## Funções  #########
    1- Listar todas as cidades
    2- Cadastra uma nova cidade
    ###########################
    0 - Sair
    ''')
    menu= input("Digite a função desejada: ")
    if menu == "1":
        print(get_lista_cidade())
        imprime_menu()
    elif menu == "2":
        cadastra_cidade()
        imprime_menu()
    elif menu == "0":
        print("Até logo")
    else:
        print("Escolha uma opção valida: ")
        imprime_menu()

imprime_menu()
