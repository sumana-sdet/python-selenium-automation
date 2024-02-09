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
sleep(6)
driver.refresh()
# click on sign in
driver.find_element(By.ID, "nav-link-accountList").click()
sleep(3)

# click on create account button
driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit").click()

# amazon header image
driver.find_element(By.CSS_SELECTOR, "[aria-label='Amazon']")

# create account header
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# name text field
driver.find_element(By.CSS_SELECTOR, "[name='customerName']")

# email text field
driver.find_element(By.CSS_SELECTOR, "[type='email']")

# password text field
driver.find_element(By.CSS_SELECTOR, "[name='password']")

# re-enter password text field
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# continue button
driver.find_element(By.CSS_SELECTOR, "#continue")

# condition of use
driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use']")

# privacy notice
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_privacy_notice']")

# signin link
driver.find_element(By.CSS_SELECTOR, "[href*='signin']")

driver.quit()