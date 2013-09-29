#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.header    import Header
from email.mime.text import MIMEText
from getpass         import getpass
from smtplib         import SMTP_SSL
from config		 import login, password


def mail(pid, emailTo):
	""" (str, str) -> None
	Accepts process id(pid) and an email(emailTo) to send a email to.

	"""

	# create message
	msg = MIMEText('Hello,\n Live is down.\nFollowing process with pid: '+pid+' is down.\nregards,\nkartik', _charset='utf-8')
	msg['Subject'] = Header('Live down', 'utf-8')
	msg['From'] = login
	msg['To'] = emailTo

	# send it via gmail
	s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
	s.set_debuglevel(0)
	try:
	    s.login(login, password)
	    s.sendmail(msg['From'], msg['To'], msg.as_string())
	finally:
	    s.quit()