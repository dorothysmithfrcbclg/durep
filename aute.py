from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--disable-web-security')

driver = webdriver.Chrome(options=chrome_options)
