import sys
sys.setrecursionlimit(100000000)

MAGIC = 10900


"""
num = 0
def best(map):
	newmap = dict(map=map)
	global num
	num += 1
	print num
	best(newmap)
map = {"0": 1}
for i in xrange(0, 10925):
	num = 0
	while num < 10925:
		best(map)
"""


alltotal = 0
localtotal = 0
class adder:
	def bester(self, map):
		newmap = dict(map=map)
		self.num += 1
		print self.num
		total = newmap
		if self.num < MAGIC:
			total = self.bester(newmap)
		return total
	def __init__(self, map):
		self.num = 0
		self.total = self.bester(map)
		global localtotal
		localtotal = self.total
		

alltotal = {0:0}
for i in xrange(0, MAGIC):
	add = adder(alltotal)
	alltotal = localtotal
	
