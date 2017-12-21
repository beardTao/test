from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
import os
'''定义截图函数装饰器'''
# def screenShot(func):
# 	def inner(*args,**kw):
# 		img_dir = os.
# 		return func
# 	return inner
def send_mail(report_path):
	msg = MIMEMultipart()
	#配置基本信息
	smtp_server = 'smtp.163.com'
	sender = 'beardtao@163.com'
	password = 'lin992100'
	receiver = ['383789543@qq.com']
	subject = '测试报告'
	body_info = '百傲瑞达3150测试报告'
	port = 25
	msg['from'] = sender
	msg['to'] = ";".join(receiver)
	msg['subject'] = subject
	#添加正文
	body = MIMEText(body_info,'html','utf-8')
	msg.attach(body)
	#添加附件
	#最新报告路径
	report_dir = report_path
	lists = os.listdir(report_dir)
	lists.sort(key = lambda fn:os.path.getmtime(report_dir+"\\"+fn))
	file = os.path.join(report_dir,lists[-1])
	with open(file,'rb') as f:
		mail_body = f.read()
	att = MIMEText(mail_body,'base64','utf-8')
	att['Content-Disposition'] = 'attachment;filename = test_report.html'
	msg.attach(att)
	try :
		server = smtplib.SMTP_SSL(smtp_server,port)
		server.login(sender,password)
	except:
		server = smtplib.SMTP(smtp_server,port)
		server.login(sender,password)
	server.sendmail(sender,receiver,msg.as_string())
	server.quit()