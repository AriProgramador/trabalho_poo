from evento import Evento

class Agenda:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, evento: Evento):
        self.eventos.append(evento)

    def mostrar_eventos(self):
        for n in self.eventos:
            print(n.nome)

ev1 = Evento("casamento", "14/03/2000", "14:30")
ev2 = Evento("aniversario", "11/09/2001", "18:05")

ag = Agenda()
ag.adicionar_evento(ev1)
ag.adicionar_evento(ev2)
ag.mostrar_eventos()