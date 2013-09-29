#Server monitoring tool

Inspired by the need to get immediate email alert, in case any wanted process running on server goes down, instead on relying on manual techniques.<br/>

This command-line utility runs indefinetly in the background polling server at regular intervals* to check if any required processes* are down, if so send emails to entire* team.<br/>
Note: * are configurable
<br/>

##How to set up for use:
1). First edit config.py as follows:<br/>
```python
#main configs
pid_to_monitor = ['20249', '5718']	#all process ids to monitor
emails_to_alert = ['kartik@domain.com']  #all emails to alert
time_interval_seconds = 60  #after these many seconds program polls server to check processes
timeout_on_fault_seconds = 1500   #after these many seconds program polls server to check processes when a fault is caught

#mail configs - from credentials (gmail account is required)
login = 'kartik@domain.com'
password = 'demo'
```
<br/>
2). execute program: $ python psm.py<br/>

Note: At the moment program must be restarted once fault occurs, will add updation of pids during runtime feature soon.


