import selenium
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Firefox(executable_path=r'C:\Users\Lena\Desktop\geckodriver.exe')
driver.get("https://www.datafolks.com")

home = driver.find_element_by_xpath("//div[@data-elem-id=1551634462374]/a")
assert home.text == "Home"

portfolio = driver.find_element_by_xpath("//div[@data-elem-id=1551634481382]/a")
assert portfolio.text == "Portfolio"

services = driver.find_element_by_xpath("//div[@data-elem-id=1551634484712]/a")
assert services.text == "Services"

contact_us = driver.find_element_by_xpath("//div[@data-elem-id=1551634487768]/a")
assert contact_us.text == "Contact Us"

driver.quit()
