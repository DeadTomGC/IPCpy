import time
import sys
from threading  import Thread
from Queue import Queue, Empty
refreshRate = 1; #Hz

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

q = Queue()
t = Thread(target=enqueue_output, args=(sys.stdin, q))
t.daemon = True # thread dies with the program
t.start()

while True:
    oldTime = time.time()
    try: line = q.get_nowait() # or q.get(timeout=.1)
    except Empty:
        sys.stderr.write('mirror no output yet\n')
    else:
        sys.stdout.write(str(int(line[:-1])+1)+"\n")
        sys.stdout.flush()
    time.sleep(0.1)
    curTime = time.time()
    if curTime-oldTime<1.0/refreshRate:
        time.sleep(1.0/refreshRate - (curTime-oldTime))
    else:
        sys.stderr.write("mirror Falling behind!!!\n")
