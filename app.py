from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import config


options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=options)
chrome.get("https://www.facebook.com/")

email = chrome.find_element_by_id("email")
password = chrome.find_element_by_id("pass")

email.send_keys(config.email)
password.send_keys(config.password)
password.submit()

time.sleep(3)
chrome.get('https://www.facebook.com/learncodewithmike')

for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)

soup = BeautifulSoup(chrome.page_source, 'html.parser')

titles = soup.find_all('span', {
    'class': 'a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7'})

for title in titles:
    print(title.getText())

chrome.quit()
