#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-xx-xx

@author: Wangchenyang

@功能：测试类
"""

import openUrl
import Clinical_System
# import medical_history
# import doctor_orders
import diagnosis


class Testclass(object):
    @classmethod
    def testcase(self):
        openUrl.open_url()
        Clinical_System.choose_patient()
        Clinical_System.double_click_patient()
        # medical_history.medical_history_edit()
        diagnosis.emr_diagnosis()


if __name__ == '__main__':
    Test = Testclass()
    Test.testcase()
