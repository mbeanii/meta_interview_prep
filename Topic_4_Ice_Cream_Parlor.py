#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
  # Write your code here
  hashmap = {}

  for i_index, i_value in enumerate(arr):
    for j_index, j_value in enumerate(arr):
      if i_index == j_index:
        continue
      if (i_value,j_value) not in hashmap:
        product = i_value * j_value
        hashmap[(i_value, j_value)] = product
        hashmap[(j_value, i_value)] = product
      else:
        product = hashmap[(i_value,j_value)]
      if product == m:
        return [i_index, j_index]

# Happy with this - going to try running
# I actually took the fact that I was happy with it and going to try running it as a clue that
# I probably needed to do a proofreading readthrough and ended up changing several things, including
# catching one of my bugs (hopefully my only) -- using list indices as hashmap keys would not have
# worked. Hopefully when I raised that question and didn't know, the interviewer would have told me
# I was right about not using them; I did have to google it. Tuples work as long as everything in them
# is immutable. Integers are, so we are good to go using tuples.
#
# I should run through a quick example -- I'll use their provided one.
# m = 6
# arr = [1. 3 4 5 6.]

#demo = [
#  (1,3):3,
#  (3,1):3,
#  (1,4):4,
#  (4,1):4,
#  (1,5):5,
#  (5,1):5,
#  (1,6):6,
#  (6,1):6,
#]
# 6

# I honestly don't understand why the testbed for this one is saying I got it wrong. I thought at
# first that I was returning the wrong thing - indices instead of answers, but I've had a look at
# their solutions and it appeared I was right the first time. Pushing solution. It's not passing
# testbed, but I need to move on.

# Enjoyed reading through some of my peers' solutions in the comments, though. A lot of them solved
# it in fewer lines and/or more efficiently.

# One person walked the array only once while using clever subtraction. (m - i)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
