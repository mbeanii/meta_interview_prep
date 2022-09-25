"""
Topic 1 | Arrays & Strings
Designer PDF Viewer
https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

PDF-highighting.png

There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25 . There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in  assuming all letters are 1mm wide.

Example
h = [1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5] word =' torn'
The heights are t=2, o=1, r=1 and n=1. The tallest letter is 2 high and there are 4 letters. The hightlighted area will be 2*4 = 8mm^2 so the answer is 8.

Function Description

Complete the designerPdfViewer function in the editor below.

designerPdfViewer has the following parameter(s):

int h[26]: the heights of each letter
string word: a string
Returns

int: the size of the highlighted area
Input Format

The first line contains  space-separated integers describing the respective heights of each consecutive lowercase English letter, ascii[a-z].
The second line contains a single word consisting of lowercase English alphabetic letters.

Constraints
1 <= h[?] <= 7, , where ? is an English lowercase letter.
word contains no more than 10 letters.

Sample Input 0
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

Sample Output 0
9

Explanation 0
We are highlighting the word abc:

Letter heights are a=1, b=3, and c=1. The tallest letter, b is 3mm high. The selection area for this word is 3*1mm * 3mm = 9mm^2

Note: Recall that the width of each character is 1mm.

Sample Input 1
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba

Sample Output 1
28

Explanation 1
The tallest letter in zaba is z at 7mm. The selection area for this word is 4x1mm = 28mm^2.

"""

# I understand from the problem definition that I need to map be an arbitrary character array
# to their respective heights in a provided height dictionary
## No, looking again, it's not a dictionary, but rather a height array, ordered in an alphabetical
# way, so it should be indexed by position rather than key... though, to do that I'd need some
# way to map from letter to position anyway, so I'd be looking at potentially making a map from
# letter to index anyway... or I could do something with ascii values - I know python has a way to
# turn characters into their ascii equivalents, but I can't remember the exact syntax without a
# google search, so I will go the map route -- for space complexity, it would be better to do
# the ascii way though so I'd probably pursue that route in a work setting, so might be worth
# fleshing out a bit more -- I might ask the interviewer here if they'd like me to go into the
# details of this solution a bit more, or if I should stick to the map solution.

# Fleshing out the ascii solution - I'd write a function which would take a single character and
# return its relative index. It would do this by:
#     1) Typecasting the character to the integer representation of its ascii values
#     2) Subtracting the integer representation of 'A' from the integer character values
#     3) Returning the difference
# This would work because the ascii values are already ordered in ascending alphebetical order,
# just offset by the ascii value of 'A'
#
# In the caller, I could then iterate over every character in 'word' and:
#     1) Call this 'get_relative_index' function, saving the result off as 'index.'
#     2) Get the character's height value via h[index]
#
# Having fleshed this out, I actually kind of love this solution. It's got linear time complexity,
# and very little space complexity - we're really not storing anything other than the answer. As
# it is an online interview, I think at this point I'd be a bit bold and explain the above to the
# interviewer and ask for permission to do a quick google search for the python syntax to get a
# character's ascii value. (I looked it up -- it's "ord()")
#
# Also, having thought that far, it rasises an interesting question -- could the 'word' parameter
# have mixed cases? I only have 26 height values, so there shouldn't be mixed cases. If I need to
# check and handle that, I would do it as an error condition, as to_upper() or similar wouldn't
# correctly meet the problem requirement, assuming upper/lower case letters have different heights.
# Probably won't be an issue, but I'll put an error check in there just to be sure.
#
# Looking back at the problem definition, it indicates they will be lower case, so I don't need
# to worry about it.

# Ok, first problem solved. Next problem is once I have each value what do I do with it?
# I really only need the number of characters, 'k' - to multiply by '1' (or not - redundant) to get
# the rectangle's width, 'w'. As this operation is redunant, might as well just call the number of
# characters 'w' to begin with. And I need the largest value 'max_height.' So, rather than storing
# the values, let's just increment our counter variable, 'w', and compare this height against h and
# save the larger one off as max_height.
#
# Another question -- I assume the rectangle will all be on the same line? Probably don't need to
# worry about handling that as this isn't really a "Designer PDF viewer," but actually just an area
# calculator, and depending on how you handled that, the answer should be the same regardless.

# Ok, I'm ready to start coding - I'd ask the interviewer at this point if they are happy for me to
# start coding.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    max_height = 0
    w = 0
    for character in word:
        w += 1
        # get_char_index is simple enough, I can just do it inline
        # Originally I had: index = ord(character) - ord('A') -- bug here.
        index = ord(character) - ord('a')
        char_height = h[index]
        # don't need to worry about if they're equal, because then assigning to either is fine.
        max_height = char_height if char_height > max_height else max_height
    # Now I have w and max_height, so multiply them and return
    return w * max_height

# I think this will work -- let me testbed it with one of their examples:
# Sample Input 1
# 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
# zaba
#
# init variables max_heigh, w
# iterate over 'word', which is 'zaba', so the first character will be 'z'
# increment w - so w is now 1, which is what we want, so there shouldn't be an off by one error here
# index is set equal to the order of character minus the order of A (which might be redundant
# depending on how the "ord" function works -- in production I'd research the answer to this before
# delivering). But for the sake of this example, what we end up with is (counting on fingers) 22
# (remembering 'A' is 0).
# So index = 22
# char_height then equals h[index] (the 23rd by human counting) -- so using ape methods, that's...
# char_height = 5
# then we have, max_height equal to char_height so long as char_height is greater than max_height
# that's several lines in one.
# first off, it checks if char_height is greater than max_height (5 > 0) - True
# since it is, it assigns char_height to max_height, so we get max_height = 5
# and the else is ignored
# back to the top of the loop -- having proved out the logic of the loop itself, I'll go a bit
# quicker now -- (Asking the interviewer's permission here)
#
# Second time through the loop:
# character = 'a'
# w = 2
# index = 0
# h[index] = 1
# charheight > maxheight (1 > 5) - False -- so the "else" executes
# max_height = maxheight (5)
#
# Third time through the loop:
# character = 'b'
# w = 3
# index = 1
# h[index] = 3
# charheight > maxheight (3 > 5) - False -- so the "else" executes
# max_height = maxheight (5)
#
# Fourth time through the loop:
# character = 'a'
# w = 4
# index = 0
# h[index] = 1
# charheight > maxheight (1 > 5) - False -- so the "else" executes
# max_height = maxheight (5)
#
# At the end of the loop we end up with max_height = 5
# w = 4
# so w * maxheight (5 * 4)
# This would return 20.
# Checking against the expected answer:
#
# Sample Output 1
# 28
#
# So my answer is wrong, and it's quickly obvious why. The code is actually correct - I made a
# mistake while testbedding -- looking up the index of 'w' (my variable name) the first time
# through, rather than 'z' (which would have been a lot easier to do by hand to be fair).
# Thus the first time through, I'd have gotten a height of 7, which would have given me the 28
# I'm looking for.
# Cool.
# So though I'm a little embarassed about the testbed mistake I made, I'm actually happy with the
# code I've written as a result of it :)
# Testing in hackerrank -- got an error:
## char_height = h[index]
## IndexError: list index out of range
# Took me only a moment to spot the bug - I used capital 'A' as the 0 value, but all of my letters
# are lower-case, so it should be index = ord(character) - ord('a')
#
# This also answers my earlier question about whether subtracting the order of A is even necessary.
# It almost definitely is, because ASCII places capital letters before lowercase letters.
#
# Cool. All tests passed. Earned my hackerrank star :)
# Pushing solution to github.



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()

