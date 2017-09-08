#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-xx-xx

@author: Wangchenyang

@功能：精神检查编辑
"""

from time import sleep
import commonWebdriver


def mind_check_edit():
    """ 进入患者精神检查 """
    find_mind_check = commonWebdriver.browser.find_element_by_xpath(
        '//*[@id="caseHistoryTitle"]/span[3]')      # 左侧精神检查标签
    find_mind_check.click()
    commonWebdriver.browser.switch_to.frame('ui-tinymce-1_ifr')     # 找到iframe元素
    sleep(2)
    find_iframe = commonWebdriver.browser.find_element_by_id('tinymce')
    find_iframe.send_keys('test')
    sleep(2)
    commonWebdriver.browser.switch_to_default_content()     # 跳出所有frame
    sleep(2)
    find_active_case_history = commonWebdriver.browser.find_element_by_xpath(
        '//*[@id="caseHistoryTitle"]/span[1]')
    find_active_case_history.click()
    sleep(5)
    commonWebdriver.browser.quit()
