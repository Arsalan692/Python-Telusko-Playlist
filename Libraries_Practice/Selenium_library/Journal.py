
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "D:/chrome_driver/chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://adamjeecoaching.blogspot.com/")
search = driver.find_element_by_id("s")
search.send_keys("Mathematics 11th")
search.send_keys(Keys.RETURN)

#print(driver.title)     It prints the title of the page











