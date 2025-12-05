import time
import pyperclip
from playwright.sync_api import Page

class CreateNewPage:
    def __init__(self, page: Page):
        self.page = page

        # Create Page
        self.flextable_button_from_menu =  page.locator("//div[normalize-space()='FlexTable']")
        self.short_code_button = page.locator("//button[@class='copy-shortcode btn-shortcode ']")
        self.page_from_menu = page.locator("//div[normalize-space()='Pages']")
        self.add_new_page =  page.locator("//a[@href='post-new.php?post_type=page']")
        self.choosea_pattern = page.locator("//div[@class='components-modal__header']//button[@aria-label='Close']//*[name()='svg']")
        self.select_block = page.locator("//span[normalize-space()='Block']")
        self.page_title = page.locator("//h1[@aria-label='Add title']")
        self.add_block_button = page.locator("//button[@aria-label='Add block']")
        self.search_filed = page.locator("input.components-input-control__input[placeholder='Search']")
        self.select_shortcode = page.locator("//span[contains(text(),'Shortcode')]")
        self.enter_shortcode_field = page.get_by_placeholder("Write shortcode here…")
        self.publish_button = page.locator("//button[normalize-space()='Publish']")
        self.second_publish_button = page.locator("//button[@class='components-button editor-post-publish-button editor-post-publish-button__button is-primary is-compact']")
        self.copy_code_button = page.locator("//button[normalize-space()='Copy']")
        self.home_button = page.locator("//a[@role='menuitem'][normalize-space()='MyLocalWordPress']")
        

        # verify table
        self.can_not_load_text = page.locator("//b[contains(text(),'Table maybe deleted or can’t be loaded.')]")

    def create_new_page(self):
        self.page.reload()
        time.sleep(3)
        short_code = self.short_code_button.all_text_contents()[0]
        #print("Code is", short_code)
        self.page_from_menu.click()
        self.add_new_page.click()
        time.sleep(2)
        self.choosea_pattern.click()
        self.page_title.fill("Test Page")
        self.add_block_button.click()
        time.sleep(1)
        self.search_filed.fill("Shortcode")
        time.sleep(1)
        self.select_shortcode.click()
        self.enter_shortcode_field.fill(short_code)
        time.sleep(1)
        self.publish_button.click()
        time.sleep(3)
        self.second_publish_button.click()
        self.copy_code_button.click()
        self.new_page_url = pyperclip.paste()
        time.sleep(3)
        self.page.goto(self.new_page_url)
        time.sleep(3)
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
    
    def verify_table_value(self):
        if self.can_not_load_text.is_visible():
            print("Table Can not be loaded during Automation time")
        else:
            print("Table loaded")
        #self.home_button.click()
        time.sleep(3)
