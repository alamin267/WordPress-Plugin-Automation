import time
from playwright.sync_api import Page

class UserAccountOrderHistory:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user_login")
        self.password_input = page.locator("#user_pass")

        # Login
        self.url = "http://mylocalwordpress.local/my-account/"
        self.my_account_button = page.locator("//a[normalize-space()='My account']")
        self.orders_button = page.locator("//a[normalize-space()='Orders']")
        #self.order_no = page.locator("(//li[@class='wc-block-order-confirmation-summary-list-item'])[1]")
        self.order_date = page.locator("text=December 4, 2025").nth(0)
        self.order_links = page.locator('th.woocommerce-orders-table__cell-order-number a')


    def check_order_history(self):
        self.page.goto(self.url)
        #self.my_account_button.click()
        self.page.wait_for_load_state("networkidle")
        self.orders_button.click()
        self.page.evaluate("window.scrollTo(0, 1500)")
        time.sleep(5)
        print("Oder history viewd")

    def validate_oder_data(self):
        #order = self.order_no.inner_text()
        #orderNo = order.strip()
        orderNo = "415"
        print(orderNo)
        print("Try to match")
        order_numbers = self.order_links.all_text_contents()

        for order_number in order_numbers:
         all_order_number = order_number.strip() 
         print(all_order_number)

        found_match = False
        for ordernumber in all_order_number:
         if ordernumber == orderNo:
          found_match = True
          break  

        if found_match:
         print("Order Data Match")
        else:
         print("Order Data Doesn't Match")
