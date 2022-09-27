#!/bin/python3

import math
import os
import random
import re
import sys

def find_n(n, arr) -> int:
  for i, element in enumerate(arr):
    if element == n:
      return i

def swap(arr, i, j):
  temp = arr[j]
  arr[j] = arr[i]
  arr[i] = temp
  return


def insertionSort2_worker(n_index, arr, len_array_zero_index, counter):
  while True:
    if not counter:
      print(arr)
    if (n_index - 1 >= 0) and (arr[n_index] < arr[n_index - 1]):
      swap(arr, arr[n_index], arr[n_index - 1])
      counter += 1
      insertionSort2_worker(n_index, arr, len_array_zero_index, counter)
      counter -= 1
      n_index = n_index - 1
      assert(n_index >= 0)
    elif (n_index + 1 <= len_array_zero_index) and arr[n_index] > arr[n_index + 1]:
      swap(arr, arr[n_index], arr[n_index + 1])
      counter += 1
      insertionSort2_worker(n_index, arr, len_array_zero_index, counter)
      counter -= 1
      n_index = n_index + 1
      assert(n_index <= len_array_zero_index)
    else:
      return n_index

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
  n_index = find_n(n, arr)
  len_array_zero_index = len(arr) - 1
  counter = 0
  n_index = insertionSort2_worker(n_index, arr, len_array_zero_index, counter)

  return

# Ok testbed
# 7
# 3 4 7 5 6 2 1
# 3 4 5 7 6 2 1
# 3 4 5 6 7 2 1
# 3 4 5 6 2 7 1
# problem - This would have sorted one element (part 1 from what I gather).
# I am trying to sort them all...
# So every time I need a swap, it should also sort the swapper and the swapee.
# Not a problem though. Just a simple recurse.
# Ok. I put a recursive call each time something is sorted to sort the other thing as well.
# That'll result in too many prints though...

# Testbed again
# 7
# 3 4 7 5 6 2 1
# 3 4 5 7 6 2 1
# 3 4 5 6 7 2 1
# 2 3 4 5 6 7 1
# 1 2 3 4 5 6 7

## Ok caught and fixed quite a few bugs. Ready to test.
# arr[j] = arr[i]
# IndexError: list index out of range

# I went off into the weeds on this one. As I'm looking at how to resolve the error, I'm realizing
# the problem that I thought I was solving is different than the stated problem.

# That's a BIG lesson to me to slow down and make sure I understand what it is that I'm trying to do
# before I start. Really understand. If I get lost or if something is "over my head," I should
# clarify and think it through until I do understand so I don't end up trying to solve the wrong
# problem.

# I think the bottom line here is that I'm really not ready for this interview and need to do a solid
# 6-9 months work in data structures and algortihms in order to get ready. Discouraging.

# I am still going to do my interview tomorrow to the best of my ability. I'm going into it with
# low confidence in passing, but am looking forward to the learning experience. And I may surprise
# myself. I am already stronger for the effort.

# After that, I'll need to make a plan to get to where I want to be. Which is to earn the respect
# of the engineering community through my work ethic and technical accumen. There are a number of
# paths that would get me there, and they all involve courage, work, and regular practice.

if __name__ == '__main__':
  n = int(input().strip())

  arr = list(map(int, input().rstrip().split()))

  insertionSort2(n, arr)
