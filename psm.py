#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from time import sleep
from gmailer import mail

def alert(pid, eta):
	""" (str, list) -> None
	alert accepts process_id(pid) and emails_to_alert(eta) as parameter.

	>>>alert('20201',['abc@example.com', 'xyz@me.com'])

	"""
	for email in eta:
		mail(pid, email)

def isOkay(ptm, eta):
	""" (list, list) -> bool, str
	isOkay accepts pid_to_monitor(ptm) and emails_to_alert(eta) as parameter and returns True only iff 
	all pid_to_monitor are running and also returns pid at fault.

	>>>isOkay(['20301','40103'], ['abc@example.com', 'xyz@me.com'])
	[True, '']

	>>>isOkay(['20300','40103'], ['abc@example.com', 'xyz@me.com'])
	[False, '20300']
	"""
	for pid in ptm:
		stdout = Popen("ps -aef | grep -v grep | grep -w " + pid + "| awk '{print $2}'", stdout=PIPE, shell=True).stdout.read()
		if len(stdout) == 0:
			return False, pid
	return True, ''

def main(ptm, eta, tis, tofs):
	while True:
		cool, pid = isOkay(ptm, eta)
		if cool:
			#print('Looking good!')
			sleep(tis)
		else:
			#print('Failure detected for pid: '+pid)
			alert(pid, eta)
			#print('Mail sent!')
			sleep(tofs)

if __name__ == '__main__':
	from config import pid_to_monitor, emails_to_alert, time_interval_seconds, timeout_on_fault_seconds

	main(pid_to_monitor, emails_to_alert, time_interval_seconds, timeout_on_fault_seconds)