#!/usr/bin/env python
# encoding:utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class logintest71(unittest.TestCase):
    def setUp(self):   #用于设置初始化的部分,这里将浏览器的调用和URL的访问放到初始化部分
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://172.15.105.71/secure/login"
        self.verificationErrors = []   #脚本运行时，错误的信息将被打印到这个列表中
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_open_and_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(3)
        driver.find_element_by_class_name("input-text").clear()
        driver.find_element_by_class_name("input-text").send_keys("13987654321")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("subbt").click()
        time.sleep(3)
        driver.close()

if __name__ == "__main__":
    unittest.main()