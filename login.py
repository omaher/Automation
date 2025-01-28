from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Start Chrome maximized
options.add_argument("--disable-notifications")  # Disable browser notifications

# Setup WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Open the sample website (e.g., a login page)
driver.get("https://www.facebook.com/login")  # Replace with your website URL

# Wait for the page to load completely
time.sleep(2)  # Optional: Adjust the sleep time depending on the website speed

# Locate the username and password fields and login button
username_field = driver.find_element(By.NAME, "username")  # Replace with correct field name
password_field = driver.find_element(By.NAME, "password")  # Replace with correct field name
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Adjust this as per the website's structure

# Send username and password (Replace with actual credentials)
username_field.send_keys("omkaraher@gmail.com")
password_field.send_keys("Omkar")

# Click the login button
login_button.click()

# Wait for a few seconds to see the result (or wait for successful login)
time.sleep(5)

# Close the browser
driver.quit()
