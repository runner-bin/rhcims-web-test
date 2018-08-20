# coding:utf-8
from util.send_mail import SendMail
from util.create_suite import CreateSuite
import time
import os
from HTMLTestRunner import HTMLTestRunner
import unittest


def main():
    current_time = time.strftime("%Y")+u"年"+time.strftime("%m")+u"月"+time.strftime("%d")+u"日"
    current_time_sv = time.strftime("%Y%m%d")
    report_dir = os.path.abspath(os.path.dirname(__file__)) + "//result//"
    report_file = report_dir + current_time_sv + "自动化测试结果.html"
    report_stream = open(report_file,'wb')
    runner = HTMLTestRunner(stream=report_stream, title=current_time + u"自动化测试报告", description=u"用例执行情况如下：",
                            verbosity=2)
    runner.run(CreateSuite().creatsuite())
    report_stream.close()
    # SendMail().send_email(report_file)



if __name__ == '__main__':
    main()



