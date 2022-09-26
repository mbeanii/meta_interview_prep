#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    # []{}() -- would this be considered to be balanced? (recruiter question -- I think the answer is yes)

    # stack problem - check the top of the stack before adding the next character. Ensure if...
    # No that's not quite right.
    # Instead, check each character to see if it's an open or a close.
    # If it's an open, add it to the stack.
    # If it's a close, pop the top of the stack and see if they match (need a dict)
    # If not return No.
    # If all execute as expected, return Yes --- no not quite right; need to make sure the stack is empty first.
    # If so, return Yes, if not, return no

    # Are you happy for me to try out that solution?

    bracket_matcher = {
      "}" : "{",
      "]" : "[",
      ")" : "("
    }

    stack = []

    for char in s:
      if char in bracket_matcher.values():
        stack.append(char)
      elif len(stack) == 0:
        return "NO"
      elif stack.pop() != bracket_matcher[char]:
        return "NO"
      else:
        continue

    if len(stack) != 0:
      return "NO"
    else:
      return "YES"

## TESTBED:
## {{[()]}}
## {[()]}}

# The second testbed case helped me find a bug I'd missed - we need to check to make sure before
# popping on line 44 above that there's something to pop, otherwise we'll get an error Instead
# of a NO indicating unbalanced brackets.

# And it worked! First try again!! Having a good night :-)
# That one took me around 30 minutes.



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
