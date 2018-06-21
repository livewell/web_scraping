from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import os


dirname = os.path.dirname(os.path.abspath(__file__))
chrome_driver_location = dirname + '/lib/chromedriver'

# Create a Chrome Browser in Incognito
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

print chrome_driver_location

browser = webdriver.Chrome(executable_path=chrome_driver_location, chrome_options=option)


browser.get("https://github.com/livewell")

assert "Github" in browser.title


browser.close()
