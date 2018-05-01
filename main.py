
# -*- coding: utf-8 -*-
import unittest
import time

from selenium import webdriver
from HTMLTestRunner import  HTMLTestRunner

from case.c_login import LoginTest as LT

class RHCase(unittest.TestCase):
    def setUp(self):
        print ">>>>>>start"

    def test_login_success(self):
        LT().login_success()

    def tearDown(self):
        print "----------->test end"



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(RHCase("test_loginsuccess"))
    with open('HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='RHCIMS Test Report',
                                description='Automation Test',
                                verbosity=1
                                )
        runner.run(suite)


