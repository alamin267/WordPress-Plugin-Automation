import time 
from playwright.sync_api import Page

class ShowTableTitleAndDescription:
    def __init__(self, page: Page):
        self.page = page

        self.url = "http://mylocalwordpress.local/wp-admin/admin.php?page=gswpts-dashboard#/"

        self.flextable_button_from_menu =  page.locator("//div[normalize-space()='FlexTable']")
        self.edit_button = locator = page.locator("(//a[contains(@class,'table-edit')])[2]")
        self.table_customization = page.locator("//span[normalize-space()='3. Table customization']")
        self.show_table_title = page.locator("//label[normalize-space()='Show Table title']")
        self.show_table_description_position = page.locator("//select[@id='description-position']")
        self.select_below_value = page.locator('option[value="below"]')
        self.show_table_description = page.locator("//label[@for='show-description']")
        self.save_changes_button = page.locator("//button[normalize-space()='Save changes']")
        self.verify_title = page.locator("//h3[@id='swptls-table-title']")
        self.verify_description = page.locator("//p[@id='swptls-table-description']")




    def show_title_and_description(self):
        self.page.goto(self.url)
        self.flextable_button_from_menu.click()
        self.edit_button.click()
        time.sleep(1)
        self.table_customization.click()
        self.show_table_title.click()
        self.show_table_description_position.click()
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.show_table_description.click()
        print("Shown title and description")
        time.sleep(2)
        self.save_changes_button.click()
        print("Update Table successfully")
        self.page.reload()
        time.sleep(5)
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        if self.verify_title.is_visible():
            print("Table Title is showing in the frontend properly")
        if self.verify_description.is_visible():
            print("Table Description is showing in the frontend properly")
        time.sleep(5)
        
