# coding:utf-8
from util.send_mail import SendMail
from util.create_suite import CreateSuite
import time
import os
from HTMLTestRunner import HTMLTestRunner


def main():
    current_time = time.strftime("%Y%m%d")
    report_dir = os.path.abspath(os.path.dirname(__file__)) + "//result//"
    report_file = report_dir + current_time + "TestResult.html"
    report_stream = open(report_file, "wb")
    runner = HTMLTestRunner(stream=report_stream, title=current_time + u"自动化测试报告", description=u"用例执行情况如下：",
                            verbosity=2)
    runner.run(CreateSuite().creatsuite())
    report_stream.close()
    # SendMail().send_email(report_file)


if __name__ == '__main__':
    main()



