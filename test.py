from selenium import webdriver
import time

def fill_form(driver):
  button_0 = '//*[@id="Field12_1"]'
  button_1 = '//*[@id="Field3_1"]'
  button_2 = '//*[@id="Field5_1"]'
  submit_button = '//*[@id="saveForm"]'
  driver.find_element_by_xpath(button_0).click()
  driver.find_element_by_xpath(button_1).click()
  driver.find_element_by_xpath(button_2).click()
  driver.find_element_by_xpath(submit_button).click()

def login(driver):
  login_button = '//*[@id="formwrapper"]/div[4]/input'
  driver.find_element_by_xpath(login_button).click()

chromedriver_location = "chromedriver.exe"
path = "user-data-dir=C:/Users/Jonathan/AppData/Local/Google/Chrome/User Data"
opts = webdriver.ChromeOptions()
opts.add_argument('--no-sandbox')
opts.add_argument('--headless')
opts.add_argument(path)
driver = webdriver.Chrome(options=opts)
driver.get("https://daily-student.cmu.edu/")

text = 'Thank you for completing the Self-Assessment today.'
timeout = time.time() + 60*2
timed_out = False
while((text in driver.page_source) == False):
  if(time.time() > timeout):
    print("failure")
    timed_out = True
    break
  print(driver.title)
  if(driver.title == "Student Daily Self-Assessment - COVID-19 Updates - Carnegie Mellon University"):
    fill_form(driver)
  elif(driver.title == "login.cmu.edu"):
    login(driver)

if(timed_out):
  print("failure")
else:
  print("success")
