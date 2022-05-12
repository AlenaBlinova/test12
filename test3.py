from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
browser.get('https://www.litres.ru/')

button=browser.find_element(by=By.CSS_SELECTOR, value='#cover_art_51366732')
button.click()

button=browser.find_element(by=By.CLASS_NAME, value='recenses-unit')
button.click()

try:
    assert 'Встретимся на Кассандре!' in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')

browser.close()