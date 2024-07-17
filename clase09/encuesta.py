class Encuesta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = []
        self.listados_respuestas = []

    def mostrar(self):
        print(f"Encuesta: {self.nombre}")
        for pregunta in self.preguntas:
            pregunta.mostrar()

    def agregar_listado_respuestas(self, listado_respuestas):
        self.listados_respuestas.append(listado_respuestas)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, edad_minima, edad_maxima):
        super().__init__(nombre)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    def agregar_listado_respuestas(self, listado_respuestas):
        if listado_respuestas.usuario.edad >= self.edad_minima and listado_respuestas.usuario.edad <= self.edad_maxima:
            super().agregar_listado_respuestas(listado_respuestas)

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, regiones):
        super().__init__(nombre)
        self.regiones = regiones

    def agregar_listado_respuestas(self, listado_respuestas):
        if listado_respuestas.usuario.region in self.regiones:
            super().agregar_listado_respuestas(listado_respuestas)