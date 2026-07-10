import requests
from faker import Faker
fake = Faker('es_CO')
datos_nuevo_usuario = {
    "name": fake.name(),
    "username": fake.user_name(),
    "email": fake.email()
}
url = "https://jsonplaceholder.typicode.com/users"
respuesta = requests.post(url, json=datos_nuevo_usuario)
print(f"Status Code recibido: {respuesta.status_code}")
if respuesta.status_code == 201:
    print("¡PRUEBA DE API EXITOSA!")
    print(f"Respuesta del Servidor (JSON): {respuesta.json()}")
else:
    print(f"¡BUG DETECTADO! Código de error: {respuesta.status_code}")