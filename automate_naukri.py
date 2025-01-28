from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

# Configure Chrome options for headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Open Naukri website
    driver.get("https://www.naukri.com/nlogin/login")

    # Log in
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)

    username_input = driver.find_element(By.ID, "usernameField")
    password_input = driver.find_element(By.ID, "passwordField")

    username_input.send_keys(os.getenv("NAUKRI_USERNAME"))
    password_input.send_keys(os.getenv("NAUKRI_PASSWORD"))
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)  # Wait for login to complete

    # Upload resume
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(os.getenv("RESUME_PATH"))
    time.sleep(5)

    # Scroll through job listings for 15 minutes
    start_time = time.time()
    while time.time() - start_time < 900:  # 15 minutes
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    print("Automation completed successfully.")
finally:
    driver.quit()
