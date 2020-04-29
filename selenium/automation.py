from selenium import webdriver
import time

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')

user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)

user_message.clear()
user_message.send_keys("I'm extra COOOOOL")
time.sleep(3)
show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')

assert "I'm extra COOOOOL" in output_message.text

print(output_message.get_attribute('innerHTML'))

chrome_browser.quit()
# chrome_browser.close()
