from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import re,requests
from urllib.request import urlopen
from time import sleep
import time
from selenium.common.exceptions import TimeoutException

def cond(url):
    liste=[]
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for tr in soup.findAll('td'):
        liste.append(tr)
    return liste

def Gothrough(url):
    driver = webdriver.PhantomJS() #initialize the webdriver
    liste=cond(url)

    for tr in liste:#start with this element 
        try:
            link = tr.find('a').get('href')
            source_code = requests.get("http://shamela.ws"+link)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "lxml")
            rows = soup.findAll('h3')
            for r in rows:
                nameBook= r.text.split("\t")[0].replace("\n","")
                lin=r.find('a').get('href')#get an author link
                source_code2 = requests.get("http://shamela.ws"+lin)
                plain_text2 = source_code2.text
                soup = BeautifulSoup(plain_text2, "lxml")
                nameAuthor=soup.find('h3').text.replace("\n\t","")
                td_list = soup.find_all('td')
                deathYear=td_list[3].text.split("\t")[0].replace("\n","")
            iden=link.split("/")[3]
            fil = open(re.sub("\s+"," ",nameBook)+"_"+re.sub("\s+"," ",nameAuthor)+"_"+re.sub("\s+"," ",deathYear)+".txt" , encoding="utf-8" , mode="w")
########################################################################################################################
            string=""
            jj=2
            driver.set_page_load_timeout(10)
            while(True):
                try:
                    driver.get("http://shamela.ws/browse.php/book-"+iden+"#page-"+str(jj))
                    sleep(2)
                    html_page = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")  # get the HTML page
                    resu = BeautifulSoup(html_page, "lxml")
                    for mt in resu.find_all("div" , {"id" : "book-container"}):
                        string=string+mt.text 
                    print(str(driver.current_url))

                    if (jj==102) or str(driver.current_url)=="http://shamela.ws/browse.php/book-"+iden+"#page-"+str(jj-1):
                        print("break")
                        break
                    else:
                        jj+=1
                except TimeoutException as e:
                    print(e)
                    continue

            fil.write(re.sub("\s+"," ",string))
        except:
            continue
##################################################################################################################
#http://shamela.ws/index.php/category/115 6 eme 
#http://shamela.ws/index.php/category/158 all
#Gothrough("http://shamela.ws/index.php/category/114/page-2")#32
#Gothrough("http://shamela.ws/index.php/category/114/page-4")
###############################################################################""
Gothrough("http://shamela.ws/index.php/category/142")




