#!/bin/python

import subprocess 

pwd = subprocess.Popen(['cat','/etc/passwd'],stdout=subprocess.PIPE,) ## The "PWD" variable hold  "/"
grep = subprocess.Popen(['grep','lucky'],stdin=pwd.stdout,stdout=subprocess.PIPE,)
cut = subprocess.Popen(['cut', '-f', '1', '-d:'],stdin=grep.stdout,stdout=subprocess.PIPE,)
end = cut.stdout
print "End of Subprocess :\C"
for line in end:
        print line

