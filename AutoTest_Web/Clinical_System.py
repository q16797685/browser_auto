#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-xx-xx

@author: Wangchenyang

@功能：进入临床系统操作
"""

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import commonWebdriver


def choose_patient():
    """ 选择当日门诊用户 """
    find_query = commonWebdriver.browser.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/div/section/form/div[2]/div/input[1]")
    find_query.send_keys(u'王晨阳')
    sleep(2)
    click_query = commonWebdriver.browser.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/div/section/form/div[2]/div/button[1]")
    click_query.click()
    sleep(2)


def double_click_patient():
    """ 双击患者列表，进入主动病历 """
    find_patient = commonWebdriver.browser.find_element_by_xpath(
        '/html/body/div[2]/div[2]/div/div/section/div/table/tbody/tr[1]/td[2]')
    ActionChains(commonWebdriver.browser).double_click(find_patient).perform()
    sleep(2)