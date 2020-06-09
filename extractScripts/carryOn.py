from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver


usernameStr = 'wafa.jil@hotmail.com'
passwordStr = 'tashaba123'


browser = webdriver.Chrome("C:\webdriver\chromedriver.exe")
browser.get('http://www.alwaraq.net')

nextButton = browser.find_element_by_id('welcome')
nextButton.click()

username = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME,'useremail')))
username.send_keys(usernameStr)

password = browser.find_element_by_name('password')
password.send_keys(passwordStr)

signInButton = browser.find_element_by_xpath("//input[@type='image']").click()

nextButton= WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT,'لسان العرب'))).click()

nextButton= WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT,'إقرأ الكتاب'))).click()
nextpage=WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME,'currentpage')))
nextpage.send_keys('34')
Button = browser.find_element_by_xpath("//a[@title='اذهب إلى صفحة معينة']").click()
i=0
while (i<=100):
    time.sleep(3)
    nextButton= WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//a[@href='javascript:OpenEmailWin()']"))).click()
    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    email = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME,'ccmail')))
    email.send_keys('wafa.jil6@gmail.com')
    formatt = browser.find_element_by_name('PageFormat').click()
    sendButton = browser.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(3)
    browser.close()
    browser.switch_to.window(handles[0])
    nextButton= WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//a[@href='javascript:target(2)']"))).click()
    i+=1
