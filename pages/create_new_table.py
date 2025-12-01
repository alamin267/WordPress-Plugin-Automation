import time
from playwright.sync_api import Page

class CreateNewTable:
    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.flextable_button_from_menu =  page.locator("//div[normalize-space()='FlexTable']")
        self.create_new_table_button = page.locator("//a[normalize-space()='Create new table']")
        self.input_url_field = page.locator("//input[@id='sheet-url']")
        self.create_table_from_url_button = page.locator("//button[normalize-space()='Create table from URL']")
        self.title_field = page.locator("//input[@id='table-name']")
        self.description_field = page.locator("//textarea[@id='table-description']")
        self.save_button = page.locator("//button[normalize-space()='Save changes']")
        self.search_field = page.locator("//input[@placeholder='Search tables']")
        self.no_table_found_text = page.locator("//h5[normalize-space()='No tables found!']")


    def Create_Table_Using_Google_sheet(self, table_name, description):
        self.flextable_button_from_menu.click()
        self.page.wait_for_load_state("networkidle")
        self.create_new_table_button.click()
        self.input_url_field.fill("https://docs.google.com/spreadsheets/d/11qRH9xUuglOTIZa7JnWTVBYuGMT32ZhFuJ5_xypApGM/edit?gid=0#gid=0")
        self.create_table_from_url_button.click()
        self.title_field.fill(table_name)
        self.description_field.fill(description)
        time.sleep(3)
        self.save_button.click()
        print("Table Create Successfully")
        time.sleep(2)
    

    def Verify_Table_Title(self, name: str):
        self.flextable_button_from_menu.click()
        time.sleep(3)
        self.search_field.fill(name)
        if self.no_table_found_text.is_visible():
            print("Table name is not display correctly")
            time.sleep(3)
        else:
            print("Table name is display correctly")
            time.sleep(3)



        