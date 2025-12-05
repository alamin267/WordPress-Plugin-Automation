# WordPress Plugin Automation

## Overview
This project is designed to automate the testing of WordPress plugins, with a focus on key WordPress functionalities such as login, plugin status, table management, WooCommerce checkout, and more. Using **Playwright** for browser automation and **pytest** for organizing and executing tests, the goal is to ensure that your WordPress environment is consistently tested, whether for development or production purposes.

### Key Features:
- **WordPress Plugin Functionality**: Automates login, plugin status verification, table creation, and page management.
- **WooCommerce Tests**: Verifies end-to-end checkout functionality and order history.
- **Cross-Browser Testing**: Runs tests across multiple browsers using Playwright.
- **CI Integration**: Easily integrates with CI tools like GitHub Actions to ensure automated testing on every push.

## Project Structure

<img width="339" height="816" alt="image" src="https://github.com/user-attachments/assets/419fcc7b-66fc-460c-92aa-a82cd97c7f4b" />

## Technologies Used
- **Playwright**: A browser automation library to simulate user interaction with WordPress.
- **pytest**: A testing framework to run and organize your tests.
- **pytest-playwright**: Playwright integration with pytest for seamless testing.
- **python-dotenv**: Loads sensitive credentials from a `.env` file.
- **pytest-xdist**: Runs tests in parallel for faster execution.
- **pytest-html**: Generates HTML test reports for easy analysis.

## Setup

### Prerequisites
Ensure the following are installed before you start:
- **Python 3.x**
- **WordPress**: Either a local or live WordPress environment is needed for testing.
- **.env File**: To store your WordPress credentials and environment configurations.


## Technologies Used
- **Playwright**: A browser automation library to simulate user interaction with WordPress.
- **pytest**: A testing framework to run and organize your tests.
- **pytest-playwright**: Playwright integration with pytest for seamless testing.
- **python-dotenv**: Loads sensitive credentials from a `.env` file.
- **pytest-xdist**: Runs tests in parallel for faster execution.
- **pytest-html**: Generates HTML test reports for easy analysis.

### Installation

1. **Clone the Repository**:


   ```bash
   git clone https://github.com/alamin267/WordPress-Plugin-Automation.git

### Navigate to the Project Directory:

cd WordPress-Plugin-Automation


### Create a Virtual Environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


### Install Dependencies:
## Install the required Python packages listed in requirements.txt:

pip install -r requirements.txt


### Configure the .env File:
Create a .env file based on .env.example and add your WordPress credentials:
 ```bash
WP_USERNAME=your_wordpress_username
WP_PASSWORD=your_wordpress_password
WP_URL=http://your-local-or-live-wordpress-url
```
### Running Tests
Run Tests Locally:
To execute the tests locally:
```bash pytest -v ```
### Generate HTML Test Reports (Optional):
If you need an HTML report:

```bash pytest --html=report.html ```

### Parallel Test Execution (Optional):
To run the tests in parallel:

pytest -n 4  # Run tests in parallel across 4 CPUs

### CI Integration

Integrate this project into your CI/CD pipeline to automatically run tests on each push.

### GitHub Actions Integration

Create a GitHub Actions workflow in .github/workflows/python-playwright.yml:

name: Python Playwright CI

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python 3.10
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"

      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y xvfb

      - name: Install Python dependencies
        run: |
          pip install -r requirements.txt
          playwright install chromium firefox webkit

      - name: Run tests in headed local or headless CI
        env:
          CI: "true"
          WP_URL: ${{ secrets.WP_URL }}   
          WP_USERNAME: ${{ secrets.WP_USERNAME }}  
          WP_PASSWORD: ${{ secrets.WP_PASSWORD }}
        run: |
          xvfb-run pytest -v --junitxml=report.xml
          
      - name: Upload test reports as artifact
        uses: actions/upload-artifact@v3
        with:
          name: test-reports
          path: report.xml  ```

### Configure Secrets in GitHub:

Go to your repository’s Settings > Secrets and add:

WP_USERNAME
WP_PASSWORD
WP_URL

## Test Suite
## WordPress Plugin Tests
test_FlexTable_Plugin.py

Login Functionality: Verifies that valid WordPress credentials can log in.
Plugin Status: Ensures the installed plugins are functioning correctly.
Table Management: Verifies creating, updating, and deleting tables.
test_WooCommerce_Checkout.py
End-to-End Checkout: Tests the complete checkout flow in WooCommerce.
Order History: Verifies that order history is visible and accurate.

## WooCommerce Tests

End_to_End_Checkout_Flow.py
Tests the complete checkout experience, ensuring products can be added to the cart and the final price is correct.
User_Account_Order_History.py
Verifies the order history functionality for users.
Test Reporting

Once the tests are complete, an XML file (report.xml) will be generated. This can be used for further reporting or visualization tools like Allure.

### Contributing

## Fork the repository.

Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to your branch (git push origin feature-branch).
Create a pull request for review.

### License

This project is licensed under the MIT License - see the LICENSE
 file for details.

### Acknowledgments
Playwright: For powerful browser automation.
pytest: For being a robust testing framework.
WooCommerce: For making e-commerce automation possible.









