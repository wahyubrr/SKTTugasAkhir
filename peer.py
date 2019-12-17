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
randlow = 10
randhigh = 20
counter = 0
print("peer id: %s" % peerid)
print("leader status: %s" % leaderstatus)

# define threading function
def counter():
	global counter
	counter = random.randint(randlow, randhigh)
	while counter != 0:
		print(counter)
		counter = counter - 1
		time.sleep(1)
	bealeader()
def heartbeat():
	c2 = c3 = zerorpc.Client()
	if peerid == 1 and leaderstatus == 1:
		c2.connect("tcp://127.0.0.1:9002")
		c3.connect("tcp://127.0.0.1:9003")
	elif peerid == 2 and leaderstatus == 1:
		c3.connect("tcp://127.0.0.1:9003")
	elif peerid == 3 and leaderstatus == 1:
		c2.connect("tcp://127.0.0.1:9002")
	while True:
		print("reset counter")
		if peerid == 2 and leaderstatus == 1:
			c3.resetcounter()
		if peerid == 3 and leaderstatus == 1:
			c2.resetcounter()
		if peerid == 1 and leaderstatus == 1:
			c2.resetcounter()
			c3.resetcounter()
		time.sleep(5)
def bealeader():
	global leaderstatus
	leaderstatus = 1
	lthread = threading.Thread(target=heartbeat)
	lthread.start()
	print("peer id: %s" % peerid)
	print("leader status: %s" % leaderstatus)

# start threading
if leaderstatus == 0:
	cthread = threading.Thread(target=counter)
	cthread.start()
	print("thread counter started")
elif leaderstatus == 1:
	bealeader()

# server class
class Peer(object):
	def resetcounter(self):
		global counter
		counter = random.randint(randlow, randhigh)
		print("counter changed, ", counter)

# if slave, open a server
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