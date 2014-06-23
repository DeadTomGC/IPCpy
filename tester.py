import time
import subprocess
import pipes
s = pipes.Template()
r = pipes.Template()
p = subprocess.Popen(['python','hello.py'],-1,None,subprocess.PIPE,subprocess.PIPE)
p.stdin.write("I am in control.\n")
p.stdin.flush();
print p.stdout.readline()
print p.stdout.readline()
print "hello from tester"
time.sleep(1)

refreshRate = 5; #Hz

