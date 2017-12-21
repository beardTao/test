from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
'''定义截图函数装饰器'''
def screenShot(func):
	def inner(*args,**kw):
		img_dir = os.
		return func
	return inner
def send_email(file):
	#配置基础信息
	sender = 'beardtao@163.com'
	password = 'lin992100...163'
	receiver = ['383789543@qq.com']
	subject = '测试报告'
	port = 25
	msg = MIMEMultipart()
