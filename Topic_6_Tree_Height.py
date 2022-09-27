class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


trip = 0
max_ = 0  ## Realized this is a prime opportunity for optimization - declaring these in the
## global scope will declare them on the heap; could improve performance a bit binary
## bringing them in from the cold, even if it's just into a local caller function.

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def height(root: Node) -> int:
    """ Returns the height of a binary tree, defined as the number of steps from the base to the
    farthest node:

    inputs:
      root (Node): The root node of a BinarySearchTree

    outputs:
      None

    raises:
      None
    """
    global trip
    global max_

    if root == None:
        return max_

    if root.left:
        trip += 1
        if trip > max_:
            max_ = trip
        height(root.left)
    if root.right:
        trip += 1
        if trip > max_:
            max_ = trip
        height(root.right)

    trip -= 1
    return max_


#  0
# / \
# \
#
# 1
# 2

tree = BinarySearchTree()
try:
    t = int(input())
except EOFError:
    pass

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))


## This one worked first time :) Good one to end on.