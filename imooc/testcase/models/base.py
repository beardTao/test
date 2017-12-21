from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def browser(browser = 'firefox'):
	try:
		if browser == 'firefox':
			driver = webdriver.Firefox()
		elif browser == 'chrome':
			driver = webdriver.Chrome()
		elif browser == 'ie':
			driver = webdriver.Ie()
		elif browser == 'phantomjs':
			driver = webdriver.PhantomJS()
		else:
			print('no such browser')
		return driver
	except:
		print('no such kind of browser,you can try "firefox"')
class BasePage(object):
	#后续方法都在此基础上进行
	def __init__(self,driver):
		self.driver = driver
	'''====================浏览器方法==================='''
	#打开网页
	def get(self,url):
		self.driver.get(url)
		self.driver.maximize_window()
	#获取标题
	def get_title(self):
		return self.driver.title
	#关闭浏览器
	def close(self):
		self.driver.close()
	def quit(self):
		self.driver.quit()
	#前进
	def forward(self):
		self.driver.forward()
	#返回
	def back(self):
		self.driver.back()
	#刷新
	def refresh(self):
		self.driver.refresh()
	#执行js
	def execute_script(self,js):
		self.driver.execute_script(js)
	#回到顶部
	def scrollTop(self):
		js = 'window.scrollTo(0,0)'
		self.driver.execute_script(js)
	def scroll_to(x,y):
		js = "window.scrollTo(%d,%d)"%(x,y)
		self.driver.execute_script(js)
	'''====================元素操作==================='''
	#获取元素，后续方法有用到。
	def find_element(self,locator,timeout = 10):
		element = WebDriverWait(self.driver,timeout).until(lambda x:x.find_element(*locator))
		return element
	def find_elements(self,locator,timeout = 10):
		elements = WebDriverWait(self.driver,timeout).until(lambda x:x.find_elements(*locator))
		return elements
	#获取文本
	def get_text(self,locator):
		e = self.find_element(locator)
		return e.text
	#获取属性
	def get_attribute(self,locator,name):
		return self.find_element(locator).get_attribute(name)
	#下拉框
	def select_by_value(self,locator,value):
		Select(self.find_element(locator)).select_by_value(value)
	def select_by_index(self,locator,index):
		Select(self.find_element(locator)).select_by_index(index)
	def select_by_text(self,locator,text):
		Select(self.find_element(locator)).select_by_text(text)
	'''====================键盘事件==================='''
	#输入文本
	def send_keys(self,locator,text):
		element = self.find_element(locator)
		element.clear()
		element.send_keys(text)
	'''====================鼠标事件==================='''
	#点击事件
	def click(self,locator):
		self.find_element(locator).click()
	#鼠标悬浮事件
	def move_to_element(self,locator):
		e = self.find_element(locator)
		ActionChains(self.driver).move_to_element(e).perform()
	#双击事件
	def double_click(self,locator):
		e = self.find_element(locator)
		ActionChains(self.driver).double_click(e).perform()
	#右击事件
	def content_text(self,locator):
		e = self.find_element(locator)
		ActionChains(self.driver).content_text(e).perform()
	'''====================元素判断==================='''
	#判断文本在元素里
	def is_text_in_element(self,locator,text,timeout = 10):
		try:
			result = WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element(locator,text))
		except:
			print('元素没找到')
			return False
		else:
			return result
	def visibility_of_element_located(self,locator,driver):
		try:
			e = visibility_of_element_located(locator)(driver)
		except:
			print('元素不可见')
			return False
		else:
			return e
#测试代码
if __name__ == '__main__':
	test = Tao(browser())
	# url = 'http://www.baidu.com'
	url = 'http://www.imooc.com'
	test.get(url)
	test.click(('id','js-signin-btn'))
	test.send_keys(('name','email'),'13055211990')
	test.send_keys(('name','password'),'dianzi1312')
	test.click(('class name','btn-red'))
	test.move_to_element(('id','header-avator'))
	result = test.get_text(('class name','name'))
	print(result)