import sys
import zerorpc

# sys.argv[1] = --leader
# sys.argv[2] = --peernumber


# class Peer(object):
#     def hello(self, name):
#         return "Hello, %s" % name

# # as server
# s = zerorpc.Server(HelloRPC())
# s.bind("tcp://0.0.0.0:4242")
# s.run()

# # as client
# c = zerorpc.Client()
# c.connect("tcp://127.0.0.1:4242")
# print c.hello("RPC")