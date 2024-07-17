import json
import logging

from usuario import Usuario

# Configuración de logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

# Crear lista para almacenar instancias de Usuario
usuarios = []

# Leer archivo usuarios.txt línea a línea
with open('usuarios.txt', 'r') as f:
    for linea in f:
        try:
            # Parsear JSON de la línea
            datos_usuario = json.loads(linea)

            # Crear instancia de Usuario
            usuario = Usuario(**datos_usuario)

            # Agregar instancia a la lista
            usuarios.append(usuario)

        except (json.JSONDecodeError, TypeError, ValueError) as e:
            # Manejar excepciones al parsear JSON o crear instancia
            logging.error(f"Error al crear usuario: {e}")

# Imprimir lista de usuarios creados
for usuario in usuarios:
    print(usuario)