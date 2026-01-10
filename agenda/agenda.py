from contato import Contato

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato:Contato):
        if not isinstance(contato, Contato):
            raise TypeError("somente contatos podem ser adicionados")
        
        self.contatos.append(contato)

    def listar_contatos(self):
        for contatos in self.contatos:
            print(f"{contatos.nome} - {contatos.telefone}")



c1 = Contato("kliger", "1515121615")
agd = Agenda()
agd.adicionar_contato(c1)
agd.listar_contatos()
        