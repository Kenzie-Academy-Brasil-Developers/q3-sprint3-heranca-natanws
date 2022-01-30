class Recipiente:
    def __init__(self, tamanho, conteudo: float = 0, limpo: bool = True,):
        self.tamanho = tamanho if tamanho > 0 else 0
        self.conteudo = conteudo
        self.limpo = limpo
    
    def esvaziar(self):
        self.conteudo = 0

    def esta_vazio(self):
        return 0 == self.conteudo

    def lavar(self):
        self.conteudo = 0
        self.limpo = True

    def esta_limpo(self):
        return self.limpo
    
    def estado(self):
        condition = 'sujo'
        
        if self.limpo:
            condition = 'limpo'
        
        return condition
        
    def sujar(self):
        self.limpo = False

    def __str__(self):
        return f"Um recipiente {'limpo' if self.limpo == True else 'sujo'} não especificado"
    
    def __repr__(self):
        return f"Um recipiente {'limpo' if self.limpo == True else 'sujo'} não especificado"

