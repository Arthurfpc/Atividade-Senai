class Cidade:
    def __init__(self, nome, populacao, uf):
        self.__nome = nome
        self.__populacao = populacao
        self.__uf = uf 

    def __str__(self):
        return f'''
        Nome: \t\t{self.__nome}
        População: \t{self.__populacao}
        Estado: \t{self.__uf["sigla"]} -- {self.__uf["nome"]}'''

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def populacao(self):
        return self.__populacao
    @populacao.setter
    def populacao(self, populacao):
        self.__populacao = populacao
        
    @property
    def uf(self):
        return self.__uf
    @populacao.setter
    def populacao(self, uf):
        self.__uf["sigla"] = uf["sigla"]
        self.__uf["nome"] = uf["nome"]