import time
from selenium import webdriver
import xml.etree.ElementTree as ET
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import unittest

class FirefoxQuoraTest(unittest.TestCase):

    def setUp(self):


        tree = ET.parse('values.xml')
        lst = tree.findall('links/link')
        for item in lst:
            browserlink = item.find('mylink').text




    def test_login(self):
        d = webdriver.Remote(desired_capabilities={'browserName': 'safari'})

        d.get("www.google.com")
        signinbuttonXpath = "//div[@class='header_signin_with_search_bar action_button']"
        loginlinkXpath = "//a[text() = 'I Have a Quora Account']"
        loginFieldXpath = "//form/div[1]/div[1]/input"
        passworFieldXpath = "//form/div[1]/div[2]/input"
        loginbuttonXpath = "//input[@value='Login']"
        tree = ET.parse('values.xml')
        root = tree.getroot()
        lst = tree.findall('users/user')

        for item in lst:

            time.sleep(2)
            signinbutttonElement = d.find_element_by_xpath(signinbuttonXpath)
            signinbutttonElement.click()
            time.sleep(5)
            loginlinkElement = d.find_element_by_xpath(loginlinkXpath)
            loginlinkElement.click()
            time.sleep(2)
            emailvalue = item.find('email').text
            loginFieldElement = d.find_element_by_xpath(loginFieldXpath)
            time.sleep(5)
            loginFieldElement.click()
            loginFieldElement.clear()
            loginFieldElement.send_keys(emailvalue)
            passvalue = item.find('password').text
            passwordFieldElement = d.find_element_by_xpath(passworFieldXpath)
            passwordFieldElement.clear()
            passwordFieldElement.send_keys(passvalue)
            loginbuttonElement = d.find_element_by_xpath(loginbuttonXpath)
            time.sleep(20)
            loginbuttonElement.click()
            time.sleep(10)

