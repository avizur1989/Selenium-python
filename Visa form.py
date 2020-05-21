from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver =webdriver.Chrome(executable_path="C:\\Users\\shany\\Selenium\\chromedriver.exe")
driver.get("https://www.visa-vietnam.co.il/")
driver.find_element_by_xpath('//*[@id="details-button"]').click()
driver.find_element_by_xpath('//*[@id="proceed-link"]').click()

driver.find_element_by_xpath("/html/body/div[2]/div/div/section[1]/div[2]/div/div/div/div/div[5]/div/div/a/span").click()
driver.implicitly_wait(500)

date1 = driver.find_element_by_xpath('//*[@id="input_8_21"]')
date1.click()
date1.send_keys("20/05/2020")
driver.find_element_by_xpath('//*[@id="input_8_20"]/option[2]').click()
# driver.find_element_by_xpath('//*[@id="input_8_43"]/option[3]').click()
driver.find_element_by_name('input_41').send_keys("Avi")
driver.find_element_by_name('input_30').send_keys("zur")
driver.find_element_by_name('input_40').send_keys("Avi@zur.com")
driver.find_element_by_name('input_40_2').send_keys("Avi@zur.com")
radio = driver.find_element_by_id('choice_8_15_1')
driver.execute_script("arguments[0].click();", radio)
driver.implicitly_wait(500)
date2 = driver.find_element_by_id('input_8_16')
date2.click()
date2.clear()
date2.send_keys("07/01/1992")
nation= driver.find_element_by_xpath('//*[@id="input_8_5"]')
nation.click()
nation=driver.find_element_by_xpath('//*[@id="input_8_5"]/option[12]').click()
driver.find_element_by_id('input_8_17').send_keys("1234567")

check = driver.find_element_by_id('choice_8_83_1')
driver.execute_script("arguments[0].click();", check)



driver.save_screenshot('avqwqwqwi.png')
button = driver.find_element_by_id('gform_submit_button_8')
driver.execute_script("arguments[0].click();", button)

time.sleep(2)
driver.save_screenshot('blabla.png')







time.sleep(5)
driver.close()
