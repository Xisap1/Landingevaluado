class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def __str__(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    def get_estado(self):
        return self.nivel, self.experiencia

    def set_estado(self, experiencia):
        self.experiencia += experiencia
        while self.experiencia >= 100:
            self.nivel += 1
            self.experiencia -= 100
        while self.experiencia < 0:
            self.nivel -= 1
            self.experiencia += 100

    def __lt__(self, other):
        return self.nivel < other.nivel

    def __gt__(self, other):
        return self.nivel > other.nivel

    def __eq__(self, other):
        return self.nivel == other.nivel

    def probabilidad_ganar(self, other):
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.5

    @staticmethod
    def dialogo_enfrentamiento(personaje, orco):
        print(f"¡Oh no!, ¡Ha aparecido un Orco! Con tu nivel actual, tienes {personaje.probabilidad_ganar(orco)*100:.2f}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        print("¿Qué deseas hacer?")
        print("1. Atacar")
        print("2. Huir")
        return int(input("Opción: "))