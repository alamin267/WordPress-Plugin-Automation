import time
from playwright.sync_api import Page

class VerifyPluginStatusPage:
    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.plugins_menu = page.locator("#menu-plugins a.wp-has-submenu")
        self.installed_plugins_submenu = page.locator("//a[normalize-space()='Installed Plugins']")
        self.add_new_plugin = page.locator("#menu-plugins a[href='plugin-install.php']")

        # Installed Plugins 
        self.search_installed_input = page.locator("#plugin-search-input")
        self.no_plugin_message = page.get_by_text("No plugins are currently available.")
        self.add_plugin_button = page.locator("//a[@class='page-title-action']")
        self.search_plugins_input_field = page.locator("//input[@id='search-plugins']")
        self.install_now_button = page.locator("a.install-now.button[data-slug='sheets-to-wp-table-live-sync']")
        self.active_plugin_button = page.locator("//a[normalize-space()='Activate']")
        self.allow_permission_button = page.locator("//a[normalize-space()='Allow']")

        # Searched Plugin and Activate
        self.search_plugin = page.locator("//input[@id='plugin-search-input']")
        self.activate_button = page.locator("//a[@id='activate-sheets-to-wp-table-live-sync']")
        self.search_plugin_name = page.locator("strong:has-text('FlexTable')")
        self.deactivate_button = page.locator("//a[@id='deactivate-sheets-to-wp-table-live-sync']")




    def go_to_installed_plugins(self):
        print("We are in the Dashboard Page")
        self.plugins_menu.click()
        self.installed_plugins_submenu.first.click()
        self.page.wait_for_load_state("networkidle")
        if self.no_plugin_message.is_visible():
            print("No plugins are available, we have to installing plugin now")
            self.add_plugin_button.click()
            self.search_plugins_input_field.fill("FlexTable")
            time.sleep(2)
            self.install_now_button.click()
            self.page.wait_for_load_state("networkidle")
            self.active_plugin_button.click()
            print("Plugin Installed Successfully")
            time.sleep(2)
            #self.allow_permission_button.click()
        elif self.search_plugin_name.is_visible():
            self.search_plugin.fill("FlexTable")
            if self.deactivate_button.is_visible():
                print("Plug is available and active, Nothing to do")
                self.page.wait_for_load_state("networkidle")
                time.sleep(2)
            else:
                print("Plugin is not Activate, We are activating it now")
                self.activate_button.click()
                self.page.wait_for_load_state("networkidle")
                print("Activated Plugin Successfully")
                time.sleep(2)
            



 