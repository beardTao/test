import unittest
from models.base import browser,BasePage
from pageObject.loginpage import LoginPage
import time
import os
from HTMLTestRunner import HTMLTestRunner
import ddt
url = r'http://www.imooc.com'
password = ['12345','123456 ']
@ddt.ddt
class Test7(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = browser()
		cls.login = LoginPage(cls.driver)
		cls.login.get(url)
	@ddt.data(*password)
	def test_username(self,testdata):
		'''密码位数、格式错误'''
		self.login.click_login_window()
		self.login.input_password(testdata)
		self.login.password_blur()
		result = self.login.get_info1()
		hope = '请输入6-16位密码，区分大小写，不能使用空格！'
		self.assertEqual(result,hope)
		self.login.refresh()
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()