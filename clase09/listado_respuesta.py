class ListadoRespuestas:
    def __init__(self, usuario):
        self.usuario = usuario
        self.respuestas = []

    def agregar_respuesta(self, respuesta):
        self.respuestas.append(respuesta)

    def mostrar(self):
        print(f"Listado de respuestas de {self.usuario.correo}:")
        for respuesta in self.respuestas:
            print(f"Respuesta: {respuesta}")