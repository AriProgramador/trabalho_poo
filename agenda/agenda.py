from contato import Contato


class Agenda:
    contatos = []

    @classmethod
    def adicionar_contato(cls, contato: Contato):
        if not isinstance(contato, Contato):
            raise TypeError("somente contatos podem ser adicionados")

        cls.contatos.append(contato)

    @classmethod
    def listar_contatos(cls):
        for contatos in cls.contatos:
            return cls.contatos
    @classmethod
    def apagar_contatos(cls, contato):
        if contato in cls.contatos:
            cls.contatos.remove(contato)