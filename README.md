#Portafolio de Automatización QA Híbrido (Backend & Frontend)

Este repositorio reúne soluciones automatizadas de nivel profesional utilizando **Python** como lenguaje principal. Demuestra la capacidad de auditar datos lógicos detrás de escena, validar la comunicación con servidores mediante APIs y simular interacciones de usuarios reales utilizando patrones de diseño avanzados en la interfaz gráfica.

---

##Estructura del Proyecto
* `pages/`: Módulos basados en el patrón de diseño Page Object Model (POM).
* `tests/`: Suite unificada de pruebas automatizadas (API y UI Web).

---

##Proyecto 1: Data Generation & Audit (Python + MySQL + Faker)

###El escenario de negocio
Simulación de pruebas de carga masiva en el Backend. El objetivo es inyectar de forma segura múltiples perfiles de usuarios realistas para estresar la base de datos o preparar entornos de prueba (**Test Data Setup**). Además, incluye scripts de auditoría lógica (`LEFT JOIN`) para detectar inconsistencias (como órdenes huérfanas sin usuario).

* **Librerías:** `mysql-connector-python`, `Faker` (configurado para `es_CO`).
* **Resultado:** Población exitosa de tablas en segundos y exportación autónoma de anomalías en el archivo `reporte_bugs.txt`.

---

##Proyecto 2: Frontend E2E Testing (Playwright + Pytest + POM)

###El escenario de negocio
Simulación del flujo crítico de un usuario (*User Journey*) dentro de un portal de comercio electrónico: Iniciar sesión con credenciales válidas y validar el acceso correcto al catálogo de productos de la empresa de forma automatizada.

* **Herramientas:** Playwright de Microsoft (`pytest-playwright`).
* **Arquitectura:** Implementación del patrón de diseño **Page Object Model (POM)**. Los selectores CSS avanzados y las acciones de la interfaz se aislaron en la clase `LoginPage`, garantizando un código limpio, legible y fácil de mantener si la UI cambia en el futuro.
* **Resultado:** Flujo completado con éxito, controlando el navegador de forma limpia e interactiva.

---

##Proyecto 3: API Automated Testing (Requests + Pytest)

###El escenario de negocio
Suite de pruebas de integración en el Backend consumiendo servicios REST para garantizar que la comunicación del servidor y los códigos de respuesta HTTP sean correctos ante las peticiones del cliente.

* **Herramientas:** `requests` para peticiones HTTP y `Pytest` como framework central de aserciones.
* **Estrategia de Pruebas:**
  * **Happy Path (Test Positivo):** Envío de un payload dinámico con Faker (`POST`), asegurando un código de estado `201 Created` y validando la integridad del ID retornado.
  * **Negative Testing (Test Negativo):** Validación de control de errores mediante peticiones `GET` a recursos inexistentes, asegurando que el servidor responda correctamente con un `404 Not Found`.

---

##Cómo ejecutar la suite completa de forma local

1. Clona este repositorio.
2. Instala las dependencias necesarias de Python:
```bash
pip install mysql-connector-python playwright requests faker pytest pytest-playwright
playwright install
