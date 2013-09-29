#!/usr/bin/env python
# -*- coding: utf-8 -*-

#main configs
pid_to_monitor = ['20249', '5718']	#all process ids to monitor
emails_to_alert = ['kartik@domain.com']  #all emails to alert
time_interval_seconds = 5  #after these many seconds program polls server to check processes
timeout_on_fault_seconds = 60   #after these many seconds program polls server to check processes when a fault is caught

#mail configs - from credentials
login = 'kartik@domain.com'
password = 'pass'