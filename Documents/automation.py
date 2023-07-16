import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def automate_country_info(country_name):
    # Launch the web browser
    driver = webdriver.Chrome()

    # Navigate to the HTML page
    driver.get('D:\website\public\index.html')

    # Wait for the input field and button to become visible
    wait = WebDriverWait(driver, 10)
    country_name_input = wait.until(EC.visibility_of_element_located((By.ID, 'countryName')))
    button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'button')))

    # Enter the country name and click the button
    country_name_input.send_keys('india')
    button.click()

    # Wait for the country information to appear
    time.sleep(8)  # Add a 3-second delay
    country_result = wait.until(EC.visibility_of_element_located((By.ID, 'countryResult')))

    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Add a 3-second delay after scrolling

    # Extract the country information
    country_info = country_result.get_attribute('innerHTML')
    print(country_info)

    # Close the web browser
    driver.quit()

automate_country_info('india')

