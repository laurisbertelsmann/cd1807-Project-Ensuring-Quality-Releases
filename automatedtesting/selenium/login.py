# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime
import time
from selenium.common.exceptions import NoSuchElementException

def print_output (message):
    timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print (timestamp + ': ' + message)
    
    
    
# Start the browser and login with standard_user
def login (driver, user, password):
    driver.get('https://www.saucedemo.com/')
    print_output('Browser started successfully. Navigating to the demo page to login.')
    username = driver.find_element(By.ID, 'user-name')
    print_output('Finding and Entering username: {user}')
    username.send_keys(user)
    time.sleep(1)
    
    user_pw = driver.find_element(By.ID, 'password')
    print_output('Finding and Entering password')
    user_pw.send_keys(password)
    time.sleep(1)
      
    button = driver.find_element(By.ID, 'login-button')
    print_output('Clicking Submit button')
    button.click()
    header = driver.find_element(By.CLASS_NAME, 'title')

    assert header.text == "Products", "ERROR: LOGIN ACTION UNSUCCESSFUL"
    print_output('Login successful')
    time.sleep(2)
    

def create_driver():
    print_output("Starting the browser...")
    chrome_options.binary_location = "/usr/local/bin/chromedriver"
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--remote-debugging-port=9515")
    driver = webdriver.Chrome(options=chrome_options) # Updated this line
    return driver

def add_to_cart(driver, product_name):
    driver.get('https://www.saucedemo.com/inventory.html')
    print_output(f'Ordering a product: {product_name}')
    button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    button.click()
    time.sleep(2)

    driver.get('https://www.saucedemo.com/cart.html')
    # Find the cart badge that holds the number of items in the cart
    cart_product_name = driver.find_element(By.CLASS_NAME, 'inventory_item_name')

    # Assert that the cart badge's text is '1', indicating one item in the cart
    assert cart_product_name.text == product_name, f"ERROR: Failed to add {product_name} to cart"
    print_output(f'{product_name} added to cart successfully')
    time.sleep(2)

def remove_from_cart(driver, product_name):
    driver.get('https://www.saucedemo.com/cart.html')
    print_output(f'Removing a product: {product_name}')
    button = driver.find_element(By.ID, 'remove-sauce-labs-backpack')
    button.click()
    time.sleep(4)
    
    # Check that object remove-sauce-labs-backpack is not present
    try:
        driver.find_element(By.ID, 'remove-sauce-labs-backpack')
        raise AssertionError(f"ERROR: Failed to remove {product_name} from cart")
    except NoSuchElementException:
        print_output(f'{product_name} removed from cart successfully')
    

if __name__ == "__main__":
    driver=create_driver()
    login(driver, 'standard_user', 'secret_sauce')
    add_to_cart(driver, 'Sauce Labs Backpack')
    remove_from_cart(driver, 'Sauce Labs Backpack')
    