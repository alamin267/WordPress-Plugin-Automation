import os
from dotenv import load_dotenv

from pages.create_new_table import CreateNewTable
from pages.verify_login_functionality import VerifyLoginFunctionality
from pages.verify_plugin_status import VerifyPluginStatusPage
from pages.navigate_to_flexiable_dashboard import NavigateToFlexiableDashboard
from pages.create_page_using_shortcode import CreateNewPage
from pages.show_table_title_and_description import ShowTableTitleAndDescription
from pages.enable_entry_Info_and_pagination import EnableEnteryInfoAndPagination
from pages.update_rows_and_height import UpdateRowsPerPageAndTableHeight
from pages.delete_the_table import DeleteTheTableAndVerifyTheFrontendRemoval

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
    show_table_title_page = ShowTableTitleAndDescription(page)
    show_entryinfo_page = EnableEnteryInfoAndPagination(page)
    update_row_page = UpdateRowsPerPageAndTableHeight(page)
    delete_table_page = DeleteTheTableAndVerifyTheFrontendRemoval(page)



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

    # Test Case 6
    show_table_title_page.show_title_and_description()

    # Test Case 7
    show_entryinfo_page.show_entryInfo_and_pagination()

    # Test Case 8
    update_row_page.select_page_row_randomly_and_table_height_manually()
    update_row_page.verify_row_per_page_and_table_height_value()

    # Test Case 9
    delete_table_page.delete_the_table()


 
