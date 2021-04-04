from selenium import webdriver

driver = webdriver.Chrome("/Users/antondieterich/Downloads/chromedriver-2")
csv = open("unis2.csv", "a")
csv.truncate(0)
csv.write(f"\"Name\";\"E-Mail\"\n")

driver.get("https://de.wikipedia.org/wiki/Liste_der_Hochschulen_in_Deutschland")

table = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/tbody')

tableContent = table.find_elements_by_tag_name("tr")
#csv.write(f"\"{uniName.text}\";\"replace\"\n")
uniSort = []
for entry in tableContent:
    uni = entry.find_elements_by_tag_name("td")
    uniName = uni[0]
    uniSort.append(uniName.text)

sorted_list = sorted(uniSort, key=str.casefold)

for i in sorted_list:
    csv.write(f"\"{i}\";\"replace\"\n")
    
csv.close()
driver.quit()