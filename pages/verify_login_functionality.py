from playwright.sync_api import Page

class VerifyLoginFunctionality:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user_login")
        self.password_input = page.locator("#user_pass")
        self.login_button = page.locator("#wp-submit")

    def navigate(self, base_url):
        self.page.goto(f"{base_url}/wp-login.php")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_load_state("networkidle")
        print("\n Login Successful")
