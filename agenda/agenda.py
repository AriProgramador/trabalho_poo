from contato import Contato

class Agenda:
    contatos = []
    @classmethod
    def adicionar_contato(self, contato:Contato):
        if not isinstance(contato, Contato):
            raise TypeError("somente contatos podem ser adicionados")
        
        self.contatos.append(contato)

    def listar_contatos(self):
        for contatos in self.contatos:
            print(f"{contatos.nome} - {contatos.telefone}")

    

