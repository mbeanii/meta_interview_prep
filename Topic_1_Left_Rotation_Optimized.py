"""
Topic 1 | Arrays & Strings
Left Rotation
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

<Not including problem definition from here on - please refer to hackerrank link above>
"""


# Ok, so optimizing. Rather than iteratively shifting left, instead I will calculate the offset to
# begin with so only one pass of the loop is required, reducing complexity from (A*B) to linear

# Ok, good. How to do that.
# Right, currently in the loop:
#   if i == 0: carryout = element; continue;
#   a[i-1] = element
# These 0 and 1 are set values assuming one shift.
# If you change to do two shifts at once, these become:
#   if i == 1: carryout = element; continue;
#   a[i-2] = element
#   AND we introduce a new problem -- our carry is no longer just a single element. i == 0 should have
#   been a carryout as well.
# So it'd actually be:
#  if i < 2: carryout_array[i] = element; continue
# for j, carry_in in enumerate[carryout_array]: a[carry_in_start + j] = carry_in
# And we also need to calculate carry_in_start
# carry_in_start would be the last element minus the size of carry_in
# I need an examples
#
# Say the array is [0, 5, 1, 2, 4] and we're shifting three times, then the 0 would end up in index 2, so the
# carry_in_start would be 2.
# is this equal to len(array) - 2?
# No, we'll get an off by one error, because the 2 is one-indexed and len(array) is 0-indexed.
# So it'll actually be:
# carry_in_start = len(array) - (d-1) -- the parentheses are redundant, so:
# carry_in_start = len(array) - d - 1
# And now I have all I need to code it.

# Coded. Stepping through my own example above with the code.
# a = [0, 5, 1, 2, 4]
# d = 3
# carry_end = 2
# carry_start = 4 - 2 (2)
## This is interesting. Why would they be the same? Is that correct, and if so, do we only need one of them?
## Or is my example too much of a special case?
## Ok, where do the carries actually start and end here?
## I use carry_end to decide when to stop adding to the carry and start shifting.
## I use carry_start to decide where to start placing the carried-in values
## They should not be the same, rather they should be on opposite sides of the middle of the array.
## In the example above, they are the same because they are the middle of the array.
## So yes, got stopped by a special case.

## Starting over with d=4 instead:
# a = [0, 5, 1, 2, 4]
# d = 4
# carry_end = 3
# carry_start = 2
## I also have an off by one error here as it seems -- len(a) is actually 1 indexed, so my correction before wants
## not required.
## Off to get coffee - I am not performing at my best right now. (Also a reminder to caffeinate before the interview)

## Renamed "carry_end" to "shifted_array_start_after" so they're both in terms of the solution.
## I am happy that shifted_array_start_after is in the right place. d-1
## What about carry_start -- 2 above. So that would mean we were carrying in 4 elements and placing them into
## A hole with space for three elements. Off by one indeed. I believe carry_start = len(a) - d fixes the problem.
# Fixed. Starting over.

# a = [0, 5, 1, 2, 4]
# d = 4
# shifted_array_start_after = 3
# carry_start = 1
## I also have an off by one error here as it seems -- len(a) is actually 1 indexed, so my correction before wants
## not required.
## Off to get coffee - I am not performing at my best right now. (Also a reminder to caffeinate before the interview)

# a = [0, 5, 1, 2, 4]
# d = 4
# shifted_array_start_after = 3
# carry_start = 1
## carry_array = []
## First time through loop:
## i = 0, element = 0
## (0 < 4) - True
## carry_array[0] = 0
## continue
## Second time through loop:
## i = 1, element = 5
## (1 < 4) - True
## carry_array[1] = 5
## continue
##
## Building array; details omitted: [0, 5, 1, 2]
## The fifth time through the loop we hit:
## (4 < 4) False
## so our carry_array is done and equal to:
## carry_array = [0, 5, 1, 2]
## Carrying on fifth time through the loop:
## a[4-4] (a[0]) = 4 ## Correct :)
## First for loop done [4, 5, 1, 2, 4] -- only the first 4 is in the right place, but we're not done yet.

## It also occurs to me that doing this in place is increasing complexity a bit. Would've been easier to
## just do a results_list.append(elem) for each. But oh well, as far as space complexity goes, I think my
## solution would actually be better, if we didn't have to copy the return list in the end regardless.

## Continuing. Entering the second loop
## a now equals [4, 5, 1, 2, 4]
## carry_array = [0, 5, 1, 2]
## i = 0; carry_in = 0
## a[0 + 1] (a[1] = 0
## a now equals [4, 0, 1, 2, 4]
## a now equals [4, 0, 5, 2, 4]
## a now equals [4, 0, 5, 1, 4]
## a now equals [4, 0, 5, 1, 2], which looks an awful lot like [0, 5, 1, 2, 4] shifted left four times.
## return a
## Done-zo. Testing.

## Nope. Missed something. Error.
##
##
## carry_array[i] = element
## IndexError: list assignment index out of range
##
## Right, ok - simple syntax error. Should have done carry_array.append(element)

## Error :( This is most disappointing.
## for i, carry_in in enumerate[carry_array]:
## TypeError: 'types.GenericAlias' object is not iterable
##
## Ouch, this one is embarassing. I used square brackets for enumerate instead of parentheses. Fixed. Running.

## Errored again. At least this time it was an issue with the algorithm, not a basic syntax thing
## 4 1 2 3 4
## Expected 5 1 2 3 4
## Ok, so the first one is wrong. Appears I've got an off by one error in there still somewhere.
## Found and fixed it. Variable "shifted_array_start_after" was never needed. d is correct because the < already
## corrects for any off by one error there. Sorted.

## All tests passed - everything ran muuuuch quicker, which was cool to see. Tests completed practically instantly
## Pushing code.

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
# [1, |0| 2, 3, 4,|1| 5]
# |0| = carry_start
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
  # There used to be a "shifted_array_start_after = d -1" on this line. Removed.
  carry_start = len(a) - d # Was erroneously carry_start = len(a) - shifted_array_start_after
  carry_array = []
  for i, element in enumerate(a):
    if i < d: # Was erroneously if i < shifted_array_start_after
      carry_array.append(element) # Was erroneously carry_array[i] = element
      continue
    a[i - d] = element

  for i, carry_in in enumerate(carry_array): # Was erroneously for i, carry_in in enumerate[carry_array]
    a[i + carry_start] = carry_in

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
