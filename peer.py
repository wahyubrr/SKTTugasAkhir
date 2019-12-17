import sys
import zerorpc
import threading
import time
import random

# sys.argv[1] = --leaderstatus
# sys.argv[2] = --peerid
# sys.argv[3] = --leaderid
peerid = int(sys.argv[1])
# leaderid = int(sys.argv[2])
leaderstatus = int(sys.argv[2])

counter = 0

# define threading function
def counter():
	global counter
	counter = random.randint(100,500)
	while counter != 0:
		print(counter)
		counter = counter - 1
		time.sleep(1)
	print("ima leader")
def heartbeat():
	c2 = zerorpc.Client()
	c3 = zerorpc.Client()
	c2.connect("tcp://127.0.0.1:9002")
	c3.connect("tcp://127.0.0.1:9003")
	while True:
		time.sleep(5)
		print("reset counter")
		c2.resetcounter()
		c3.resetcounter()

# start threading
if leaderstatus == 0:
	cthread = threading.Thread(target=counter)
	cthread.start()
	print("thread counter started")
elif leaderstatus == 1:
	lthread = threading.Thread(target=heartbeat)
	lthread.start()

# server class
class Peer(object):
	def resetcounter(self):
		global counter
		counter = random.randint(100,500)
		print("counter changed, ", counter)

if leaderstatus == 0:
	s = zerorpc.Server(Peer())
	s.bind("tcp://0.0.0.0:900%s" % peerid)
	print("tcp://0.0.0.0:900%s" % peerid)
	s.run()

# else:
# 	c = zerorpc.Client()
# 	c.connect("tcp://127.0.0.1:900%s" % leaderid)
# 	print("wee")
# 	time.sleep(5)
# 	c.getheartbeat()
# 	print("wee")