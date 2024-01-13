import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
import csv

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.ss.lv/lv/"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.ID, "mtd_59")
find.click()

find = driver.find_element(By.ID, "ahc_14195")
find.click()

find = driver.find_element(By.ID, "ahc_1106")
find.click()

find = driver.find_element(By.ID, "f_o_8_min")
find.send_keys("250")

find = driver.find_element(By.ID, "f_o_8_max")
find.send_keys("700")

find = driver.find_element(By.ID, "f_o_4_min")
find.send_keys("2")

find = driver.find_element(By.ID, "f_o_4_max")
find.send_keys("3")

find = driver.find_element(By.NAME, "topt[1][max]")
select = Select(find)
select.select_by_value("2")

find = driver.find_element(By.XPATH, f'//option[@value="/lv/real-estate/flats/riga/centre/filter/photo/"]')
find.click()

find = driver.find_element(By.XPATH, f'//option[@value="/lv/real-estate/flats/riga/centre/hand_over/filter/photo/"]')
find.click()

with open("ads.csv", "w", newline='', encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    headers = ["Apraksts", "Cena", "Istabas", "Stāvs", "Iela", "Saite"]
    csv_writer.writerow(headers)

    ads = set()
    for page in range(1, 4):  
        find = driver.find_elements(By.CLASS_NAME, "d8")

        for element in find:
            content = element.text.split("\n")
            apraksts = content[1] if len(content) > 1 else ""
            cena = content[6] if len(content) > 6 else ""
            istabas = content[2] if len(content) > 2 else ""
            stāvs = content[4] if len(content) > 4 else ""
            iela = content[0] if len(content) > 0 else ""
            saite = element.find_element(By.TAG_NAME, "a")
            saite = saite.get_attribute("href")
            
            if apraksts not in ads:
                csv_writer.writerow([apraksts, cena, istabas, stāvs, iela, saite])
                ads.add(apraksts)
        time.sleep(1)
        try:
            pages = driver.find_element(By.CLASS_NAME, "navi")
            driver.execute_script("arguments[0].click();", pages)
        except NoSuchElementException:
            break
driver.close()