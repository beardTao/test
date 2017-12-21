import unittest
from models.base import browser,BasePage
from pageObject.loginpage import LoginPage
import time
import os
from HTMLTestRunner import HTMLTestRunner
import ddt
url = r'http://www.imooc.com'
username = ['130552119900','123','1305521199a','1@q']
@ddt.ddt
class Test6(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = browser()
		cls.login = LoginPage(cls.driver)
		cls.login.get(url)
	@ddt.data(*username)
	def test_username(self,testdata):
		'''账号位数、格式错误'''
		self.login.click_login_window()
		self.login.input_username(testdata)
		self.login.username_blur()
		result = self.login.get_info0()
		hope = '请输入正确的邮箱或手机号'
		self.assertEqual(result,hope)
		self.login.refresh()
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()