#!/bin/python

import os,subprocess,sys,time

path = '/usr/apache/apache-tomcat-9.0.0.M3/bin'
sec = 5
process = "ps -ef | grep -v grep | grep " + path + " | wc -l"
pid = 'ps -ef | grep -v grep | grep ' + path + ' | awk \'{print $2}\''

print "Welcome to Tomcat Restart Python Script"
print "1)Status "
print "2)Start "
print "3)Stop "
print "4)Restart "


def status():
        tpid = subprocess.Popen(process,stdout=subprocess.PIPE,shell=True)
        opt, err = tpid.communicate()
        if int(opt) < 1:
                print "Tomcat process is not running"
        else:
                print "Tomcat process is running"
        return()

def start():
        subprocess.call(path + "/startup.sh",stdout=subprocess.PIPE,shell=True)
        return()

def stop():
        subprocess.call(path + "/shutdown.sh",stdout=subprocess.PIPE,shell=True)
        return()

def restart():
        tpid = subprocess.Popen(process,stdout=subprocess.PIPE,shell=True)
        opt, err = tpid.communicate()
        if int(opt) < 1:
                subprocess.Popen([path + "/startup.sh"], stdout=subprocess.PIPE)
        else:
                subprocess.Popen([path + "/shutdown.sh"], stdout=subprocess.PIPE)
                time.sleep(sec)
                tpid = subprocess.Popen(process,stdout=subprocess.PIPE,shell=True)
                opt, err = tpid.communicate()
                if int(opt) < 1:
                        subprocess.Popen([path + "/startup.sh"], stdout=subprocess.PIPE)
                else:
                        tpid = subprocess.Popen([pid], stdout=subprocess.PIPE, shell=True)
                        out, err = tPid.communicate()
                        subprocess.Popen(["kill -9 out"], stdout=subprocess.PIPE, shell=True)
                        print "Tomcat failed to shutdown, so killed with PID " + out
                        subprocess.Popen([path + "/startup.sh"], stdout=subprocess.PIPE)
        return()

choice = input("Enter your Choice : ")

if choice > 4:
	print "Invalid Choice, Please go tthrough the usage again"
if choice  == 1:
        status()
elif choice == 2:
        start()
elif choice == 3:
        stop()
elif choice == 4:
        restart()

