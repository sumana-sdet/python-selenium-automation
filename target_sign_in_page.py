from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)

driver.get("https://www.target.com")

driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

# sleep(3)
SIGN_IN_ACCOUNT = (By.XPATH, "//span[contains(text(),'Target account')]")
driver.wait.until((
    EC.presence_of_element_located(SIGN_IN_ACCOUNT)),
    message='Sign in text is not located.'
)
sign_in_account_text = driver.find_element(*SIGN_IN_ACCOUNT).text
# print(sign_in_account_text)
assert "Target account" in sign_in_account_text, f"Expected word didn't appear in {sign_in_account_text}"

sign_in_button_text = driver.find_element(By.ID, "login").is_displayed()
# print("sign in button present :" + str(sign_in_button_text))
assert sign_in_button_text is True, f"Sign in button is not displayed"

print("Test case passed!")
driver.quit()
