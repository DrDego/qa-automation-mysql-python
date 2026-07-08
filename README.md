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
