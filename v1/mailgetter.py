from selenium import webdriver
import re
import time


def getMailbyName(name):
    try:
        driver = webdriver.Chrome("/Users/antondieterich/Downloads/chromedriver-2")
        driver.get("https://google.com")
        searchBar = driver.find_element_by_name('q')
        searchBar.send_keys(name)
        searchBar.send_keys('\n')
        element = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/a').get_attribute("href")
        driver.get(element)
        impressum = driver.find_elements_by_tag_name('a')
        for i in impressum:
            if "Impressum".upper() in i.get_attribute('innerText').upper():
                impressum = i
            elif "Kontakt".upper() in i.get_attribute('innerText').upper():
                impressum = i
            elif "Presse".upper() in i.get_attribute('innerText').upper():
                impressum = i
        driver.get(impressum.get_attribute("href"))
        el = driver.page_source
        mail = "Error"
        if re.findall(r"[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*", el):
            mail = re.findall(r"[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*", el)[0]
        elif re.findall(r"[A-Za-z0-9\.\+_-]+[(]+[a]+[t]+[)]+[A-Za-z0-9\._-]+\.[a-zA-Z]*", el):
            mail = re.findall(r"[A-Za-z0-9\.\+_-]+[(]+[a]+[t]+[)]+[A-Za-z0-9\._-]+\.[a-zA-Z]*", el)[0]
        else:
            mail = "Error finding Email"
        driver.close()
        return mail
    except:
        driver.close()
        print(f"{name} got error")

liste = open("schule.txt", "r")
for line in liste:
    unimail = getMailbyName(line.replace("\n", ""))
    f = open("mails.txt", "a")
    f.write(f"Uni: {line} Mail: {unimail}\n")
    f.close()