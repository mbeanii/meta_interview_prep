# I'm still thinking there might be something to the pointer idea.
# Or, could use one of them to store the number of elements in the first
# then pour it out into the first like water

# queue
# [1 2 3]

# stacks
# [3 2 1] <- storage
# []      <- bucket

# Then when dequeue is called,
# pop counter and move counter-1 elements from storage to counter.
# Then pop storage and swap the pointers.

# Truth is, with the len() method, don't even need to keep track. Just need one pointer then.
# Also, swapping the bucket and storage won't work because then bucket's order would be reversed.
# Got to move the entire thing twice every time we dequeue. Gross. At least it's still linear.

class Queue_2s():
  def __init__(self):
    self.stack_1 = []
    self.stack_2 = []

    self.storage = self.stack_1
    self.bucket = self.stack_2

  def enqueue(self, data):
    self.storage.append(data)

  def dequeue(self):
    while self.storage:
      self.bucket.append(self.storage.pop())

    return_value = self.bucket.pop()

    while self.bucket:
      self.storage.append(self.bucket.pop())

    return return_value

  def peek(self):
    return self.storage[0]

# Feeling good. Running.
# return_value = self.storage.pop()
# IndexError: pop from empty list
# Off by one error - I should have investigated closer when I had this thought earlier.
# Thing is, it's the opposite of the off by one error I thought it was.
# Fixed :)
# Wrong answer - 14; 28 again :(
# Fixed :)
# No. Oddly, no.
# Fixed :)
# This solution got a bunch more test cases to pass. However, it's still failed a few. They
# say to optimize my code. Will start there tomorrow. I still think I was close with the
# pointer-swapping thing.


queue_2p = Queue_2s()
num_lines = int(input())
for i in range(num_lines):
    line = input()
    if ' ' in line:
      line_split = line.split()
      assert (line_split[0] == '1')
      queue_2p.enqueue(line_split[1])
    elif line == '2':
        queue_2p.dequeue()
    elif line == '3':
        print(queue_2p.peek())

#10      q = 10 (number of queries)
#1 42    1st query, enqueue 42   [] [28]
#2       dequeue front element
#1 14    enqueue 14
#3       print the front element
#1 28    enqueue 28
#3       print the front element
#1 60    enqueue 60
#1 78    enqueue 78
#2       dequeue front element
#2       dequeue front element