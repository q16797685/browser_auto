#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-xx-xx

@author: Wangchenyang

@功能：精神检查编辑
"""

from time import sleep
import commonWebdriver


def orders_sumbit():
    """ 进入患者精神检查 """
    find_orders = commonWebdriver.browser.find_element_by_xpath(
        '/html/body/div[2]/div[2]/div/div[2]/div[8]/div/h2/span[2]')      # 上侧医嘱标签
    find_orders.click()
    sleep(1)
    choose_medical = commonWebdriver.browser.find_element_by_xpath(".//*[@id='s2id_autogen17']/a")
    sleep(1)
    choose_medical.click()
    sleep(1)
    choose_medical.send_keys('wlf')
    sleep(2)
    insert_medical = commonWebdriver.browser.find_element_by_xpath("/html/body/div[7]/ul/li[1]/div[contains(@role,'option')]")
    insert_medical.click()
    sleep(2)
    sumbit_orders = commonWebdriver.browser.find_element_by_xpath("//button[contains(@ng-click,'saveToHis.save()')]")
    sumbit_orders.click()
    sleep(2)
