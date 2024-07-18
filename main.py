class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self._idade = idade
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_idade(self):
        return self._idade
    
    def set_idade(self, idade):
        self._idade = idade

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self._idade}, CPF: {self.__cpf}'	
