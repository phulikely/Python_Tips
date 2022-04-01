# pip install webdriver-manager
# https://pypi.org/project/webdriver-manager/
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com/")
driver.maximize_window()
# print(driver.title)

searching = driver.find_element_by_name('q')
searching.send_keys('Nokonoshima Island')
searching.send_keys(Keys.ENTER)

time.sleep(3)
link_img = driver.find_element_by_link_text('Hình ảnh')
link_img.click()

time.sleep(3)
driver.quit
