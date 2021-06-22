from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(executable_path='C:/Users/michael.yu/PycharmProjects/Self-Test Platform/chromedriver.exe')
driver.maximize_window()
driver.get('https://stp-uat.paymark.co.nz/logon.htm?locale=en_US')
assert 'Login' in driver.title
email = driver.find_element_by_id('email').send_keys('michael.yu@paymark.co.nz')
password = driver.find_element_by_id('password').send_keys('MiC281290')
login = driver.find_element_by_id('loginButton').click()
time.sleep(2)
ad_list = driver.find_element_by_xpath('//*[@id="crfo-nav"]/ul[3]/li[3]/ul')
for item in ad_list.find_elements_by_tag_name('li'):
    print(item.get_attribute("innerHTML"))
    if item.get_attribute("innerHTML") == '<a id="menu.TCMTestPlans" href="/tcm/testplans.htm">Test case management</a>':
        driver.get('https://stp-uat.paymark.co.nz/tcm/testplans.htm')
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'text ng-binding')))
state = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'mainBtnFilter_TestPlans')))
time.sleep(2)
state.click()
driver.find_element_by_xpath('//*[@id="contentFilter_TestPlans"]/ul[1]/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="tcmTestPlansBlock"]/div/div/div[1]/div[3]/tcm-filter/div/div[2]/button').click()
test_plans = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'testPlansTable')))
count_row = len(driver.find_elements_by_xpath('//*[@id="testPlansTable"]/tbody/tr'))
count_col = len(driver.find_elements_by_xpath('//*[@id="testPlansTable"]/thead/tr/th'))

for t_row in range(1, (count_row+1)):
    for t_col in range(1, (count_col)):
        table_xpath = driver.find_element_by_xpath('//*[@id="testPlansTable"]')
        cell = driver.find_element_by_xpath(f'//*[@id="testPlansTable"]/tbody/tr[{str(t_row)}]/td[{str(t_col)}]').text
        print(cell)

for item in range(1, (2)):
    for col in range(1(1)):
        