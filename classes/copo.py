from classes import recipiente
from classes.recipiente import Recipiente

class Copo(Recipiente):
    def __init__(self, tamanho):
        super().__init__(tamanho)

    def encher(self, bebida: str = "água"):
        if not self.limpo:
            return "Não se pode encher um copo sujo"
        else:
            self.conteudo = self.tamanho
            self.limpo = False
            self.bebida = bebida

    def beber(self, quantidade):
        if quantidade < 0:
            return "Quantidade deve ser positiva"
        elif quantidade > self.conteudo:
            return 'Não há bebida suficiente no copo'
        else:
            self.conteudo -= quantidade

    def lavar(self):
        self.limpo = True
        self.bebida = None
        self.conteudo = 0

    def __str__(self):
        return f"Um copo vazio de {float(self.tamanho)}ml" if self.conteudo == 0 else f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"

    def __repr__(self):
        return f"Um copo vazio de {float(self.tamanho)}ml" if self.conteudo == 0 else f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"