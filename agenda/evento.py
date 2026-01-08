from contato import Contato, NomeInvalidoError
from datetime import datetime
class Evento:
    def __init__(self, nome, data, horario, contato: Contato):
        self.verificar_nome(nome)
        self.data = self.verificar_data(data)
        self.horario = self.verificar_hora(horario)
        self.contato = contato

    def verificar_data(self, data):
        if not isinstance(data, str):
            raise TypeError("a data deve ser uma string")
        try:
            return datetime.strptime(data, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Data inválida use o formato dd/mm/aaaa")
   
        
        
    def verificar_nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError("digite somente texto")
        if nome.strip() == "":
            raise NomeInvalidoError("nome nao pode ser vazio")
        self.nome = nome


    def verificar_hora(self, horario):
        if not isinstance(horario, str):
            raise ValueError("o horario deve ser uma string")
        
        try: 
            return datetime.strptime(horario,"%H:%M").time()
        except ValueError:
            raise ValueError("horario invalido use o formato hh:mm")
        