import requests

# 1. Obtener toda la información del usuario de la API
response = requests.get('https://reqres.in/api/users')
users_data = response.json()
print(users_data)

# 2. Crea un nuevo usuario con nombre Ignacio y Profesor
data = {'name': 'Ignacio', 'job': 'Profesor'}
response = requests.post('https://reqres.in/api/users', json=data)
created_user = response.json()
print(created_user)

# 3. actualizar usuario
data = {'name': 'morpheus', 'residence': 'zion'}
response = requests.put('https://reqres.in/api/users/2', json=data)
updated_user = response.json()
print(updated_user)

# 4. eliminar usuario
response = requests.delete('https://reqres.in/api/users/5')
print(response.status_code)