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

import random, sys

success = 0
attempts = 0


"""
create three doors, one true two false
select door
open one
switch to other
check if true or false
attemps ++
if chosen is true, success++
"""

def do_the_thing():
    doors = [False, False, False]
    doors[random.randint(0, 2)] = True # winner door
    choice = random.randint(0, 2) # original choice door
    done = False
    """
    while not done: # choose the removed door
        pick = random.randint(0, 2)
        if not doors[pick]: # check if it's false; if it's true, it's a winner, can't remove
            doors[pick] = 3 # set the value of the removed door to 3
            done = True
    # we assume the contestant switches, so he wins if his original choice is not the winner door
    """
    if doors[choice] != True:
        return 1
    return 0

for i in xrange(0, int(sys.argv[1])):
    success += do_the_thing()
    attempts += 1
    
print (success / float(attempts))
    
