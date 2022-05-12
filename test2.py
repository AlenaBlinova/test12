from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome()
browser.get('https://www.litres.ru/pages/put_money_on_account/?descr=18')

q=browser.find_element(by=By.ID, value='code1')
q.send_keys('aW11p0' + Keys.ENTER)

try:
    assert 'Чтобы активировать промокод, зарегистрируйтесь или войдите' in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')


browser.close()