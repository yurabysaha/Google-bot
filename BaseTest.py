import os
import random
import time
from selenium import webdriver
import xml.etree.ElementTree as ET

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import unittest
from xml.etree import ElementTree
from xml.dom import minidom

def xmlpath():
    if os.uname()[0] == "Linux":
        return '/'
    else:
        return '\\'

ROOT_PATH=os.getcwd() + xmlpath()


def osw():
    if os.uname()[0] == "Linux":
        return ROOT_PATH + 'chromedriver'
    else:
        return ROOT_PATH + 'chromedriver.exe'

class RobotTest(unittest.TestCase):
    def setUp(self):
        # PROXYList = ["203.66.159.44:3128", "31.207.0.99:3128", "219.255.197.90:3128", "64.103.27.184:8080", "209.242.141.60:8080", "122.226.166.231:8080"]
        # random.shuffle(PROXYList)
        # PROXY = random.choice(PROXYList)
        # chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument('--lang=en')
        chrome = webdriver.Chrome(osw(), chrome_options=chrome_options)
        browserlink = 'https://plus.google.com'
        chrome.get(browserlink)

        self.driver = chrome

    def test_login(self):
        driver = self.driver

        tree = ET.parse(ROOT_PATH + 'text.xml')

        text = tree.find('text').text
        picture = ET.parse(ROOT_PATH + 'pictureLink.xml').find('link').text
        emailXpath = "//*[@id='Email']"
        passXpath = "//*[@id='Passwd']"
        signinBtn = "//*[@id='gb_70']"
        loginBtnXpath = "//*[@id='signIn']"
        textArea = "XPxXbf"
        btn = ".iHCNId>div:last-child"
        treeuser = ET.parse(ROOT_PATH + 'user.xml')


        driver.find_element_by_xpath(signinBtn).click()
        time.sleep(2)
        emailvalue = treeuser.find('email').text
        time.sleep(2)
        driver.find_element_by_xpath(emailXpath).send_keys(emailvalue)
        time.sleep(1)
        nextBtn = "//*[@id='next']"
        driver.find_element_by_xpath(nextBtn).click()
        time.sleep(2)
        passvalue = treeuser.find('password').text
        driver.find_element_by_xpath(passXpath).send_keys(passvalue)
        driver.find_element_by_xpath(loginBtnXpath).click()
        time.sleep(2)
        try:
            newDesign = driver.find_element_by_class_name("GWQXxc")
            newDesign.click()

        except:
            pass

        tree22 = ET.parse(ROOT_PATH + 'groupLink.xml')
        lstgroup = tree22.findall('glink')
        not_posted = 0
        posted = 0
        for i in lstgroup:

            try:
                grouplinks = i.text
                driver.get(grouplinks)
                time.sleep(8)
                addBtn = driver.find_element_by_css_selector(".jXDCJf.Tek5Ce.BDrJf")
                addBtn.click()
                time.sleep(2)
                textArea1 = driver.find_element_by_id(textArea)
                time.sleep(2)
                textArea1.send_keys(text)
                time.sleep(2)
                picBtn = driver.find_element_by_css_selector(".XjCfXd>div:first-child>div:first-child")
                picBtn.click()
                time.sleep(2)
                picture = driver.find_element_by_css_selector(".uNI4p>div>input")
                time.sleep(2)
                picture.send_keys("/home/lego/Pictures/ruby-rails.jpg")
                time.sleep(5)
                postBtn = driver.find_element_by_css_selector(btn)
                time.sleep(5)
                postBtn.click()
                time.sleep(10)
                posted = posted + 1

            except:
                doc = ET.parse(ROOT_PATH + 'link.xml')
                root = doc.getroot()
                new = ET.Element('glink')
                new.text = grouplinks
                root.append(new)
                doc.write(ROOT_PATH + 'link.xml', encoding="utf-8", xml_declaration=True)
                not_posted = not_posted +1
                continue

        text_file = open(ROOT_PATH + "Statistic.txt", "w")
        fuck = ["Not Posted in : %s " % not_posted + "\n", "Posted in : %s" % posted]
        text_file.writelines(fuck)
        text_file.close()

        driver.close()

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(RobotTest))
    return test_suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
