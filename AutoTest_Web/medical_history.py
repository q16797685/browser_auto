#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-xx-xx

@author: Wangchenyang

@功能：病史编辑
"""

from time import sleep
import commonWebdriver
import random

medical_history = [u'喜欢胡思乱想，与别人说话有点儿紧张。别人不按我说的做我很生气', u'睡不好人累头痛困疲惫做恶梦', u'晚上失眠，脑袋总是在想东西',
                u'不开心,往坏处想事,抗压力差', u'头晕头痛失眠喜欢胡思乱想', u'失眠', u'喜欢胡思乱想，与别人说话有点儿紧张。别人不按我说的做我很生气',
                u'失眠，晚上睡不着，偶尔耳边有声音']


def medical_history_edit():
    """ 进入患者主动病历页面 """
    commonWebdriver.browser.switch_to.frame('ui-tinymce-2_ifr')  # 找到iframe元素
    sleep(3)
    test = commonWebdriver.browser.find_element_by_id('tinymce')
    sleep(3)
    ran_medical_history = random.choice(medical_history)
    test.send_keys(ran_medical_history)
    sleep(3)
    commonWebdriver.browser.switch_to_default_content()
    find_mind_check = commonWebdriver.browser.find_element_by_xpath(
        '//*[@id="caseHistoryTitle"]/span[3]')
    find_mind_check.click()
