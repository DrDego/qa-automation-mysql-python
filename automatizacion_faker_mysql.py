import mysql.connector
from mysql.connector import Error
from faker import Faker
fake = Faker('es_CO')
try:
    conexion = mysql.connector.connect(
        host='localhost',
        database='tienda_prueba',
        user='root',
        password=''
    )
    if conexion.is_connected():
        cursor = conexion.cursor()
        print(" Conexión exitosa a MySQL. Iniciando inyección masiva de datos...\n")
        usuarios_creados = 0
        for _ in range(20):
            nombre_ficticio = fake.name()
            query_insertar = "INSERT INTO usuarios (nombre) VALUES (%s)"
            datos = (nombre_ficticio,)
            cursor.execute(query_insertar, datos)
            usuarios_creados += 1
            print(f" [{usuarios_creados}/20] Generado e insertado: {nombre_ficticio}")
        conexion.commit()
        print(f"\n ¡PRUEBA DE CARGA EXITOSA! Se inyectaron {usuarios_creados} usuarios correctamente.")
except Error as e:
    print(f" Error durante la automatización de datos: {e}")
finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
        print(" Conexión cerrada con el servidor.")
