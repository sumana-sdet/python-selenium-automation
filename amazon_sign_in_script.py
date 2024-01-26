from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# path of chromedriver executable
driver_path = ChromeDriverManager().install()

# create Chrome browser instance
service = Service(driver_path)

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# open the url
driver.get("https://www.amazon.com/")

sleep(3)

driver.find_element(By.ID, "nav-link-accountList").click()

# amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# email field
driver.find_element(By.ID, "ap_email").send_keys("abc.abc@gmail.com")

# continue button
driver.find_element(By.ID, "continue")

# conditions to use link
driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions')]")

# privacy notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# need help link
driver.find_element(By.XPATH, "//span[contains(text(),'Need help')]").click()

# forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom")

# other issues with sing-in link
driver.find_element(By.ID, "ap-other-signin-issues-link")

# create your amazon account button
driver.find_element(By.ID, "createAccountSubmit")

driver.quit()