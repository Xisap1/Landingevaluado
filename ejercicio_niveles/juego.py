import random
from personaje import Personaje

def main():
    print("¡Bienvenido a Gran Fantasía!")
    nombre_personaje = input("Por favor indique nombre de su personaje: ")
    personaje = Personaje(nombre_personaje)
    print(personaje)

    orco = Personaje("Orco")
    print(f"¡Oh no!, ¡Ha aparecido un Orco!")

    while True:
        opcion = Personaje.dialogo_enfrentamiento(personaje, orco)
        if opcion == 1:
            if random.random() <= personaje.probabilidad_ganar(orco):
                print("¡Le has ganado al orco, felicidades!")
                personaje.set_estado(50)
                orco.set_estado(-30)
            else:
                print("¡Oh no! ¡El orco te ha ganado!")
                personaje.set_estado(-30)
                orco.set_estado(50)
            print(personaje)
            print(orco)
        elif opcion == 2:
            print("¡Has huido! El orco ha quedado atrás.")
            break

if __name__ == "__main__":
    main()