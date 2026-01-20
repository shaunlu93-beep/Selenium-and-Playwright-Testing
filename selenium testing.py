from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

# Setup
options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--user-data-dir=C:\\Users\\Drmilk\\AppData\\Local\\Google\\Chrome\\User Data") # Path to your chrome profile
options.add_argument('--profile-directory=Profile 11') # Profile name
options.headless = False
PATH = (r"C:/Users/Drmilk/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
service_for_driver = Service(executable_path=PATH) 
driver = webdriver.Chrome()# service=service_for_driver, options=options)
def Tab(name):
    driver.find_element(By.NAME, name).send_keys(webdriver.Keys.TAB)

# Time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"Current time in Asia/Taipei timezone: {current_time}")

# Open Google
repeat_times = input("Repeat For How Many Times?")
for i in range(int(repeat_times)):
    driver.get("https://accounts.google.com/ServiceLogin?hl=zh-TW&passive=true&continue=https://www.google.com/&ec=futura_exp_og_so_72776762_e")
    driver.maximize_window()
    driver.find_element(By.NAME, 'identifier').send_keys("pajh113031@pajh.hcc.edu.tw", webdriver.Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'Passwd')))
    driver.find_element(By.NAME, 'Passwd').send_keys("F133156219", webdriver.Keys.ENTER)
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeKA5va7ez55lqpC8kMgy01V3F8tkqoATrDhTIfsTe8KH6jkQ/viewform")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Hello")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("World!")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("123")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div').click()
    

print(f"Successfully sent {repeat_times} time(s) at {current_time}")