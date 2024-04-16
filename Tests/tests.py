###
#Script to test functions
###

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://google.com")
driver.maximize_window()
time.sleep(3)
driver.close()
driver.quit()