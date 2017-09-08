#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-xx-xx

@author: Wangchenyang

@功能：历史病历
"""

from time import sleep
import commonWebdriver
from selenium.webdriver.common.keys import Keys

def emr_diagnosis():
    sleep(3)
    find_diagnosis = commonWebdriver.browser.find_element_by_xpath(
        "//div/div[2]/div[2]/span[1][contains(@ng-click,'rightDiagnosisFun(2)')]")
    find_diagnosis.click()
    sleep(3)
    click_diagnosis_name = commonWebdriver.browser.find_element_by_xpath(
        'html/body/div[2]/div[2]/div/div[2]/div[7]/div/div[1]/div[3]/label/input')   # 点击备注
    click_diagnosis_name.send_keys('ceshi1')
    sleep(2)
    click_diagnosis_name.send_keys(Keys.ENTER)
    sleep(2)
