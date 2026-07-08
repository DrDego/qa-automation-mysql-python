import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        database='tienda_prueba',
        user='root'
    )
    if conexion.is_connected():
        print("¡Conexión exitosa a la base de datos!")
        cursor = conexion.cursor()
        query = """
            SELECT u.id, u.nombre, o.total 
        FROM ordenes o
        LEFT JOIN usuarios u ON u.id = o.usuario_id
        WHERE o.total > 100;
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        print("\n--- Resultados de la consulta ---")
        for fila in resultados:
            print(f"ID: {fila[0]} | Nombre: {fila[1]} | Total Compra: ${fila[2]}")
        print("\n Ejecutando verificación lógica de QA...")
        with open("reporte_bugs.txt", "w", encoding="utf-8") as archivo_reporte:
            archivo_reporte.write("=== REPORTE AUTOMATIZADO DE QA ===\n\n")
            
            for fila in resultados:
                if fila[1] is None:
                    mensaje_bug = f" ¡BUG ENCONTRADO! La orden por ${fila[2]} no tiene un ID de usuario válido.\n"
                    print(mensaje_bug.strip())
                    archivo_reporte.write(mensaje_bug)
                else:
                    print(f" Registro verificado correctamente para {fila[1]}.")
except Error as e:
    print(f"Error al conectar a MySQL: {e}")
finally:
    if 'conexion' in locals() and conexion.is_connected():
        if 'cursor' in locals():
            cursor.close()
        conexion.close()
        print("\nConexión cerrada limpiamente.")