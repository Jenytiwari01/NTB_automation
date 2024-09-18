# import random
# import time
# from selenium.webdriver import ActionChains
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# from selenium.webdriver.common.keys import Keys

# # Path to the chromedriver executable
# chrome_driver_path = r'C:\drivers\chromedriver\chromedriver.exe'

# # Initialize webdriver
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)

#     # Open URL and maximize window
# driver.get('http://192.168.1.74:2323/Security/Login')
# driver.maximize_window()

# username_field = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/main/div/div/div/div[2]/form/div[2]/label')
# password_field = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/main/div/div/div/div[2]/form/div[3]/label')

# username_field.send_keys("012")
# password_field.send_keys("12345")

# password_field.send_keys(Keys.RETURN)

# # Optionally, wait for the login process to complete and access a new page
# # Wait up to 10 seconds for elements to load

# time.sleep(100)
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# Path to the chromedriver executable
chrome_driver_path = r'C:\drivers\chromedriver\chromedriver.exe'

# Initialize webdriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open URL and maximize window
    driver.get('http://192.168.1.74:2323/Security/Login')
    driver.maximize_window()

#     dropdown_office = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//span[@class='select2-selection__arrow']"))
# )
#     print("element selected")
# # Click to open the dropdown
#     dropdown_office.click()

#     # Wait for the dropdown options to be visible
#     options = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='select2-results__options']/li"))
#     )

#     # List of options to select
#     options_to_select = ['Kathmandu', 'Pokhara', 'Lumbini']

#     for option_text in options_to_select:
#         for option in options:
#             if option_text in option.text:
#                 option.click()
#                 print(f"Selected: {option_text}")
#                 break

#         # Optional: Add a short delay to observe changes
#         time.sleep(2)

#     # Verify the selected option
#     final_selected_option = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//span[@class='select2-selection__rendered']"))
#     ).text
#     print(f"Final selected option: {final_selected_option}")

    options_to_select = ['Pokhara', 'Lumbini', 'Kathmandu']

    # Remove "Kathmandu" from the list for now
    # if 'Kathmandu' in options_to_select:
    #     options_to_select.remove('Kathmandu')

    # Iterate through other options first
    for option_text in options_to_select:
        # Open the dropdown for each option
        dropdown_office = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='select2-selection__arrow']"))
        )
        dropdown_office.click()

        # Wait for the dropdown options to be visible
        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='select2-results__options']/li"))
        )

        # Select the correct option
        for option in options:
            if option_text in option.text:
                option.click()
                print(f"Selected: {option_text}")
                break

        # Optional: Add a short delay to observe changes
        time.sleep(2)

    # Finally, select "Kathmandu"
    dropdown_office = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='select2-selection__arrow']"))
    )
    dropdown_office.click()

    # Wait for the dropdown options to be visible
    options = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='select2-results__options']/li"))
    )

    for option in options:
        if 'Kathmandu' in option.text:
            option.click()
            print("Selected: Kathmandu")
            break

    # Optional: Add a short delay to observe changes
    time.sleep(2)

    # Verify the final selected option
    final_selected_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='select2-selection__rendered']"))
    ).text
    print(f"Final selected option: {final_selected_option}")

    # Wait until the username and password fields are present
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="username"]')))
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))

    # Enter credentials
    username_field.send_keys("012")
    password_field.send_keys("12345")
    time.sleep(5)
    # Submit the form
    password_field.send_keys(Keys.RETURN)
    time.sleep(10)
    # Wait for the new page to load or some element on the new page
    # Update the XPath to an element on the new page or use the appropriate wait condition
    # Attempt some action that might fail if the window is closed
    menu_toggle_button = driver.find_element(By.XPATH, "//div[@class='menuToggleButton']")
    menu_toggle_button.click()
    time.sleep(5)
    security_click=driver.find_element(By.XPATH,"//a[@id='a-5']")
    security_click.click()
    time.sleep(5)

    user_acess = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='16']")))
    # Perform actions on the element
    user_acess.click()

    # user_acess=driver.find_element(By.XPATH,"//label[@class='col-md-3 float-start']")
    # user_acess.click()
    # # Optionally, interact with the new page here
   
    # dropdown_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@class='form-control form-select input-sm']")))
    # Wait for the options to be populated
    dropdown_elementMO=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//select[@id='ddlOffice']")))
#    (By.XPATH, "//select[@id='ddlOffice']/option[text()='Kathmandu']")
    # print("element found")
    dropdown_elementMO.click()

    select = Select(dropdown_elementMO)

# List of options to select
    options_to_select = ['Kathmandu', 'Pokhara', 'Lumbini']

    for option in options_to_select:
        # Select the option by visible text
        select.select_by_visible_text(option)
        
        # Perform any action you want to do after selecting the option
        # For example, you might want to print the selected option
        print(f"Selected: {option}")

        # print(f"Currently selected: {selected_option}")
        final_selected_option = select.first_selected_option.text
        print(f"Final selected option: {final_selected_option}")
        # Optional: Add a short delay if needed to observe changes
        import time
        time.sleep(2)  # Sleep for 2 seconds

        print("Option selected and events dispatched")

        time.sleep(5)

        close_button = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "//select[@id='ddlOffice']")))
        close_button.click()

    #     user_dropdown = WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.XPATH, "//select[@id='ddlOfficeUser']/option[text()='Jeny']"))
    # )
   
    # print("element found")
    # user_dropdown.click()
    # time.sleep(5)

#     driver.execute_script("arguments[0].value = 'Kathmandu';", dropdown_element)

# # Optionally, trigger a change event in case the page requires it to detect the change
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", dropdown_element)

#     print("Value set successfully")

 # select = Select(dropdown_elementMO)
    # select.select_by_value("Kathmandu")
    # select.select_by_visible_text("Kathmandu")
    # select.select_by_index(0)



    # select = Select(dropdown_element)


    # select.select_by_visible_text("Kathmandu")

# Or, you can select by value (assuming the options have value attributes)
# select.select_by_value("Kathmandu") 

# Or, you can select by index (0-based index)
# select.select_by_index(1)  # This will select the second option in the dropdown

   

finally:
    # Wait for a while to observe the result
    time.sleep(10)

    # Close the WebDriver
    driver.quit()
