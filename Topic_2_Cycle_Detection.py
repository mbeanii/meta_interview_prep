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

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
  # Pointers have address values, but I've never thought about how to look at them in python3
  # If I had the address of my node, I could:
  # 1) Check to see if it's in my dictionary already
  # 2) If not save it;
  # 2b) If so, return 1
  # 3) Navigate to the next node in the list
  # Then return 0

  # If I had the size of the list, I could check to see if the number of nodes I'd visited
  # exceeded the number of elements in the list.

  # Oh, I think I know a way to do my first solution -- I think in Python if you add an object
  # to a dictionary, it does it via pointers in the background, so I'd like to give that a try.

  # "Are you ready for me to try that approach?"
  node = head
  hashmap = {}
  while node:
    if node in hashmap:
      return 1
    hashmap[node] = None
    node = node.next
  return 0

  ## Testbed (did the commentary bits out loud - it was much quicker and good practice ;) )
  ## 1 > 2 > 3 > Null [ 1 2 3 ] 0
  ## 1 > 2 > 1 > 2... [ 1 2 ]   1
  ## Null

  ## Ready to run in hackerrank
  ## Pass. Beautiful. That one only took me around 20 minutes and it passed the first time :-)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1);
        temp = llist.head;

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()