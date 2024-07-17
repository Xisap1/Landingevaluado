class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar(self):
        print(f"Alternativa: {self.contenido}")
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")