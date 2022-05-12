from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()
browser.get('https://www.litres.ru/')

q=browser.find_element(by=By.NAME, value='q')
q.send_keys('Эффект врат' + Keys.ENTER)


try:
    assert 'Эффект врат' in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
browser.close()