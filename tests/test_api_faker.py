import requests
from faker import Faker
def test_crear_usuario_exitoso():
    """Prueba que verifica la creación exitosa de un usuario con datos aleatorios"""
    fake = Faker('es_CO')
    datos_nuevo_usuario = {
        "name": fake.name(),
        "username": fake.user_name(),
        "email": fake.email()
    }
    url = "https://jsonplaceholder.typicode.com/users"
    respuesta = requests.post(url, json=datos_nuevo_usuario)
    assert respuesta.status_code == 201, f"Código esperado 201, pero se obtuvo {respuesta.status_code}"
    data = respuesta.json()
    assert "id" in data, "El JSON de respuesta no contiene el campo 'id'"
    assert data["name"] == datos_nuevo_usuario["name"], "El nombre retornado no coincide con el enviado"
def test_buscar_usuario_inexistente_error_404():
    """Prueba negativa: Verifica que buscar un ID loco devuelva 404"""
    url = "https://jsonplaceholder.typicode.com/users/9999"
    respuesta = requests.get(url)
    assert respuesta.status_code == 404, f"Se esperaba error 404, pero se obtuvo {respuesta.status_code}"