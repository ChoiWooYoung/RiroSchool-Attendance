from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\Python\chromedriver.exe')
driver.get("https://학교.riroschool.kr/user.php")
driver.find_element_by_xpath('//*[@id="userId"]').send_keys('ID')
driver.find_element_by_xpath('//*[@id="userPass"]').send_keys('PW')
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/form/div/div[5]/a").click()      //Login Button
driver.get("해당 출석 URL 입력")
time.sleep(1)                             //Radio Button 입력 씹힘을 방지한 Delay 1초
driver.find_element_by_xpath("체크해야할 Radio Button의 XPath").click()
driver.find_element_by_xpath("출석 Button 의 Xpath").click()


