from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import re


usernameStr = 'wafa.jil6@gmail.com'
passwordStr = 'meriem1230'

browser = webdriver.Chrome()
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))

# fill in username and hit the next button

username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(5)
# wait for transition then continue to fill items
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "password")))

password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()


WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//tr[@class='zA yO']"))).click()
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='adx']"))).click()


# after this i try to get that element then the text in that element
while (True):
    time.sleep(3)

    WebDriverWait(browser, 10).until(EC.presence_of_element_located(((By.XPATH,"//div[@class='gs gt']")))).click()
    time.sleep(3)
    shit=WebDriverWait(browser, 10).until(EC.presence_of_element_located(((By.XPATH,"//div[@class='ii gt']"))))
    with open("لسان العرب.txt", "a",encoding='utf-8') as myfile:  
        myfile.write(re.sub(r'[a-zA-Z?&;]', '', shit.text).strip())
        myfile.write('\n')
        myfile.write('\n')
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='T-I J-J5-Ji T-I-Js-Gs aap T-I-awG T-I-ax7 L3']"))).click()
    time.sleep(3)
    input_el=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,"tm"))).click()
#last page get it by hand 
