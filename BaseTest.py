import time
from selenium import webdriver
import xml.etree.ElementTree as ET
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import unittest

class QuoraTest(unittest.TestCase):

    def setUp(self):
        PROXY = "103.44.26.163:3128"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

        chrome = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)

        tree = ET.parse('values.xml')
        lst = tree.findall('links/link')
        for item in lst:
            browserlink = item.find('mylink').text
            chrome.get(browserlink)
            self.driver = chrome


    def test_login(self):
        driver = self.driver
        signinbuttonXpath = "//div[@class='header_signin_with_search_bar action_button']"
        loginlinkXpath = "//a[text() = 'I Have a Quora Account']"
        loginFieldXpath = "//form/div[1]/div[1]/input"
        passworFieldXpath = "//form/div[1]/div[2]/input"
        loginbuttonXpath = "//input[@value='Login']"
        allowPasswordLessXpath = "//input[@name='allow_passwordless']"
        upvoteXpath = "//span[text() = 'Upvote']"
        upvotedXpath = "//span[text() = 'Upvoted']"
        topmenuXpath = "//span[@class='user']"
        logoutXpath = "//a[text() = 'Logout']"
        continueWithEmailXpath = "//a[text() = 'Login As Another User']"
        loginfieldasanotherXpath = "//input[@placeholder='Email']"
        passwordfieldasanotherXpath = "//input[@placeholder='Password']"
        remembermecheckboxXpath = "//input[@name='allow_passwordless']"
        loginasanotheButtonXpath = "//input[@value='Login']"
        tree = ET.parse('values.xml')
        root = tree.getroot()
        lst = tree.findall('users/user')

        for item in lst:
            time.sleep(2)
            emailvalue = item.find('email').text
            passvalue = item.find('password').text
            time.sleep(5)
            try:
                signinbutttonElement = driver.find_element_by_xpath(signinbuttonXpath)
                signinbutttonElement.click()
                time.sleep(5)
                loginlinkElement = driver.find_element_by_xpath(loginlinkXpath)
                loginlinkElement.click()
                time.sleep(2)
                loginFieldElement = driver.find_element_by_xpath(loginFieldXpath)
                time.sleep(5)
                loginFieldElement.click()
                loginFieldElement.clear()
                loginFieldElement.send_keys(emailvalue)
                passwordFieldElement = driver.find_element_by_xpath(passworFieldXpath)
                passwordFieldElement.clear()
                passwordFieldElement.send_keys(passvalue)
                time.sleep(2)
                allowPasswordLessElement = driver.find_element_by_xpath(allowPasswordLessXpath)
                allowPasswordLessElement.click()
                loginbuttonElement = driver.find_element_by_xpath(loginbuttonXpath)
                time.sleep(5)
                loginbuttonElement.click()
            except:
                continueWithEmailElement = driver.find_element_by_xpath(continueWithEmailXpath)
                continueWithEmailElement.click()
                time.sleep(4)
                loginfieldasanotherElement = driver.find_element_by_xpath(loginfieldasanotherXpath)
                loginfieldasanotherElement.clear()
                loginfieldasanotherElement.send_keys(emailvalue)
                time.sleep(2)
                passwordfieldasanotherElement = driver.find_element_by_xpath(passwordfieldasanotherXpath)
                passwordfieldasanotherElement.clear()
                passwordfieldasanotherElement.send_keys(passvalue)
                time.sleep(2)
                remembermecheckboxElement = driver.find_element_by_xpath(remembermecheckboxXpath)
                remembermecheckboxElement.click()
                time.sleep(2)
                loginasanotheButtonElement = driver.find_element_by_xpath(loginasanotheButtonXpath)
                loginasanotheButtonElement.click()
            time.sleep(7)
            try:
                try:
                    upvoteElement = driver.find_element_by_xpath(upvoteXpath)
                    upvoteElement.click()
                except:
                    upvotedElement = driver.find_element_by_xpath(upvotedXpath)
                    upvotedElement.click()
            except:
                time.sleep(7)
                driver.execute_script("window.scrollTo(0, 500)")
                time.sleep(4)
                try:
                    upvoteElement = driver.find_element_by_xpath(upvoteXpath)
                    upvoteElement.click()
                except:
                    upvotedElement = driver.find_element_by_xpath(upvotedXpath)
                    upvotedElement.click()
            time.sleep(3)
            topmenuElement = driver.find_element_by_xpath(topmenuXpath)
            topmenuElement.click()
            time.sleep(2)
            logoutElement = driver.find_element_by_xpath(logoutXpath)
            logoutElement.click()
            time.sleep(3)





    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
