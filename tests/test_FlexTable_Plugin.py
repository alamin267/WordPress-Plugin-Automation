import os
from dotenv import load_dotenv

from pages.create_new_table import CreateNewTable
from pages.verify_login_functionality import VerifyLoginFunctionality
from pages.verify_plugin_status import VerifyPluginStatusPage
from pages.navigate_to_flexiable_dashboard import NavigateToFlexiableDashboard
from pages.create_page_using_shortcode import CreateNewPage

# Load credentials from .env
load_dotenv()

def test_wordpress_login(page):
    base_url = os.getenv("WP_URL")
    username = os.getenv("WP_USERNAME")
    password = os.getenv("WP_PASSWORD")

    login_page = VerifyLoginFunctionality(page)
    plugin_page = VerifyPluginStatusPage(page)
    flextable_page = NavigateToFlexiableDashboard(page)
    create_table_page = CreateNewTable(page)
    create_page =  CreateNewPage(page)

    # Test Case 1
    login_page.navigate(base_url)
    login_page.login(username, password)
    assert "/wp-admin/" in page.url or "Dashboard" in page.content()


    # Test Case 2
    plugin_page.go_to_installed_plugins()

    # Test Case 3
    flextable_page.navigate_to_Flextable_Dashboard()

    
    # Test Case 4
    create_table_page.Create_Table_Using_Google_sheet("WPPOOL","Table Description")
    create_table_page.Verify_Table_Title("WPPOOL")

    # Test Case 5
    create_page.create_new_page()
    create_page.verify_table_value()

 
