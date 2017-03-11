#!/usr/bin/env python
# encoding:utf-8
import unittest
import time
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
import re


class login(unittest.TestCase):
    def setUp(self):   #用于设置初始化的部分,这里将浏览器的调用和URL的访问放到初始化部分
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://172.15.105.71"
        self.verificationErrors = []   #脚本运行时，错误的信息将被打印到这个列表中
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_open_and_search(self):
        driver = self.driver
        driver.get(self.base_url + "/secure/login")
        time.sleep(3)
        driver.find_element_by_class_name("input-text").clear()
        driver.find_element_by_class_name("input-text").send_keys("13987654321")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("subbt").click()
        time.sleep(3)
        driver.get(self.base_url + "/invest/list")
        #driver.find_element_by_xpath("//tr[6]/td[6]").click()
        driver.find_element_by_xpath("//*[@id=\"txtClickHref\"]").click()
        driver.find_element_by_css_selector("td.td6 a")
        print driver.window_handles
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_css_selector("#investAmt").clear()
        driver.find_element_by_css_selector("#investAmt").send_keys("100")
        time.sleep(5)
        driver.find_element_by_class_name("btn-invest").click()
        print driver.window_handles
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        # driver.find_element_by_css_selector("a[class][id][href][onclick]").click()
        driver.find_element_by_xpath("//*[@id=\"btnJoin\"]").click()
        time.sleep(5)
        #添加检查点
        url.value = r"https://172.15.105.71/invest/success"
        time.sleep(2)
        if driver.find_current_url == url.value
            print "投资成功"
        else:
            print "投资不成功"




        """为什会弹出另外一个窗口打开投资页面"""

if __name__ == "__main__":
    unittest.main()