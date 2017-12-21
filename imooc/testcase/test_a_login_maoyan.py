import unittest
from models.base import browser,BasePage
from pageObject.loginpage import LoginPage
import time
import os
from HTMLTestRunner import HTMLTestRunner
import ddt
username = [{'username':'13055211992','password':'dianzi1312'},
{'username':'21@qqssdaa.com','password':'dianzi1312'}]
@ddt.ddt
class Test(unittest.TestCase):
	def setUp(self):
		self.driver = browser()
		url = r'http://www.imooc.com'
		self.login = LoginPage(self.driver)
		self.login.get(url)
	def test_maoyan(self):
		'''登录冒烟测试'''
		self.login.click_login_window()
		self.login.login_sub('13055211990','dianzi1312')
		self.login.move_to_header()
		result = self.login.get_userinfo()
		hope = '慕工程9059550'
		self.assertEqual(result,hope)
	@ddt.data(*username)
	def test_usernameNotExist(self,username):
		'''账号未注册'''
		self.login.click_login_window()
		self.login.login_sub(username['username'],username['password'])
		result = self.login.get_info()
		hope = '账号未注册'
		self.assertEqual(result,hope)
	def test_pswError(self):
		'''登录密码错误'''
		self.login.click_login_window()
		self.login.login_sub('13055211990','1232122')
		hope = '密码错误'
		result = self.login.get_info()
		print(result)
		self.assertEqual(result,hope)
	# def test_09(self):
	# 	'''验证码'''
	# 	self.login.click_login_window()
	# 	self.login.login_sub('13055211990','dianzi1312')
	# 	hope = '请输入正确验证码'
	# 	result = self.login.get_info2()		
	def tearDown(self):
		self.login.quit()