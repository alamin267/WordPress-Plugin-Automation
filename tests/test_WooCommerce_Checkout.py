import os
from dotenv import load_dotenv
from Wocommerce.End_to_End_Checkout_Flow import EndToEndCheckoutFlow
from Wocommerce.User_Account_Order_History import UserAccountOrderHistory



# Load credentials from .env
load_dotenv()

def test_Woocommerce_checkout(page):
    base_url = os.getenv("WP_URL")
    username = os.getenv("WP_USERNAME")
    password = os.getenv("WP_PASSWORD")

    checkout_page = EndToEndCheckoutFlow(page)
    order_history_page = UserAccountOrderHistory(page)



    # Test Case 1
    checkout_page.go_to_the_product_page(username, password)
    checkout_page.place_an_order()
    checkout_page.verify_product_final_price()

    # Test Case 2
    order_history_page.check_order_history()

