class Pregunta:
    def __init__(self, enunciado, ayuda=None, requerida=False, alternativas=None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = alternativas if alternativas else []

    def mostrar(self):
        print(f"Pregunta: {self.enunciado}")
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")
        for alternativa in self.alternativas:
            alternativa.mostrar()