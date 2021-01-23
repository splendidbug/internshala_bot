# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:28:11 2021

@author: Lenovo
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re
import beepy as beep
import requests
import clx.xms
import requests
import selenium.webdriver.support.ui as ui

driver = webdriver.Chrome(executable_path = r"C:\Users\Lenovo\Desktop\chromedriver.exe")

driver.get('https://internshala.com/')

sleep(5)
loginbutton = driver.find_element_by_xpath("/html/body/div[1]/div[17]/div/nav/div[3]/ul/li[4]/button")#the complete xpath of the element
loginbutton.click()

#if(EC.presence_of_element_located((By.TAG_NAME, 'body'))):


sleep(5)

emailid = driver.find_element_by_xpath("/html/body/div[1]/div[15]/div/div/div[2]/form/div[1]/input")#the complete xpath of the element
emailid.send_keys('shreyasanother@gmail.com')#the get function gets the string in the entry object

clickpassword = driver.find_element_by_xpath("/html/body/div[1]/div[15]/div/div/div[2]/form/div[2]/input")
clickpassword.send_keys('lamboisnotthebest')

loginbutton2 = driver.find_element_by_xpath("/html/body/div[1]/div[15]/div/div/div[2]/form/div[4]/button")#the complete xpath of the element
loginbutton2.click()

sleep(20)

driver.get('https://internshala.com/internships/data%20science-internship')   

sleep(5)


#company_name1 =  driver.find_element_by_xpath("/html/body/div[1]/div[18]/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]").text
#position_name1 = driver.find_element_by_xpath("/html/body/div[1]/div[18]/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[2]").text


def send_sms(company_name, position_name):
    client = clx.xms.Client(service_plan_id='', token='')
    
    create = clx.xms.api.MtBatchTextSmsCreate()
    create.sender = ''
    create.recipients = {''}
    create.body = "Bro there's a new internship.\nCompany name: " + company_name + "\nPosition_name: " + position_name + "\n:)"
    
    try:
      batch = client.create_batch(create)
    except (requests.exceptions.RequestException,
      clx.xms.exceptions.ApiException) as ex:
      print('Failed to communicate with XMS: %s' % str(ex))

count=0;


while(True):
    sleep(10)
    company_name =  driver.find_element_by_xpath("/html/body/div[1]/div[18]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]/a").text
    position_name = driver.find_element_by_xpath("/html/body/div[1]/div[18]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[1]").text

    if((company_name != 'Stodict' or position_name != 'Equity Research Analysis')):
        
        open_application = driver.find_element_by_xpath('/html/body/div[1]/div[18]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[1]/a')
        open_application.click()
      
        """
        apply_now = driver.find_element_by_link_text("Apply now")
        apply_now.click()
        proceed_to_application = driver.find_element_by_xpath('/html/body/div[1]/div[17]/div/div/div/div[1]/div[2]/button')
        proceed_to_application.click()
    """
        send_sms(company_name=company_name, position_name=position_name)       
        for i in range(1,4): 
            beep.beep(3)
        sleep(0.7)
        for i in range(1,4): 
            beep.beep(3)
        sleep(0.7)
        for i in range(1,4): 
            beep.beep(3)
#        why_should_i_hire_u = driver.find_element_by_name('cover_letter')
#        why_should_i_hire_u.clear()
#        why_should_i_hire_u.send_keys('')
        #time_period = driver.find_element_by_xpath('/html/body/div[1]/div[17]/div/div/div/div[2]/form/div/div[2]/div[2]/div[1]/label').text
#        time_period = driver.find_element_by_link_text('available').text
#        print(time_period)
#        time_period = int(re.search(r'\d+', time_period).group())
#        time_text_area = driver.find_element_by_name('text_1845216')
#        time_text_area.clear() 
#        time_text_area.send_keys('Yes, I am available for ' + str(time_period) + ' months, starting immediately.')
 
#        submit = driver.find_element_by_name("submit")
#        submit.click()

#        field_is_required_text = driver.find_element_by_xpath("/html/body/div[1]/div[17]/div/div/div/div[2]/form/div/div[2]/div[3]/label").text        

        wait = ui.WebDriverWait(driver, 10000) # timeout after 1000 seconds
        wait.until(lambda driver: driver.find_elements_by_link_text('Go to internship search'))
        driver.get('https://internshala.com/internships/data%20science-internship')
        sleep(5)
    else:
        count+=1
        print(count)
        sleep(120)
        driver.get('https://internshala.com/internships/data%20science-internship')
        

