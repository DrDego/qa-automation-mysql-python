import time
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, slow_mo=1000)
    pagina = navegador.new_page()
    print(" Robot: Iniciando prueba negativa de Login...")
    pagina.goto("https://saucedemo.com")
    print(" Robot: Escribiendo credenciales de usuario bloqueado...")
    pagina.fill("input#user-name", "locked_out_user")  # Usuario bloqueado del sistema
    pagina.fill("input#password", "secret_sauce")      # Contraseña correcta
    print(" Robot: Presionando botón de ingreso...")
    pagina.click("input#login-button")
    print(" Robot: Validando si la interfaz bloquea el acceso correctamente...")
    contenedor_error = pagina.locator("[data-test='error']")
    if contenedor_error.is_visible():
        texto_error = contenedor_error.text_content()
        print(f" Alerta detectada en pantalla: '{texto_error}'")
        if "sorry, this user has been locked out" in texto_error.lower():
            print(" PRUEBA NEGATIVA EXITOSA: El sistema bloqueó al usuario correctamente.")
            pagina.screenshot(path="evidencia_usuario_bloqueado.png")
        else:
            print(" BUG: Aparece un error, pero el mensaje no es el correcto para un bloqueo.")
    else:
        print(" ¡BUG CRÍTICO ENCONTRADO! El sistema permitió el ingreso o no mostró ninguna alerta.")
        pagina.screenshot(path="evidencia_falla_bloqueo.png")
    navegador.close()
    print("🏁 Prueba negativa terminada.")