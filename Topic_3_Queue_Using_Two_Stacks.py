# Enter your code here. Read input from STDIN. Print output to STDOUT
# implement a queue using two stacks
# it's got to have:
# enqueue
# dequeue

# TAIL 4 < 3 < 2 < 1 HEAD
# FIFO
# "head"
# "tail"
# enqueue
## 1) set tail.next to new_guy
## 2) set Queue obj.tail to new_guy
# dequeue
## 1) move "head" to the head.next

# STACK is LIFO -- 2 stacks
# TAIL [1 2 3 4] HEAD
# TAIL [1 2 3 4] HEAD

# We want to configure that so that the system does a FIFO instead:
# queue:
# [ 4 3 2 1 ]

# [1]
# [2] <-- second object, so for deque, grab me and move pointer to other one

# [2 1]

# [3 1] <-- for enqueue, put onto the one not pointed at (or with 'enqueue' pointer or whatever)
# [2]

# [3 2 1]

# [3 1] <-- dequeue
# [2]   <-- enqueue

# [3 2 1]

# [3 1]   <-- d
# [2]   <-- e

# [3 2 1]

# I think this is going to work - are you happy for me to have a stab at coding this up?

# class Queue_2p():
#  def __init__(self):
#    self.stack_1 = []
#    self.stack_2 = []
#
#    self.enqueue_ref = self.stack_1
#    self.dequeue_ref = self.stack_2
#
#  def swap_ref(self):
#    temp = self.enqueue_ref
#    self.enqueue_ref = self.dequeue_ref
#    self.dequeue_ref = temp
#
#  def enqueue(self, data):
#    self.enqueue_ref.append(data)
#    self.swap_ref()
#
#  def dequeue(self):
#    data = self.dequeue_ref.pop()
#    self.swap_ref()
#    return data
#
#  def peek(self):
#    return self.dequeue_ref[-1]

# I am having to play with this since I've never tried doing pointery things in Python
# (And if my python anscestors knew I was trying, they would be rolling in their graves)
# Using scratch.py, in the same project. I've used and deleted it a few times now.
# Kind of cheating, I know I won't be able to do that in the real interview...

# I also need a parser for the input ( I sort of just dove in here - it could've used some prior
# thought as well) str.split_lines and str.split would have done most of the work here...
# That is, if I'm allowed to use built-ins... Which I am not sure of.

# One good recruiter question here, "Do I need to check for/handle bad input data?" Might be also
# decent question in a lot of cases actually...
#queue_2p = Queue_2p()
#_input = input()
#command = ""
#value = ""
#for i, char in enumerate(_input):
#  if i == 0:
#    continue
#  if(char != " "):
#    command += char
#  elif(char == " " and command):
#    command = int(command)
#  if(command):
#    if(char != " "):
#      value += char
#    elif(char == " " and value):
#      value = int(value)
#  if(char == "\n"):
#    # execute command
#    if command == 1:
#      # Enqueue
#      queue_2p.enqueue(value)
#    elif command == 2:
#      # Dequeue
#      queue_2p.dequeue()
#    elif command == 3:
#      # Print the element at the front of the queue
#      print(queue_2p.peek())
#
#    # reset
#    command = ""
#    value = ""

## Skipping the testbed here because it's huge, so instead running on hackerrank, though
## in all honesty, I'll be a little surprised if this mess all works like I think it should.
## Kind of rude for them to not give me a parser...

## No output the first time. I am going to comment out my parser up there and start over with a
## new less ugly more pythonic one.

# Looks better maybe
# Nope, still not working.

# Running/debugging in pycharm. I know, cheating. But I think my solution has worked for awhile
# now and I just cant test it because I'm struggling to get my parser to work.

# Ok got my parser working in pycharm :) Pasted above. The trick was realizing lines whatever
# being input one at a time (because they're '\n' separated) not one block of text containing
# '\n' characters.
# Then it took a minute to realize that for the first time I need to be using the first line
# input -- to iterate over the correct number of lines.

# So my parser is working but I have an error (which is what I get for skipping the testbed)
# data = self.dequeue_ref.pop()
# IndexError: pop from empty list

## Testbedding now - should have done up front:
## Copied example:

#10      q = 10 (number of queries)  []   <- E   [] <-D
#1 42    1st query, enqueue 42       [42] <- D   [] <-E
#2       dequeue front element       Crashing here... the previous line must not have worked. Fixed.
#1 14    enqueue 14                  [14] <- D   [] <-E
#3       print the front element     This one was right -- 14
#1 28    enqueue 28                  [14] <- E   [28] <-D
#3       print the front element     This one was wrong -- which makes sense. Stack not queue.
#1 60    enqueue 60                  So only swap when enqueueing? would that work?
#1 78    enqueue 78
#2       dequeue front element
#2       dequeue front element

# I see! I skip the first command processed by the parser because of a vestige. Found it myself :)
# Retesting :)

# Done and better (see parser below). Wrong answer. It gave me 14; 28 this time.

# Back to formula.
# [1 2 3]

# [1]  <- Front
# [3 2]

# Add the first one to the front and don't swap the pointers. It's the front.
# Add the second one to the (not front)
# Add the third one to...

# What if we did like a RAM/storage situation:

# [1 2 3]

# [] <- RAM
# [1 2 3] <- storage

# Add the first one to the storage
# When adding a second one, first pop the storage off to RAM
# Then add the second one to storage and pop the first one from RAM

# When adding the third one, pop the first one to RAM
# pop the second one to RAM
# add the third one to storage
# pop the second one from RAM and push it to storage
# pop the first one from RAM and push it to storage

# Good for adding elements

# Now removing elements is as simple as popping them from storage

# Peeking will stay the same (as we pop/append to a list "backwards" in python)
# Hopefully my interviewer would have prevented me from going so far into the weeds on this...

class Queue_2p():
  def __init__(self):
    self.ram     = []
    self.storage = []

  def enqueue(self, data):
    while self.storage:
      self.ram.append(self.storage.pop())
    self.storage.append(data)  # Was erroneously self.storage = data
    while self.ram:
      self.storage.append(self.ram.pop())

  def dequeue(self):
    return self.storage.pop()

  def peek(self):
    return self.storage[-1]

# Testing yet again..

queue_2p = Queue_2p()
num_lines = int(input())
for i in range(num_lines):
    line = input()
#    if i == 0:                 These lines are vestigal.
#        continue
    if ' ' in line:
        line_split = line.split()
        assert (line_split[0] == '1')
        queue_2p.enqueue(line_split[1])
    elif line == '2':
        queue_2p.dequeue()
    elif line == '3':
        print(queue_2p.peek())

# Running again. Hopeful.
# Error return self.storage.pop()
# AttributeError: 'str' object has no attribute 'pop'
# Found. Fixed. Rerunning.
# Passed a number of them but quite a few failed due to performance issues. Pushing, then will
# optimize.