from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

email=input('enter your linkedIn EmailID: ')
password=input('Enter your linkedIn password: ')

custom_message = "Hi, I'm a software engineering student who admires your work. I'd love to connect and would truly appreciate any guidance or referral you could offer. Thank you!"

df=pd.read_excel('linkedin_profiles1.xlsx')
status_list=[]

driver=webdriver.Chrome()

wait=WebDriverWait(driver,10)

driver.get('https://www.linkedin.com/login')
time.sleep(3)

driver.find_element(By.ID,'username').send_keys(email)
driver.find_element(By.ID,'password').send_keys(password)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

for url in df['LinkedIn_URL']:
    try:
        driver.get(url)
        time.sleep(5)

        connect_button = driver.find_element(By.XPATH, "//span[text()='Connect']/ancestor::button")
        driver.execute_script("arguments[0].scrollIntoView(true);",connect_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();",connect_button)

        add_note_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Add a note']"))
        )
        driver.execute_script("arguments[0].click();", add_note_button)

       
        note_textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@name='message']"))
        )
        note_textarea.send_keys(custom_message)

        
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Send']"))
        )
        time.sleep(2)
        driver.execute_script("arguments[0].click();", send_button)
        status_list.append('Request send')
        print(f'{url} send')

    except Exception as e:
        status_list.append("Failed or Already Connected")
        print(f"{url} Failed or Already Connected")

    time.sleep(5)

df['status']=status_list

df.to_excel('connection_result.xlsx',index=False)

print('done ')

driver.quit()