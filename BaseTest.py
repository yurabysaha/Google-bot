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
ROOT_PATH=os.getcwd()

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

        chrome = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

        browserlink = 'https://facebook.com'
        chrome.get(browserlink)
        self.driver = chrome

    def test_login(self):
        driver = self.driver

        tree = ET.parse(ROOT_PATH + '/text.xml')

        text = tree.find('text').text
        picture = ET.parse('pictureLink.xml').find('link').text
        emailXpath = "//*[@id='email']"
        passXpath = "//*[@id='pass']"
        loginBtnXpath = "//*[@id='u_0_o']"
        textArea = "_4h98"
        btn = "_332r"
        treeuser = ET.parse(ROOT_PATH + '/user.xml')

        time.sleep(2)
        emailvalue = treeuser.find('email').text
        passvalue = treeuser.find('password').text
        time.sleep(2)
        driver.find_element_by_xpath(emailXpath).send_keys(emailvalue)
        time.sleep(1)
        driver.find_element_by_xpath(passXpath).send_keys(passvalue)
        time.sleep(1)
        driver.find_element_by_xpath(loginBtnXpath).click()
        time.sleep(2)

        tree22 = ET.parse(ROOT_PATH + '/groupLink.xml')
        lstgroup = tree22.findall('glink')
        not_posted = 0
        posted = 0
        for i in lstgroup:

            try:
                grouplinks = i.text
                driver.get(grouplinks)
                time.sleep(2)
                textArea1 = driver.find_element_by_class_name(textArea)
                time.sleep(2)
                textArea1.send_keys(picture)
                time.sleep(10)
                picture = driver.find_element_by_class_name("_5rpu")
                time.sleep(1)
                picture.send_keys(Keys.CONTROL + 'a')
                time.sleep(1)
                picture.send_keys(Keys.BACKSPACE)
                # picture.send_keys("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
                time.sleep(2)
                picture.send_keys(text)
                time.sleep(5)
                postBtn = driver.find_element_by_class_name(btn)
                time.sleep(5)
                postBtn.click()
                time.sleep(10)
                posted = posted + 1

            except:
                doc = ET.parse(ROOT_PATH + '/link.xml')
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
