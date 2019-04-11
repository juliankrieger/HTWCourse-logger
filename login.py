from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://moodle.htwsaar.de/auth/shibboleth/index.php")
user_field = driver.find_element_by_id("username")
pw_field = driver.find_element_by_id("password")

user_field.send_keys("jkrieger")
pw_field.send_keys("azpf7zm9f!")
button = driver.find_element_by_tag_name("button")
button.click()

accept_button = driver.find_element_by_name("_eventId_proceed")

accept_button.click()

driver.get("https://moodle.htwsaar.de/course/view.php?id=123");

notice = driver.get_element_by_id("notice")
if not notice:
    print("Something changed. Log into course now?")
    return

if not "Dieser" in notice.getText():
    print("Something changed. Log into course now?")
    return

print(driver.page_source)
