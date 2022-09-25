"""
Topic 2 | Lists
Insert a Node at a Position Given in a List
https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
"""

## Create a new node "new_node"
## Traverse the list by starting at head and calling next ('position' - 1) times. "this" is now one before
## the requested index.
## Memoize this.next as "old_next"
## Set this's next to new_node
## Set new_node's next to old_next --- If we reverse this and the step before, we won't have to memoize
##
## So instead,
## Create a new node "new_node"
## Traverse the list by starting at head and calling next ('position' - 1) times. "this" is now one before
## the requested index.
## Set new_node's next to this.next
## Set this's next to new_node
## Done with "insert in the middle"
##
## For insertion to the head node:
## Create a new node "new_node"
## Set new_node's next to head
## Set the linked list's head to new_node
##
## I think insertion at the end is just a special case of the insertion in the middle, requiring no more code
## because at the end this.next will be null.

## At this point I'd ask the interviewer if they'd like me to start coding

## Looking at the provided class, it appears we have both a head and a tail, so in the base case, we'll need to
## do a check to see if the next node is null and if so, update the linked list class with the new tail

## Oh, we also get an insert_node already... oh, but it looks like that's to insert at the end. Could call that
## For the special case of being at the end.

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

class NegativePositionError(Exception):
  pass

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
## 1 -> 2 -> 3
## 4
## 2
## if not llist gets skipped
## new_node is created and passed 4
## if position == 0 gets skipped
## so we end up in the else
## we start traversing the list
## until we get to the one before the requested one (cannot be negative as position is not less than or equal to 0 by this point)
## so node.data is now equal to 2
## new_node is assigned to the 3 node
## and new_node becomes the 2 node's new next
## Then last, we check to see if the 2 node's next is Null - it is not
## So we exit the else block and return llist

## I feel good about this. Testing. Three tweaks were required (one failed testbed)
## I don't need to reset the head and tail because llist isn't the Linked List class, it's a node in the list.
## Pushing
def insertNodeAtPosition(llist, data, position) -> SinglyLinkedList:
  if position < 0:
    raise NegativePositionError

  if not llist:
    return_list = SinglyLinkedList()
    return_list.insert_node(data)
    return return_list

  new_node = SinglyLinkedListNode(data)

  if position == 0:
    new_node.next = llist.head
    # llist.head = new_node

  else:
    node = llist #.head
    for i in range(position - 1):
      node = node.next
    new_node.next = node.next
    node.next = new_node
    #if(new_node.next == None):
    #  llist.tail = new_node

  return llist