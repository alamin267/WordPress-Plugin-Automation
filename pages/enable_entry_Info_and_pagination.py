import time
from playwright.sync_api import Page

class EnableEnteryInfoAndPagination:
    def __init__(self, page: Page):
        self.page = page


        self.flextable_button_from_menu =  page.locator("//div[normalize-space()='FlexTable']")
        self.edit_button = locator = page.locator("(//a[contains(@class,'table-edit')])[2]")
        self.table_customization = page.locator("//span[normalize-space()='3. Table customization']")
        self.show_entry_info_button = page.locator("//label[normalize-space()='Show entry info']")
        self.show_pegination_button = page.locator("//label[normalize-space()='Show pagination']")
        self.save_changes_button = page.locator("//button[normalize-space()='Save changes']")
        self.table_entry_info = page.locator("//div[@id='create_tables_info']")
        self.previous_button = page.locator("//a[@id='create_tables_previous']")
        self.next_button = page.locator("//a[@id='create_tables_next']")


    def show_entryInfo_and_pagination(self):
        self.flextable_button_from_menu.click()
        self.edit_button.click()
        self.table_customization.click()
        self.show_entry_info_button.click()
        self.show_pegination_button.click()
        self.show_pegination_button.scroll_into_view_if_needed()
        time.sleep(3)
        self.save_changes_button.click()
        time.sleep(5)
        print("Enabled the Entry Info and Pagenation properly")
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        if self.table_entry_info.is_visible():
            print("Table info is showing in the frontend properly")
        if self.previous_button.is_visible() and self.next_button.is_visible():
            print("Pagination is showing in the frontend properly")
        time.sleep(5)