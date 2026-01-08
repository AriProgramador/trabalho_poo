class NomeInvalidoError(Exception):
    pass

class Contato:
    def __init__(self, nome:str, telefone:str):
        self.verificar_nome(nome)
        self.verificar_telefone(telefone)

    def verificar_nome(self, nome):
        if not isinstance(nome,str):
            raise TypeError("o nome deve ser uma string")
        
        if nome.strip() == "":
            raise NomeInvalidoError("nome nao pode ser vazio")
        
        self.nome = nome
    
    def verificar_telefone(self, telefone):
        if not isinstance(telefone, str):
            raise TypeError("deve ser uma string")
        
        if not telefone.isdigit():
            raise ValueError("digite somente numeros")
        
        if len(telefone) != 8:
            raise ValueError("o numero deve ter 8 digitos")
        
        self.telefone = telefone
