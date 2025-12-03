import time
from playwright.sync_api import Page

class DeleteTheTableAndVerifyTheFrontendRemoval:
    def __init__(self, page: Page):
        self.page = page


        self.flextable_button_from_menu =  page.locator("//div[normalize-space()='FlexTable']")
        self.delete_button = page.locator("(//button[@class='table-delete'])[1]")
        self.delete_button_inPopup = page.locator("//button[normalize-space()='Delete']")
        self.first_table_text = page.locator("//p[normalize-space()='Click the button below to create your first table!']")



    def delete_the_table(self):
        self.page.reload()
        self.flextable_button_from_menu.click()
        self.delete_button.click()
        self.delete_button_inPopup.click()
        print("Deleted the table successfully")
        time.sleep(3)
        self.page.wait_for_load_state("networkidle")
        if self.first_table_text.is_visible():
            print("Table deleted successfully and empty state message appears.")
        else:
            print("Table can not deleted")

        time.sleep(3)