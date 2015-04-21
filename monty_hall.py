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
    
