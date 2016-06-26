#!/bin/python
import os
import subprocess

HOME=/u01/tomcat
PID=subprocess.Popen(ps -ef | grep catalina | grep -v grep | awk '{print $2}',shell=True)

def usage():
	print "1)Status "
	print "2)Stop "
	print "3)Start "
	print "4)Restart "
	return()
def status():
	if PID == 0:
		print "Tomcat service is not running"
	else:
		print "Tomcat service is running"
	return status()
def stop():
	subprocess.Popen('HOME/bin/shutdown.sh',shell=True)
	return stop()
def start():
	subprocess.Popen('HOME/bin/startup.sh',shell=True)
	return start()
def restart():
	if PID == 0:
		subprocess.Popen('HOME/bin/startup.sh',shell=True)
	else:
		subprocess.Popen('HOME/bin/shutdown.sh',shell=True)
		time.sleep(60)
		PID=subprocess.Popen(ps -ef | grep catalina | grep -v grep | awk '{print $2}',shell=True)
		if PID == 0:
			 subprocess.Popen('HOME/bin/startup.sh',shell=True)
		else:
			subprocess.Popen('kill - 9 PID',shell=True)
			subprocess.Popen('HOME/bin/startup.sh',shell=True)			
	return restart()

choice = input("Enter your choice : ")

if choice == 1:
	status()
elif choice == 2:
	stop()
elif choice == 3:
	start()
elif choice == 4:
	restart()
elif choice >= 4:
	print "Invalid Entry"
