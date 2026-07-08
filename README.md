# Automatización de Pruebas en Base de Datos (QA Híbrido)

Este proyecto demuestra una solución automatizada de Backend Testing utilizando **Python** para conectarse de forma programática a una base de datos **MySQL**, auditar registros comerciales y exportar un reporte automatizado de fallas lógicas (Bugs).

## Escenario de Prueba (Caso de Negocio)
La regla del negocio estipula que: *"Toda orden de compra registrada con un monto mayor a $100 debe estar vinculada obligatoriamente a un ID de usuario registrado y válido."*

## Lo que se uso en el proyecto
* **Lenguaje:** Python 3.12
* **Base de Datos:** MySQL (MariaDB vía XAMPP)
* **Conector:** `mysql-connector-python`

## Resultados que ah dado el Script
Al aplicar un enfoque de **LEFT JOIN** priorizando la tabla de órdenes, el script fue capaz de extraer de forma masiva los datos e identificar de manera autónoma una orden huérfana (Monto: $120.00, Usuario: `None`), generando un archivo de salida llamado `reporte_bugs.txt` con la alerta correspondiente para el equipo de desarrollo.
