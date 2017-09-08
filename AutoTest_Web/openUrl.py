#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-xx-xx

@author: Wangchenyang

@功能：进入医生工作站
"""


from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import commonWebdriver


def open_url():
    """ 启动页面 """
    commonWebdriver.browser.get("http://172.17.200.94")
    commonWebdriver.browser.maximize_window()
    sleep(2)
    commonWebdriver.browser.find_element_by_id('username').send_keys('1153')    # 输入用户名
    sleep(2)
    commonWebdriver.browser.find_element_by_id('password').send_keys('1153')    # 输入密码
    sleep(2)
    commonWebdriver.browser.find_element_by_xpath('//*[@id="opStyle"]/div').click()     # 点击确认
    sleep(2)
    commonWebdriver.browser.find_element_by_xpath('/html/body/div[2]/div[3]/a[1]/div/span').click()  # 点击进入临床系统
    sleep(2)
    double_click = commonWebdriver.browser.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[1]/div[2]/label/span[contains(@ng-bind,'list.deptName') and contains(text(),'精神科门诊')]")  # 精神科门诊
    sleep(2)
    ActionChains(commonWebdriver.browser).double_click(double_click).perform()   # 双击进入科室
    sleep(2)