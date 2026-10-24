from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options = options)
driver.get("https://www.amazon.com.tr")
time.sleep(2)

arama_kutusu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
arama_kutusu.send_keys("iphone 17 pro max" + Keys.ENTER)
time.sleep(2)

ilk_urun = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "div[data-component-type='s-search-result']")))
urun_ismi = ilk_urun.find_element(By.CSS_SELECTOR, "h2 span").text
fiyat_ana = ilk_urun.find_element(By.CLASS_NAME, "a-price-whole").text
fiyat_kusurat = ilk_urun.find_element(By.CLASS_NAME, "a-price-fraction").text
fiyat = f"{fiyat_ana},{fiyat_kusurat} TL"

print(urun_ismi)
print(fiyat_ana)

time.sleep(3)

input("Input: ")
driver.quit()