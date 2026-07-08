import time
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, slow_mo=1000)
    pagina = navegador.new_page()
    print(" Robot: Abriendo la página de login...")
    pagina.goto("https://saucedemo.com")
    print(" Robot: Escribiendo credenciales...")
    pagina.fill("input#user-name", "standard_user")  # Escribe el usuario
    pagina.fill("input#password", "secret_sauce")   # Escribe la contraseña
    print("🖱️ Robot: Haciendo clic en el botón Login...")
    pagina.click("input#login-button")
    print(" Robot: Validando si el ingreso fue exitoso...")
    if pagina.locator(".title").is_visible():
        titulo_pagina = pagina.locator(".title").text_content()
        if titulo_pagina == "Products":
            print(" PRUEBA EXITOSA: Logramos entrar al catálogo de productos.")
            pagina.screenshot(path="evidencia_login_exitoso.png")
    else:
        print(" ¡BUG ENCONTRADO! El botón falló o las credenciales no sirvieron.")
        pagina.screenshot(path="evidencia_error_login.png")
    navegador.close()
    print(" Prueba terminada.")