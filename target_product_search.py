from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver_path = ChromeDriverManager().install()
service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

driver.get("https://www.target.com")

search_word = "valentine cards"
driver.find_element(By.ID, "search").send_keys(search_word)
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(6)
actual_text = driver.find_element(By.XPATH, "//*[@data-test='resultsHeading']").text
assert search_word in actual_text, f"The expected word '{search_word}' didn't match the actual word '{actual_text}'"

print("Test case passed!")
driver.quit()

