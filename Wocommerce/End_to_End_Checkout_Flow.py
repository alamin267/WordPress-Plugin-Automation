import time
from playwright.sync_api import Page, Error
from playwright.sync_api import Page

class EndToEndCheckoutFlow:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user_login")
        self.password_input = page.locator("#user_pass")

        # Login
        self.url = "http://mylocalwordpress.local/shop/"
        self.login_button = page.locator("#wp-submit")
        self.login = page.locator('a:text("Log in")')
        # Place Order
        self.add_to_cart_button = page.locator("//button[@aria-label='Add to cart: “Acer Aspire 5”']")
        self.cart_button = page.locator("//span[@class='wc-block-mini-cart__quantity-badge']//*[name()='svg']")
        self.view_my_cart_button = page.locator("//div[normalize-space()='View my cart']")
        self.proceed_to_checkout_button = page.locator("//div[normalize-space()='Go to checkout']")
        self.edit_shippping_address_button = page.locator("//span[@aria-label='Edit shipping address']")
        self.input_first_name = page.locator("//input[@id='shipping-first_name']")
        self.input_last_name = page.locator("//input[@id='shipping-last_name']")
        self.input_address = page.locator("//input[@id='shipping-address_1']")
        self.input_city = page.locator("//input[@id='shipping-city']")
        self.input_district = page.locator("//select[@id='shipping-state']")
        self.input_postcode = page.locator("//input[@id='shipping-postcode']")
        self.input_phone_number = page.locator("//input[@id='shipping-phone']")
        self.select_pathao = page.locator("//span[@id='radio-control-0-flat_rate:2__label']")
        self.place_order = page.locator("//button[@type='button']")

        # verify price
        self.product_price = page.locator("ins.wc-block-components-product-price__value.is-discounted >> text=80,000.00৳")
        self.quantity = page.locator("//div[@class='wc-block-components-order-summary-item__quantity']")
        self.shipping_charge = page.locator("span.wc-block-formatted-money-amount.wc-block-components-formatted-money-amount.wc-block-components-totals-item__value >> text=1,000.00")
        self.final_price_showing = page.locator("//div[@class='wc-block-components-totals-item__value']")



    def go_to_the_product_page(self, username, password):
        self.page.goto(self.url)
        self.login.click()
        self.username_input.fill(username)
        time.sleep(1)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_load_state("networkidle")
        print("\nLogin Successful")

    def place_an_order(self):
        self.add_to_cart_button.click()
        self.cart_button.click()
        print("Add to cart Product successfully")
        self.page.wait_for_load_state("networkidle")
        #self.view_my_cart_button.click()
        time.sleep(3)
        self.proceed_to_checkout_button.click()
        print("Go to checkout page successfully")
        self.page.wait_for_load_state("networkidle")
        self.edit_shippping_address_button.click()
        self.input_first_name.fill("Md")
        self.input_last_name.fill("Al-amin")
        self.input_address.fill("Alamnagar,Housing")
        time.sleep(2)
        self.input_city.fill("Dhaka,Bangladesh")
        self.input_postcode.fill("1338")
        self.input_phone_number.fill("01977570776")
        time.sleep(3)
        print("Enter Shipping Adress Successfully")
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        self.select_pathao.click()
        time.sleep(3)
        self.place_order.click()

    def verify_product_final_price(self):
        # self.add_to_cart_button.click()
        # self.cart_button.click()
        price = self.product_price.inner_text()
        price = price.split('৳')[0].replace(',', '').strip()
        price = float(price)
        print("Product price:",price)

        #self.proceed_to_checkout_button.click()
        quantityValue = self.quantity.inner_text()
        quantity_item = quantityValue.split()[1]
        quantity_item = float(quantity_item)
        print("Quantity:", quantity_item)

        self.page.wait_for_load_state("networkidle")
        shipping_charge_amount = self.shipping_charge.inner_text()
        shipping_charge_amount = shipping_charge_amount.split('৳')[0].replace(',', '').strip()
        shipping_charge_amount = float(shipping_charge_amount)
        print("Shipping Charge:", shipping_charge_amount)

        final_price = self.final_price_showing.inner_text()
        final_price = final_price.split('৳')[0].replace(',', '').strip()
        final_price = float(final_price)
        print("FInal Price:", final_price)

        total_calculated_price = (price * quantity_item) + shipping_charge_amount
        print("Calculated Price is :", total_calculated_price)
        if total_calculated_price == final_price :
            print("Total Price is matched:", total_calculated_price)
        else:
            print("Invalid values detected")

        time.sleep(3)
        
