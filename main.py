import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Edge()


browser.get('http://makemytrip.com')

browser.implicitly_wait(10)
close=browser.find_element(By.XPATH,"//span[@data-cy='closeModal']")
browser.execute_script("arguments[0].click();",close)
browser.find_element(By.XPATH, "//input[@id='fromCity']").send_keys('Hyd')
Action=ActionChains(browser)
time.sleep(2)
Action.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
time.sleep(2)
browser.find_element(By.XPATH,"//input[@id='toCity']").send_keys('Mumbai')
time.sleep(2)
Action.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
time.sleep(2)
dep=browser.find_element(By.XPATH,"//input[@id='departure']")
browser.execute_script("arguments[0].click();",dep)
time.sleep(2)
dep_date=browser.find_element(By.XPATH,"//div[@aria-label='Thu Oct 26 2023']")
browser.execute_script("arguments[0].click();",dep_date)
ret=browser.find_element(By.XPATH,"//p[@data-cy='returnDefaultText']")
browser.execute_script("arguments[0].click();",ret)

ret_date=browser.find_element(By.XPATH,"//div[@aria-label='Tue Oct 31 2023']")
browser.execute_script("arguments[0].click();",ret_date)


search=browser.find_element(By.XPATH,"//p//a[contains(@class,'Search')]")
browser.execute_script("arguments[0].click();",search)
WebDriverWait(browser,20).until(ec.presence_of_element_located((By.XPATH,"//div[@class='flightsContainer makeFlex spaceBetween']//*[@class='font24 blackFont whiteText appendBottom20 journey-title makeFlex spaceBetween bottom']/span")))
result=browser.find_element(By.XPATH,"//div[@class='flightsContainer makeFlex spaceBetween']//*[@class='font24 blackFont whiteText appendBottom20 journey-title makeFlex spaceBetween bottom']/span")


print(result.text)
assert result.text =='Flights from Hyderabad to Mumbai, and back'

# Find the search box


browser.quit()