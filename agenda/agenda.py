from evento import Evento

class Agenda:
    def __init__(self , nome):
        self.nome = nome
        self.eventos = []

    def adicionar_evento(self, evento: Evento):
        if not isinstance(evento, Evento):
            raise TypeError("somente evento podem ser adicionados")
        
        self.eventos.append(evento)

    def listar_eventos(self):
        return self.eventos.copy()