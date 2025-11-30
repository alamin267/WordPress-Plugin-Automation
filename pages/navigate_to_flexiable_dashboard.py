import time
from playwright.sync_api import Page

class NavigateToFlexiableDashboard:
    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.flextable_button_from_menu =  page.locator("//div[normalize-space()='FlexTable']")
        self.welcome_text = page.locator("//h2[contains(text(),'👋 Welcome!')]")
        self.url = "http://mylocalwordpress.local/wp-admin/admin.php?page=gswpts-dashboard#/"



    def navigate_to_Flextable_Dashboard(self):
        self.flextable_button_from_menu.click()
        self.page.wait_for_load_state("networkidle")
        assert "admin.php?page=gswpts-dashboard" in self.url, f"❌ Not on FlexTable Dashboard. Current URL: {self.url}"
        print("FlexTable Dashboard Load Successfully")




