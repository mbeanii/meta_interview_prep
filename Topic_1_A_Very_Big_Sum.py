"""
Topic 1 | Arrays & Strings
A Very Big Sum (Warm-up, learning how to use HackerRank)
https://www.hackerrank.com/challenges/a-very-big-sum/problem

In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Function Description

Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

aVeryBigSum has the following parameter(s):

int ar[n]: an array of integers .
Return

long: the sum of all array elements
Input Format

The first line of the input consists of an integer .
The next line contains  space-separated integers contained in the array.

Output Format

Return the integer sum of the elements in the array.

Constraints


Sample Input

5
1000000001 1000000002 1000000003 1000000004 1000000005
Output

5000000015
Note:

The range of the 32-bit integer is [-2147483648 to 2147483647].
When we add several integer values, the resulting sum might exceed the above range. You might need to use long int C/C++/Java to store such sums.
"""

# calculate and print the sum of the elements in an array (some of these "integers" may be "quite large")

## Will the built-in integer data structure be big enough to handle the sum or will
## I need to think about using/implementing something like "bigint?"
## I'm fairly sure that if a number surpasses what the int class can handle, python starts using scientific notation and carries on just fine. I will continue under this premise, though I'm wondering if that will defeat the purpose a bit as it seems like this exercise may be in part testing whether the programmer knows how to typecast appropriately.
## Are they all integers? -- yes, the question clarfies this
## Is it the sum that's "quite large" or the integers themselves? -- looks like the addends may be quite large

## First line of input appears to be the number of elements in the array.
## Judging by the sample output, this top number is NOT included in the output sum.

## Ah, I see - the "Input" is not the same as our function's "ar" variable -- that will just be the data bits of the input per the main function block.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    # I think python's sum() function can handle this without any fuss.
    # It kind of feels like a bit of a cheat, but honestly, looping over The
    # array and summing isn't that much more complex still. All of this
    # still assuming that the magic of python is going to handle the datatypes
    # for me.
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
