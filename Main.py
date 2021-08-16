# Import Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Defining Variables
site = 'http://www.rpachallenge.com/'
file = 'challenge.xlsx'
dt_registros = pd.read_excel(file) 

print("Tabela de registros:")
print(dt_registros)

# Open Google Chrome in URL RPA Challenge
print("Abrindo browser Google Chrome na URL do RPA Challenge")
driver = webdriver.Chrome(executable_path=r"C:\Users\samuc\Documents\Python\chromedriver.exe")
driver.get(site)

print("Iniciando preenchimento dos formulários")
# Click in Start
btn_start = driver.find_element_by_xpath("//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']")
btn_start.click()


for i, r in dt_registros.iterrows():
    # Saving data in variables
    first_name = r['First Name']
    last_name = r['Last Name']
    company_name = r['Company Name']
    role_in_company = r['Role in Company']
    address = r['Address']
    email = r['Email']
    phone_number = r['Phone Number']

    print('Round:', i)


    # Write First Name
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelFirstName']")
    textbox.clear()
    textbox.send_keys(first_name)

    # Write Last Name
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelLastName']")
    textbox.clear()
    textbox.send_keys(last_name)

    # Write Company Name
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelCompanyName']")
    textbox.clear()
    textbox.send_keys(company_name)

    # Write Role In Company
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelRole']")
    textbox.clear()
    textbox.send_keys(role_in_company)

    # Write Adress
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelAddress']")
    textbox.clear()
    textbox.send_keys(address)

    # Write Email
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelEmail']")
    textbox.clear()
    textbox.send_keys(email)

    # Write Phone Number
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelPhone']")
    textbox.clear()
    textbox.send_keys(phone_number)

    # Click in Submit
    botao_submit = driver.find_element_by_xpath("//input[@value='Submit']")
    botao_submit.click()

# Wait 20 seconds
time.sleep(20)

print("Fim do processo")

# Quit Browser
driver.close()
