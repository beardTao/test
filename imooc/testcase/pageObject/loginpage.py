import sys
sys.path.append('../models/')
from models.base import BasePage,browser
class LoginPage(BasePage):
	#locator
	login_window_loc  = ('id','js-signin-btn')
	username_loc = ('name','email')
	password_loc = ('name','password')
	login_btn_loc = ('class name','btn-red')
	user_header_loc = ('id','header-avator')
	user_info_loc = ('class name','name')
	#错误提示信息1
	globle_info = ('id','signin-globle-error')
	#错误提示信息2
	info = ('class name','errorHint')
	#action
	def click_login_window(self):
		self.click(self.login_window_loc)
	def input_username(self,username):
		self.send_keys(self.username_loc,username)
	def input_password(self,password):
		self.send_keys(self.password_loc,password)
	def login_sub(self,username,password):
		self.input_username(username)
		self.input_password(password)
		self.click(self.login_btn_loc)
	def move_to_header(self):
		self.move_to_element(self.user_header_loc)
	def get_userinfo(self):
		#注意需要return获取到的值
		return self.get_text(self.user_info_loc)
	def get_info(self):
		#注意需要return获取到的值
		return self.get_text(self.globle_info)
	#方法成立，当提示文本时，才能获取到提示文本值，无需考虑验证码
	def get_info0(self):
		return self.find_elements(self.info)[0].text
	def get_info1(self):
		return self.find_elements(self.info)[1].text
	def get_info2(self):
		return self.find_elements(self.info)[2].text
	def username_blur(self):
		if self.username_loc[0] == 'name':
			js = 'document.getElementsByName("%s")[0].blur()'%self.username_loc[1]
		elif self.username_loc[0] == 'id':
			js = 'document.getElementById("%s").blur()'%self.username_loc[1]
		else :
			js = 'document.getElementByClassName("%s").blur()'%self.username_loc[1]
		self.execute_script(js)
	def password_blur(self):
		if self.password_loc[0] == 'name':
			js = 'document.getElementsByName("%s")[0].blur()'%self.password_loc[1]
		elif self.password_loc[0] == 'id':
			js = 'document.getElementById("%s").blur()'%self.password_loc[1]
		else :
			js = 'document.getElementByClassName("%s").blur()'%self.password_loc[1]
		self.execute_script(js)