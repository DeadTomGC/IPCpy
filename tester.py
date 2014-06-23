import time
import subprocess
import pipes
import sys
from threading  import Thread
from Queue import Queue, Empty


refreshRate = 1; #Hz
p = subprocess.Popen(['python','mirror.py'],-1,None,subprocess.PIPE,subprocess.PIPE)
p.stdin.write("1\n")
p.stdin.flush()

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()


q = Queue()
t = Thread(target=enqueue_output, args=(p.stdout, q))
t.daemon = True # thread dies with the program
t.start()

while True:
    oldTime = time.time()
    try: line = q.get_nowait() # or q.get(timeout=.1)
    except Empty:
        print('tester no output yet')
    else:
        p.stdin.write(str(int(line[:-1])+1)+"\n")
        p.stdin.flush()
        print line[:-1]
    time.sleep(0.1)
    curTime = time.time()
    
    if curTime-oldTime<1.0/refreshRate:
        time.sleep(1.0/refreshRate - (curTime-oldTime))
    else:
        print "tester Falling behind!!!"
