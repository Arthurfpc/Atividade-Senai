from src.classes.cidade import Cidade
import json

sair = False
lista_cidades=[]

while sair == False:
    nome_cidade= input("Digite o nome da cidade: ")
    populacao_cidade= int(input("Digite a populaçao da cidade: "))
    sigla_estado= input("Digite a sigla do estado: ")
    nome_estado= input("Digite o nome do estado: ")

    nova_cidade= Cidade(nome_cidade, populacao_cidade,{"sigla": sigla_estado, "nome": nome_estado})
    lista_cidades.append({
        "nome": nova_cidade.nome,
        "populacao": nova_cidade.populacao,
        "uf": {
            "sigla":nova_cidade.uf["sigla"],
            "nome":nova_cidade.uf["nome"]
        }
    })
    r= input("Deseja cadastra mais uma cidade ? (S/N): ")
    if r.upper() == "N":
        sair = True

arquivo= open("./src/bd/bd.json", 'w')
arquivo.write(json.dumps(lista_cidades))
arquivo.close()


