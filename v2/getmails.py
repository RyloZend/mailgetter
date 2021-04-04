from selenium import webdriver
import re

with open('searchuni.csv') as f:
    unis = f.read().splitlines()

uniMails = open("unimails.csv", "a")
uniMails.truncate(0)
uniMails.write(unis[0])
uniMails.write("\n")
uniMails.close()

unis.pop(0)

print(len(unis))

driver = webdriver.Chrome("/Users/antondieterich/Downloads/chromedriver-2")
tmpdriver = webdriver.Chrome("/Users/antondieterich/Downloads/chromedriver-2")

def findMail(text):
    if re.findall(r"[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*", text):
        return re.findall(r"[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*", text)[0]
    elif re.findall(r"[A-Za-z0-9\.\+_-]+[(]+[a]+[t]+[)]+[A-Za-z0-9\._-]+\.[a-zA-Z]*", text):
        return re.findall(r"[A-Za-z0-9\.\+_-]+[(]+[a]+[t]+[)]+[A-Za-z0-9\._-]+\.[a-zA-Z]*", text)[0]
    else:
        return False

#uniMails.write(f"\"{uniName}\";\"{mail}\"")

def checkMail(mail):
    if mail:
        if "info" in mail:
            return mail
        elif "rektor" in mail:
            return mail
    print("No Mail found")
    return False

for uni in unis:
    try:
        uniName = uni.split(";")[0]
        #uniName = uniName[1:][:-1]
        print(uniName)
        driver.get("https://google.com")
        searchBar = driver.find_element_by_name('q')
        searchBar.send_keys(uniName)
        searchBar.send_keys('\n')
        results = driver.find_element_by_id("rso")
        uniPage = results.find_elements_by_class_name("hlcw0c")[0]
        uniPage = uniPage.find_elements_by_class_name("g")[0]
        uniPage = uniPage.find_elements_by_tag_name("a")[0].get_attribute("href")
        driver.get(uniPage)
        html = driver.find_element_by_tag_name("html")
        mail = findMail(html.get_attribute("innerHTML"))
        links = driver.find_elements_by_tag_name("a")
        mail = checkMail(mail)
        if mail: 
            uniMails = open("unimails.csv", "a")
            uniMails.write(f"\"{uniName}\";\"{mail}\"\n")
            uniMails.close()
            print(mail)
            continue
        for link in links:
            if "Impressum".upper() in link.get_attribute('innerHTML').upper():
                print("Found Impressum")
                tmpdriver.get(link.get_attribute('href'))
                body = tmpdriver.find_element_by_tag_name("html")
                mail = findMail(body.get_attribute("innerHTML"))
                if mail:
                    print(mail)
                    uniMails = open("unimails.csv", "a")
                    uniMails.write(f"\"{uniName}\";\"{mail}\"\n")
                    uniMails.close()
                    #tmpdriver.close()
                    break
                #tmpdriver.close()
            elif "Kontakt".upper() in link.get_attribute('innerHTML').upper():
                print("Found Kontakt")
                tmpdriver.get(link.get_attribute('href'))
                body = tmpdriver.find_element_by_tag_name("html")
                mail = findMail(body.get_attribute("innerHTML"))
                if mail:
                    print(mail)
                    uniMails = open("unimails.csv", "a")
                    uniMails.write(f"\"{uniName}\";\"{mail}\"\n")
                    uniMails.close()
                    #tmpdriver.close()
                    break
                #tmpdriver.close()
    except:
        print("Err")
        continue

tmpdriver.close()
driver.close()
print("Got all Mails")