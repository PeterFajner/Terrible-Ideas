"""
The MIT License (MIT)

Copyright (c) 2015 Peter Fajner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
	
