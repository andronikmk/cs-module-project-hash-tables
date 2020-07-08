# Your code here
import math
import random

lookup_table = {}

def slowfun_too_slow(x, y):
    """
    # takes two numbers
    # sets v to power
    # sets v to factorial
    """
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # slow 1: takes even slower
    # lookup_table[i] = slowfun_too_slow(x, y)
    
    # slow 2: even slower 2
    lookup_table[i] = math.pow(x, y)
    lookup_table[i] = math.factorial(lookup_table[i])
    lookup_table[i] //= (x+y)
    lookup_table[i] %= 982451653
    return lookup_table[i]

    # slow 3
    # v = math.pow(x, y)
    # v = math.factorial(v)
    # v //= (x + y)
    # v %= 982451653
    # lookup_table[(x, y)] = v
    # return v
    

# Do not modify below this line!
# this is a for loop range(0, 50000)
# that randomly generates x, y in specified ranges
# prints out the index: x, y pair

for i in range(50000):
   x = random.randrange(2, 14)
   y = random.randrange(3, 6)
   print(f'{i}: {x},{y}: {slowfun(x, y)}')