from src.db.manipulabanco import add_cidade, get_lista_cidade
from src.classes.cidade import Cidade


def cidade_dao_add(nova_cidade):
    cidade_json = {
        "nome": nova_cidade.nome,
        "populacao": nova_cidade.populacao,
        "uf": nova_cidade.uf
    }

    add_cidade(cidade_json)

def get_lista_cidade_dao():
    cidades = get_lista_cidade()

    lista_cidades = []

    for cidade in cidades:
        instancia = Cidade(cidade['nome'], cidade['populacao'], cidade['uf'])
        lista_cidades.append(instancia)

    return lista_cidades