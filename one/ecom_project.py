import random
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Path to the chromedriver executable
chrome_driver_path = r'C:\drivers\chromedriver\chromedriver.exe'

# Initialize webdriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open URL and maximize window
    driver.get('http://tutorialsninja.com/demo/')
    driver.maximize_window()

    # Phones button
    phones = driver.find_element(By.XPATH, '//a[text()="Phones & PDAs"]')
    phones.click()

    # iPhone
    iphone = driver.find_element(By.XPATH, '//a[text()="iPhone"]')
    iphone.click()
    time.sleep(1)

    # First picture
    first_pic = driver.find_element(By.XPATH, '//ul[@class="thumbnails"]/li[1]')
    first_pic.click()
    time.sleep(2)

    # Next picture
    next_click = driver.find_element(By.XPATH, '//button[@title="Next (Right arrow key)"]')
    for i in range(5):
        next_click.click()
        time.sleep(2)

    # Save screenshot
    screenshot_filename = 'screenshot#' + str(random.randint(0, 101)) + '.png'
    driver.save_screenshot(screenshot_filename)
    print(f"Screenshot saved as {screenshot_filename}")

    # Close picture view
    x_button = driver.find_element(By.XPATH, '//button[@title="Close (Esc)"]')
    x_button.click()
    time.sleep(1)

    # Set quantity
    quantity = driver.find_element(By.ID, 'input-quantity')
    quantity.clear()
    quantity.send_keys('2')
    time.sleep(1)

    # Add to cart
    add_to_button = driver.find_element(By.ID, 'button-cart')
    add_to_button.click()
    time.sleep(2)

    # Hover over and select Laptops & Notebooks
    laptops = driver.find_element(By.XPATH, '//a[text()="Laptops & Notebooks"]')
    action = ActionChains(driver)
    action.move_to_element(laptops).perform()
    time.sleep(2)

    laptops_2 = driver.find_element(By.XPATH, '//a[text()="Show AllLaptops & Notebooks"]')
    laptops_2.click()
    time.sleep(1)

    # Click on HP laptop
    HP = driver.find_element(By.XPATH, '//a[text()="HP LP3065"]')
    HP.click()

    # Scroll to add to cart button
    add_to_button_2 = driver.find_element(By.XPATH, '//button[@id="button-cart"]')
    driver.execute_script("arguments[0].scrollIntoView();", add_to_button_2)
    time.sleep(1)

    # Select date
    # calendar = driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
    # calendar.click()
    # time.sleep(1)

    next_click_calendar = driver.find_element(By.XPATH, '//th[@class="next"]')
    month_year = driver.find_element(By.XPATH, '//th[@class="picker-switch"]')

    while month_year.text != 'December 2022':
        next_click_calendar.click()
        time.sleep(2)

    calendar_date = driver.find_element(By.XPATH, '//td[text()="31"]')
    calendar_date.click()
    time.sleep(2)

    # Add to cart
    add_to_button_2.click()
    time.sleep(1)

    # Checkout
    go_to_cart = driver.find_element(By.ID, 'cart-total')
    go_to_cart.click()
    time.sleep(1)

    checkout = driver.find_element(By.XPATH, '//p[@class="text-right"]/a[2]')
    checkout.click()
    time.sleep(1)

    # Click on guest account
    try:
        guest = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@value="guest"]'))
        )
        guest.click()
        print("Clicked on guest account.")
    except TimeoutException:
        print("TimeoutException: Guest account element not found or not interactable.")
        driver.save_screenshot('timeout_guest_element.png')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        driver.save_screenshot('unexpected_error.png')

    # Click continue 1
    try:
        continue_1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'button-account'))
        )
        continue_1.click()
        print("Clicked on Continue button.")
    except TimeoutException:
        print("TimeoutException: Continue button element not found or not interactable.")
        driver.save_screenshot('timeout_continue_button.png')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        driver.save_screenshot('unexpected_continue_error.png')

    # Step 2: Billing Details
    step_2 = driver.find_element(By.XPATH, '//a[text()="Step 2: Billing Details "]')
    driver.execute_script("arguments[0].scrollIntoView();", step_2)
    time.sleep(2)

    # Fill billing details
    first_name = driver.find_element(By.ID, 'input-payment-firstname')
    first_name.send_keys('test_first_name')
    last_name = driver.find_element(By.ID, 'input-payment-lastname')
    last_name.send_keys('test_last_name')
    email = driver.find_element(By.ID, 'input-payment-email')
    email.send_keys('test@test.com')
    telephone = driver.find_element(By.ID, 'input-payment-telephone')
    telephone.send_keys('012345678')
    address = driver.find_element(By.ID, 'input-payment-address-1')
    address.send_keys('teststreet 187')
    city = driver.find_element(By.ID, 'input-payment-city')
    city.send_keys('Frankfurt')
    postcode = driver.find_element(By.ID, 'input-payment-postcode')
    postcode.send_keys('112233')

    # Country and region selection
    country = driver.find_element(By.ID, 'input-payment-country')
    Select(country).select_by_index(87)
    region = driver.find_element(By.ID, 'input-payment-zone')
    Select(region).select_by_visible_text('Hessen')

    # Click continue 2
    continue_2 = driver.find_element(By.ID, 'button-guest')
    continue_2.click()
    time.sleep(1)

    # Click continue 3
    continue_3 = driver.find_element(By.ID, 'button-shipping-method')
    continue_3.click()
    time.sleep(1)

    # Accept terms & conditions
    t_e = driver.find_element(By.NAME, 'agree')
    t_e.click()
    time.sleep(1)

    # Click continue 4
    continue_4 = driver.find_element(By.ID, 'button-payment-method')
    continue_4.click()
    time.sleep(3)

    # Final price
    final_price = driver.find_element(By.XPATH, '//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')
    print("The final price of both products is " + final_price.text)
    time.sleep(2)

    # Click on the confirmation button
    confirmation_button = driver.find_element(By.ID, 'button-confirm')
    confirmation_button.click()
    time.sleep(2)

    # Success text
    success_text = driver.find_element(By.XPATH, '//div[@class="col-sm-12"]/h1')
    print(success_text.text)

finally:
    driver.quit()
