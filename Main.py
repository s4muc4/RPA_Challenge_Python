from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

site = 'http://www.rpachallenge.com/'

file = 'challenge.xlsx'

dt_registros = pd.read_excel(file) 

print(dt_registros)
print(dt_registros.info())

driver = webdriver.Chrome(executable_path=r"C:\Users\samuc\Documents\Python\chromedriver.exe")
driver.get(site)

btn_start = driver.find_element_by_xpath("//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']")
btn_start.click()

for i, r in dt_registros.iterrows():
    first_name = r['First Name']
    last_name = r['Last Name']
    company_name = r['Company Name']
    role_in_company = r['Role in Company']
    address = r['Address']
    email = r['Email']
    phone_number = r['Phone Number']

    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelFirstName']")
    textbox.clear()
    textbox.send_keys(first_name)

    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelLastName']")
    textbox.clear()
    textbox.send_keys(last_name)

    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelCompanyName']")
    textbox.clear()
    textbox.send_keys(company_name)

    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelRole']")
    textbox.clear()
    textbox.send_keys(role_in_company)

    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelAddress']")
    textbox.clear()
    textbox.send_keys(address)

    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelEmail']")
    textbox.clear()
    textbox.send_keys(email)

    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelPhone']")
    textbox.clear()
    textbox.send_keys(phone_number)

    botao_submit = driver.find_element_by_xpath("//input[@value='Submit']")
    botao_submit.click()