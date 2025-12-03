import time
import random
from playwright.sync_api import Page

class UpdateRowsPerPageAndTableHeight:
    def __init__(self, page: Page):
        self.page = page


        self.flextable_button_from_menu =  page.locator("//div[normalize-space()='FlexTable']")
        self.edit_button = locator = page.locator("(//a[contains(@class,'table-edit')])[2]")
        self.table_customization = page.locator("//span[normalize-space()='3. Table customization']")
        self.show_entry_info_button = page.locator("//label[normalize-space()='Show entry info']")
        self.show_pegination_button = page.locator("//label[normalize-space()='Show pagination']")
        self.save_changes_button = page.locator("//button[normalize-space()='Save changes']")
        self.styling_button =  page.locator("//button[normalize-space()='Styling']")
        self.row_per_page_field = page.locator("//select[@id='rows-per-page']")
        self.table_height_field = page.locator("//select[@id='table_height']")



    def select_page_row_randomly_and_table_height_manually(self):
        self.flextable_button_from_menu.click()
        self.edit_button.click()
        self.table_customization.click()
        self.styling_button.click()
        self.row_per_page_field.click()
        self.page.wait_for_load_state("networkidle")

        self.options = self.row_per_page_field.locator('option')
        self.values = self.options.evaluate_all('options => options.map(option => option.value)')
        #print("values:",self.values)
        self.random_value = random.choice(self.values[:-2])
        self.row_per_page_field.select_option(value=self.random_value)
        #print("Random value is",self.random_value )
        time.sleep(2)
        print("Select Row per page value randomly")
        self.table_height_field.click()
        self.table_height_field.select_option(value='800')
        time.sleep(2)
        print("Select table height value manually")
        self.save_changes_button.click()
    
    def verify_row_per_page_and_table_height_value(self):

        selected_value = self.row_per_page_field.input_value()
        selected_value_for_table_height = self.table_height_field.input_value()
        #print("Values:",selected_value,selected_value_for_table_height)
        if self.random_value == selected_value and selected_value_for_table_height == "800":
            print("Rows per page and table height value matches with the selected value in frontend ")
        else:
            print("Value Doesn't match")
        time.sleep(2)
