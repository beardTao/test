import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner
from libs.func import send_mail
case_dir = r'testcase/'
def cases():
	discover = unittest.defaultTestLoader.discover(case_dir,pattern = '*_test.py',top_level_dir = None)
	return discover	
if __name__ == '__main__':
	# testSuite = unittest.TestSuite()
	# testSuite.addTest(Test('test_01'))
	a = time.strftime('%y_%m_%d_%H_%M_%S')
	file_path = os.path.join('./report/report',a+'report.html')
	fp = open(file_path,'wb')
	runner = HTMLTestRunner(stream = fp,title = '慕课网测试报告',description = '环境windows 10 浏览器：firefox')
	runner.run(cases())
	fp.close()
	send_mail(r'./report/report')