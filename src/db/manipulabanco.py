import json 

def get_lista_cidade():
    arquivo = open("./src/db/db.json", 'r')
    lista_cidades = json.loads(arquivo.read())
    arquivo.close()
    return lista_cidades

def set_lista_cidade(lista_cidades):
    arquivo = open("./src/db/db.json", 'w')
    arquivo.write(json.dumps(lista_cidades))
    arquivo.close()  

def add_cidade(cidade_json):
    lista_cidade = get_lista_cidade()
    lista_cidade.append(cidade_json)
    set_lista_cidade(lista_cidade)