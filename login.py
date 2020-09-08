from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

#opens my school's website to login 
driver.get("https://shib.idm.umd.edu/shibboleth-idp/profile/SAML2/Redirect/SSO?execution=e1s1")

#look for the login button
login_button = driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]')
#click on the login button
login_button.click()

#allow some time for the page to load before moving on
sleep(1)

#For privacy reasons I have not included my username and password, customize them with your own if you use this program to make life a little easier!

#looks for the space to enter my Directory ID which is the username
username = driver.find_element_by_xpath('//*[@id="Directory ID"]')
username.send_keys(" ")

#looks for the password field
password = driver.find_element_by_xpath('//*[@id="password"]')

password.send_keys(" ")

#click on submit button
driver.find_element_by_xpath('//*[@id="submit-button"]').click()
