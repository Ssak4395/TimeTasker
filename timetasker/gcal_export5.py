from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, os

# get current directory
cwd = os.getcwd().replace('\\', '/')
cwd = cwd + '/chromedriver.exe'
cwd = os.path.normpath(cwd)

# gmail stuff + ics url
USERNAME = "elsalee841020@gmail.com"
PASSWORD = "JoKeR520Peace"
ics_snatch = "C:/Users/Jasmine/Downloads/timetable.ics"

# this was supposed to prevent chrome from opening a window, but didnt work
chrome_options = Options()
chrome_options.add_argument("--headless")

# ATTENTION  |   ASDFWEZDTRAGERSERTAGERDZRAFEDFHAERSDXZRFESDZXGAVREDZXFFRDFXZCGDFZGADFZX
# if youre getting some sort of error on this line of code, replace the directory of the chromedriver with the current file where you extracted the zip

# gets current file path
direct_path = os.path.dirname(os.path.abspath(__file__))
if direct_path is not None:
	print('found current file path:')
else:
	print('did not find current path')
direct_path = direct_path+'\\chromedriver.exe'
# print('direct_path new: ', direct_path)
driver = webdriver.Chrome(direct_path)

driver.get("https://accounts.google.com/signin/v2/identifier?service=cl&passive=1209600&osid=1&continue=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Fr%2Fsettings%2Faddbyurl&followup=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Fr%2Fsettings%2Faddbyurl&scc=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

# insert username, i hate 2 page login    
username_field = driver.find_element_by_name("identifier")
username_field.send_keys(USERNAME)
username_field.send_keys(Keys.RETURN)

# wait for password field to generate
driver.implicitly_wait(2)

# insert password
password_field = driver.find_element_by_name("password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.RETURN)

# wait in order to load page
time.sleep(1)

# put in the ics url for gcal to process
url_field = driver.find_element_by_class_name("WpDZC.zHQkBf")
url_field.send_keys(ics_snatch)

# waiting for loading
driver.implicitly_wait(1)
time.sleep(1)

# press set to public view
public_click = driver.find_element_by_class_name("uVccjd.OQWBod")
public_click.click()

# confirm upload
confirm_click = driver.find_element_by_class_name("uArJ5e.UQuaGc.Y5sE8d.WFMp5")
confirm_click.click();

