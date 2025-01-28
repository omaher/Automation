from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # Open Naukri.com
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(5)  # Wait for the page to load

    # Click on the login button
    #login_button = driver.find_element(By.LINK_TEXT, "Login")
    #login_button.click()
    time.sleep(3)

    # Enter your username and password
    username = driver.find_element(By.ID, "usernameField")
    password = driver.find_element(By.ID, "passwordField")

    username.send_keys("omkarbaher@gmail.com")
    password.send_keys("hCKNK@98")

    # Click the login button
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(5)  # Wait for login to complete

    # Navigate to the profile section to upload CV
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)

    # Click the "Update Resume" button
    update_resume_button = driver.find_element(By.XPATH, "//input[@value='Update resume']")
    update_resume_button.click()
    time.sleep(2)  # Wait for the file upload dialog to appear

    # Handle the file upload dialog using AutoIT or PyAutoGUI
    # Here, we'll use PyAutoGUI for simplicity
    import pyautogui

    # Wait for the file upload dialog to appear
    time.sleep(2)

    # Type the path of the CV file
    pyautogui.write(r"C:\GITHUB\Automation\resources\Omkar_Aher_resume_5years.pdf")  # Replace with the actual path to your CV
    time.sleep(1)

    # Press Enter to confirm the file selection
    pyautogui.press("enter")
    time.sleep(5)  # Wait for the upload to complete
    # Scroll for 15 minutes
    start_time = time.time()
    while time.time() - start_time < 900:  # 900 seconds = 15 minutes
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(5)  # Scroll every 5 seconds

finally:
    # Close the browser
    driver.quit()