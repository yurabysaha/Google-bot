import random
import time
from selenium import webdriver
import xml.etree.ElementTree as ET
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import unittest

class QuoraTest(unittest.TestCase):

    def setUp(self):
        PROXYList = ["203.66.159.44:3128", "31.207.0.99:3128", "218.205.17.79:3128"]
        random.shuffle(PROXYList)
        PROXY = random.choice(PROXYList)

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
        tree = ET.parse('values.xml')
        lst = tree.findall('links/link')
        for item in lst:
            browserlink = item.find('mylink').text
            #driver.get(browserlink)
            removebuttonXpath = "//a[@class='remove br3']"
            signinbuttonXpath = "//div[@class='header_signin_with_search_bar action_button']"
            signinlinkXpath = "//a[text() = 'Sign In']"
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
                time.sleep(10)
                driver.get(browserlink)
                signinbutttonElement = driver.find_element_by_xpath(signinbuttonXpath)
                signinbutttonElement.click()
                time.sleep(5)
                try:
                    signinlinkElement = driver.find_element_by_xpath(signinlinkXpath)
                    signinlinkElement.click()
                except:

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
                    time.sleep(7)
                    topmenuElement = driver.find_element_by_xpath(topmenuXpath)
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
                    seconds_list = [300, 600, 900, 1200]
                    random.shuffle(seconds_list)
                    seconds = random.choice(seconds_list)
                    time.sleep(seconds)
                    topmenuElement.click()
                    time.sleep(2)
                    logoutElement = driver.find_element_by_xpath(logoutXpath)
                    logoutElement.click()
                    time.sleep(3)
                    removebuttonElement = driver.find_element_by_xpath(removebuttonXpath)
                    removebuttonElement.click()
                    time.sleep(6)



                    #tree = ET.parse('values.xml')
                    #lst = tree.findall('links/link')
                    #for item in lst:
                     #   browserlink = item.find('mylink').text
                      #  driver.get(browserlink)





    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
