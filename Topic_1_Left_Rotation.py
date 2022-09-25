"""
Topic 1 | Arrays & Strings
Left Rotation
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

<Not including problem definition from here on - please refer to hackerrank link above>
"""


# I originally solved this with paragraphs of comments of explanation as to my thought process as I was solving
# it, but then I went to lunch without saving it off, and lost it. Lesson learned - always push code before
# stepping away. Just recreating the solution here.

# This solution passed most hackerrank test cases, but failed to execute three of them in time with a
# "please optimize your code" error message. Pushing this solution then will optimize.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotate_left_once(a: list) -> None:
  """ Performs one left rotation on the list.

  Inputs:
    a (list): List of integers to be rotated

  Outputs:
    None (performs in place)

  Raises:
    None
  """
  carry_out = None
  for i, element in enumerate(a):    # May ask permission to do this - I know how to do by hand if required
    if i == 0:
      carry_out = element
      continue
    a[i-1] = element
  a[-1] = carry_out                  # If this is too much python magic, a[len(a)] = element works too
  return


def rotLeft(a: list, d: int) -> list:
  """ Performs a carry-in rotation of array a, d times

  Inputs:
    a (list): List of integers to be rotated
    d (int) : The number of times to rotate list 'a'  --- Clarifying question - will this always be positive?

  Outputs:
    a (list): A copy of the array 'a' after the shift operations -- per requirement

  Raises:
    None
  """
  for i in range(d):              # Once again, depends on if I'm allowed to use built-ins.
    rotate_left_once(a)           # The c way to do this would be: if(i=0; i<len(d); i++)
  return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
