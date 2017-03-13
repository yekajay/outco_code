#
#  Homework V
#
#  Problem 1: Node class
#
#  Prompt:    Create a Node class
#             The Node class should contain the following properties:
#
#                    value:  integer value
#               left_child:  pointer to another node (initially None)
#              right_child:  pointer to another node (initially None)
#
#                 Example:   sample1 = Node()
#                            sample1.value         // None
#                            sample1.left_child    // None
#                            sample1.right_child   // None
#
#                 Example:   sample2 = Node(1)
#                            sample2.value         // 1
#                            sample2.left_child    // None
#                            sample2.right_child   // None
#
#
#  Problem 2: BinarySearchTree class.
#
#  Prompt:    Create a BinarySearchTree class
#
#             The BinarySearchTree class should contain the following
#             properties:
#
#                    root:   A pointer to the root node (initially None)
#                    size:   The number of nodes in the BinarySearchTree
#
#             The BinarySearchTree class should also contain the following
#             methods:
#
#                  insert:   A method that takes takes an integer value, and
#                            creates a node with the given input.  The method
#                            will then find the correct place to add the new
#                            node. Values larger than the current node node go
#                            to the right, and smaller values go to the left.
#
#                            Input:     value
#                            Output:    None
#
#                  search:   A method that searches if a value exists with a
#                            exists within the tree and returns true if found.
#
#                            Input:     value
#                            Output:    Boolean
#
#
#             What are the time and auxilliary space complexities of the
#             various methods?
#
#
#  Extra:     Remove method for BinarySearchTree class
#
#  Prompt:    Add the following public method to the BinarySearchTree class:
#
#                  remove:   A method that removes a value matching the input
#                            the tree is then retied so that the binary search
#                            tree order is not violated.
#

class Node(object):
	def __init__(self,v=None,lc=None,rc=None):
		self.value=v
		self.left_child=lc
		self.right_child=rc
  

class BinarySearchTree(object):
	def __init__(self,rt=None,si=0):
		self.root=rt
		self.size=si
		
	# Time Complexity: O(log n)
	# Auxiliary Space Complexity: O(log n)	
	def insert(self, value):
		self.size+=1
		tmp=Node(value)
		if self.root is None:
			self.root=tmp
		else:
			def insert_helper(curr):
				if curr is None:
					curr=tmp
				elif value <= curr.value:
					curr.left_child=insert_helper(curr.left_child)
				else:
					curr.right_child=insert_helper(curr.right_child)
				return curr
			insert_helper(self.root)
	
	# Time Complexity: O(log n)
	# Auxiliary Space Complexity: O(log n)
	def search(self, value):
		def search_helper(curr):
			if curr is None:
				return False
			if value==curr.value:
				return True
			elif value<curr.value:
				return search_helper(curr.left_child)
			else:
				return search_helper(curr.right_child)
		return search_helper(self.root)
	
	# Extra credit remove
	def remove(self, value):
		self.size-=1
		def find_min(curr):
			if curr is None:
				return curr
			while curr.left_child is not None:
				curr = curr.left_child
			return curr
		
		def remove_helper(curr,curr_value):
			if curr is None:
				return curr
			if curr.value==curr_value:
				if curr.left_child is None and curr.right_child is None:
					curr=None
				elif curr.left_child is None:
					curr = curr.right_child
				elif curr.right_child is None:
					curr=curr.left_child
				else:
					tmp=find_min(curr.right_child)
					curr.value=tmp.value
					curr.right_child=remove_helper(curr.right_child,tmp.value)
				return curr
			elif curr_value<curr.value:
				curr.left_child=remove_helper(curr.left_child,curr_value)
			else:
				curr.right_child=remove_helper(curr.right_child,curr_value)
		remove_helper(self.root,value)





















############################################################
###############  DO NOT TOUCH TEST BELOW!!!  ###############
############################################################

# custom expect function to handle tests
# List count : keeps track out how many tests pass and how many total
#   in the form of a two item array i.e., [0, 0]
# String name : describes the test
# Function test : performs a set of operations and returns a boolean
#   indicating if test passed 
def expect(count, name, test):
  if(count == None or not isinstance(count, list) or len(count) != 2):
    count = [0, 0]
  else:
    count[1] += 1
  

  result = 'false'
  errMsg = None
  try: 
    if test():
      result = ' true'
      count[0] += 1
  except Exception, err: 
    errMsg = str(err)

  print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
  if errMsg != None: 
    print('       ' + errMsg + '\n')

# code for capturing print output
from cStringIO import StringIO
import sys
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout

# code for checking if lists are equal
def lists_equal(lst1, lst2):
  if len(lst1) != len(lst2):
    return False
  for i in xrange(0, len(lst1)):
    if lst1[i] != lst2[i]:
      return False
  return True


print('Node Class')
test_count = [0, 0]

def test():
  node = Node()
  return isinstance(node, object)
expect(test_count, 'able to create an instance', test)

def test():
  node = Node()
  return hasattr(node, 'value')
expect(test_count, 'has value property', test)

def test():
  node = Node()
  return hasattr(node, 'left_child')
expect(test_count, 'has left_child property', test)

def test():
  node = Node()
  return hasattr(node, 'right_child')
expect(test_count, 'has right_child property', test)

def test():
  node = Node()
  return node.value == None
expect(test_count, 'has default value set to None', test)

def test():
  node = Node(5)
  return node.value == 5
expect(test_count, 'able to assign a value upon instantiation', test)

def test():
  node = Node()
  node.value = 5
  return node.value == 5
expect(test_count, 'able to reassign a value', test)

def test():
  node1 = Node(5)
  node2 = Node(10)
  node1.left_child = node2
  return node1.left_child.value == 10
expect(test_count, 'able to point to left child node', test)

def test():
  node1 = Node(5)
  node2 = Node(10)
  node1.right_child = node2
  return node1.right_child.value == 10
expect(test_count, 'able to point to right child node', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Binary Search Tree Class')
test_count = [0, 0]

def test():
  bst = BinarySearchTree()
  return isinstance(bst, object)
expect(test_count, 'able to create an instance', test)

def test():
  bst = BinarySearchTree()
  return hasattr(bst, 'root')
expect(test_count, 'has root property', test)

def test():
  bst = BinarySearchTree()
  return hasattr(bst, 'size')
expect(test_count, 'has size property', test)

def test():
  bst = BinarySearchTree()
  return bst.root == None
expect(test_count, 'default root set to None', test)

def test():
  bst = BinarySearchTree()
  return bst.size == 0
expect(test_count, 'default size set to 0', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('BinarySearchTree Insert Method')
test_count = [0, 0]

def test():
  bst = BinarySearchTree()
  return hasattr(bst, 'insert') and callable(getattr(bst, 'insert'))
expect(test_count, 'has insert method', test)

def test():
  bst = BinarySearchTree()
  bst.insert(5)
  return bst.size == 1 and bst.root.value == 5
expect(test_count, 'able to insert a node into empty binary search tree', test)

def test():
  bst = BinarySearchTree()
  bst.insert(5)
  bst.insert(3)
  return bst.size == 2 and bst.root.value == 5 and bst.root.left_child.value == 3
expect(test_count, 'able to insert node to left of root node', test)

def test():
  bst = BinarySearchTree()
  bst.insert(5)
  bst.insert(3)
  bst.insert(4)
  return bst.size == 3 and bst.root.value == 5 and bst.root.left_child.value == 3 and bst.root.left_child.right_child.value == 4
expect(test_count, 'able to insert node to right of node left of root node', test)

def test():
  bst = BinarySearchTree()
  bst.insert(5)
  bst.insert(8)
  return bst.size == 2 and bst.root.value == 5 and bst.root.right_child.value == 8
expect(test_count, 'able to insert node to right of root node', test)

def test():
  bst = BinarySearchTree()
  bst.insert(5)
  bst.insert(8)
  bst.insert(7)
  return bst.size == 3 and bst.root.value == 5 and bst.root.right_child.value == 8 and bst.root.right_child.left_child.value == 7
expect(test_count, 'able to insert node to left of node right of root node', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('BinarySearchTree Search Method')
test_count = [0, 0]

def test():
  bst = BinarySearchTree()
  return hasattr(bst, 'search') and callable(getattr(bst, 'search'))
expect(test_count, 'has search method', test)

def test():
  bst = BinarySearchTree()
  bst.insert(5)
  bst.insert(3)
  bst.insert(8)
  bst.insert(4)
  bst.insert(7)
  return bst.search(4) == True
expect(test_count, 'returns true when element exists in binary search tree', test)

def test():
  bst = BinarySearchTree()
  bst.insert(5)
  bst.insert(3)
  bst.insert(8)
  bst.insert(4)
  bst.insert(7)
  return bst.search(10) == False
expect(test_count, 'returns false when element does not exist in binary search tree', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
