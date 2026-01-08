from agenda import Agenda
from contato import Contato
from evento import Evento

agenda_de_eventos = Agenda()
contato_1 = Contato("ari", "15451545")
evento_1 = Evento("aniversario", "14/06/2000", "15:30", contato_1)

agenda_de_eventos.adicionar_evento(evento_1)
