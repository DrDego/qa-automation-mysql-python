#Portafolio de Automatización QA Híbrido (Backend & Frontend)
Este repositorio reúne soluciones automatizadas de nivel profesional utilizando **Python** como lenguaje principal. Demuestra la capacidad de auditar datos lógicos detrás de escena y de simular interacciones de usuarios reales directamente en la interfaz gráfica.
---
##  Proyecto 1: Backend Testing (Python + MySQL)

### El escenario en el q trabaja es sobre negocio
La regla del negocio estipula que: *"Toda orden de compra registrada con un monto mayor a $100 debe estar vinculada obligatoriamente a un ID de usuario registrado y válido."*

### Detalles Técnicos de este escenario
* **Conector:** `mysql-connector-python`
* **Lógica:** Implementación de un enfoque **LEFT JOIN** priorizando la tabla de órdenes para extraer registros masivos.
* **Resultado:** El script detectó de forma autónoma una orden huérfana (Monto: $120.00, Usuario: `None`), exportando una alerta estructurada al archivo `reporte_bugs.txt`.
---
## Proyecto 2: Frontend E2E UI Testing (Python + Playwright)

### El escenario en el q trabaja es sobre negocio
Simulación del flujo crítico de un usuario (*User Journey*) dentro de un portal de comercio electrónico: Iniciar sesión con credenciales válidas y validar el acceso correcto al catálogo de productos de la empresa.

### Detalles Técnicos de este escenario
* **Herramientas:** Playwright de Microsoft (`playwright.sync_api`).
* **Navegador utilizado:** Chromium (Headless=False, slow_mo=1000ms para auditoría visual).
* **Estrategia de Localizadores:** Uso de Selectores ID avanzados de CSS (`input#user-name`, `input#password`, `input#login-button`).
* **Validación de QA:** Verificación de la visibilidad y coincidencia de texto en el elemento del título de la interfaz gráfica (`.title`).
* **Resultado:** Flujo completado con éxito, guardando evidencia fotográfica en el archivo `evidencia_login_exitoso.png`.
---
## Cómo ejecutar los proyectos de forma local?

1. Clona este repositorio.
2. Instala las dependencias necesarias de Python:
   ```bash
   pip install mysql-connector-python playwright
   playwright install
   ```
3. Ejecuta `python prueba_conexion.py` para la prueba de datos o `python prueba_web.py` para la prueba del navegador.
---
---

## Proyecto 4: Data Generation & Load Testing (Python + Faker + MySQL)

### El escenario en el q trabaja es sobre negocio
Simulación de pruebas de carga masiva en el Backend. El objetivo es inyectar de forma segura múltiples perfiles de usuarios realistas para estresar la base de datos o preparar entornos de pruebas automatizadas (*Test Data Setup*).

### Detalles Técnicos de este escenario
* **Librerías adicionales:** `Faker` configurada con localización colombiana (`es_CO`).
* **Lógica:** Implementación de un ciclo iterativo `for` que genera estructuras de datos dinámicas en memoria.
* **Persistencia:** Uso del método `.commit()` para consolidar la inserción de 20 tuplas de manera síncrona en MySQL de forma atómica.
* **Resultado:** Población exitosa de tablas en un segundo sin violar restricciones de integridad del servidor.
## Proyecto 3: API Automated Testing (Python + Requests + Pytest)

###  El escenario en el que trabaja es sobre negocio
Simulación de pruebas de integración y validación de endpoints (Backend) consumiendo servicios REST para garantizar que la comunicación con el servidor sea correcta y segura ante peticiones del cliente.

###  Detalles técnicos de este escenario
* **Herramientas:** `requests` para el manejo de peticiones HTTP y `Faker` para la inyección de payloads dinámicos.
* **Estrategia de Datos:** Uso de `Faker('es_CO')` para generar datos de usuario realistas (nombre, username, email) en tiempo de ejecución, evitando usar datos fijos (Hardcoded).
* **Framework de Testing:** Estructurado completamente bajo los estándares de **Pytest** utilizando aserciones (`assert`) nativas.
* **Tipos de Pruebas Incluidas:**
  * **Happy Path (Test Positivo):** Validación de creación exitosa de usuarios mediante peticiones `POST`, asegurando un código de estado HTTP `201 Created` y verificando la integridad del JSON de respuesta.
  * **Negative Testing (Test Negativo):** Validación de control de errores mediante peticiones `GET` a recursos inexistentes, asegurando que el servidor responda con un código `404 Not Found`.

---

##Cómo ejecutar los proyectos de forma local?

1. Clona este repositorio.
2. Instala las dependencias necesarias de Python:
```bash
pip install mysql-connector-python playwright requests faker pytest
playwright install
