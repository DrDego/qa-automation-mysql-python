from playwright.sync_api import Page
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "input#user-name"
        self.password_input = "input#password"
        self.login_button = "input#login-button"
        self.catalog_title = ".title"
    def navegar(self):
        self.page.goto("https://www.saucedemo.com/")
    def iniciar_sesion(self, usuario, password):
        self.page.fill(self.username_input, usuario)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
    def obtener_titulo_catalogo(self):
        return self.page.locator(self.catalog_title)