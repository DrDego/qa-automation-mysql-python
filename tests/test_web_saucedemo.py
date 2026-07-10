import pytest
from playwright.sync_api import Page
from login_page import LoginPage
def test_login_exitoso(page: Page):
    """Prueba funcional: Login correcto usando el patrón Page Object Model"""
    login = LoginPage(page)
    login.navegar()
    login.iniciar_sesion("standard_user", "secret_sauce")
    assert "inventory.html" in page.url, f"Error: URL incorrecta: {page.url}"
    titulo = login.obtener_titulo_catalogo()
    assert titulo.is_visible(), "Error: El catálogo de productos no se desplegó"