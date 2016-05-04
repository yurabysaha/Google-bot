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
        topmenuXpath = "//span[@class='user']"
        logoutXpath = "//a[text() = 'Logout']"

        tree = ET.parse('values.xml')
        root = tree.getroot()
        lst = tree.findall('users/user')

        for item in lst:

            time.sleep(2)
            signinbutttonElement = driver.find_element_by_xpath(signinbuttonXpath)
            signinbutttonElement.click()
            time.sleep(5)
            loginlinkElement = driver.find_element_by_xpath(loginlinkXpath)
            loginlinkElement.click()
            time.sleep(2)
            emailvalue = item.find('email').text
            loginFieldElement = driver.find_element_by_xpath(loginFieldXpath)
            time.sleep(5)
            loginFieldElement.click()
            loginFieldElement.clear()
            loginFieldElement.send_keys(emailvalue)
            passvalue = item.find('password').text
            passwordFieldElement = driver.find_element_by_xpath(passworFieldXpath)
            passwordFieldElement.clear()
            passwordFieldElement.send_keys(passvalue)
            time.sleep(2)
            allowPasswordLessElement = driver.find_element_by_xpath(allowPasswordLessXpath)
            allowPasswordLessElement.click()
            loginbuttonElement = driver.find_element_by_xpath(loginbuttonXpath)
            time.sleep(5)
            loginbuttonElement.click()
            time.sleep(7)
            try:
                upvoteElement = driver.find_element_by_xpath(upvoteXpath)
                upvoteElement.click()
            except:
                driver.execute_script("window.scrollTo(0, 500)")
                upvoteElement.click()
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
