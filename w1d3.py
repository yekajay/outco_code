#  Homework III
#
#  Problem 1: Node class
#
#  Prompt:    Create a Node class
#             The Node class should contain the following properties:
#
#                 value:   integer value (default None)
#                  next:   pointer to another node (default None)
#
#               Example:   input: let sample1 = new Node(1)
#                          sample1.value     // 1
#                          sample1.next      // None
#
#               Example:   input: let sample2 = new Node()
#                          sample2.value     // None
#                          sample2.next      // None
#
#
#  Problem 2:  LinkedList class
#
#  Prompt:     Create a LinkedList class
#              The LinkedList class should contain the following properties:
#
#                length:   The number of nodes in the linked list
#                  head:   A pointer to the head node
#                  tail:   A pointer to the tail node
#
#              The LinkedList class should also contain the following methods:
#
#                append:   A method that appends a value to the end of the
#                          LinkedList.
#
#                          Input:     value
#                          Output:    None
#
#                insert:   A method that inserts an integer value at a set
#                          index in the LinkedList (assume head index is 0).
#
#                          Input:     value, index
#                          Output:    None
#
#                remove:   A method that removes a node at a specified index.
#
#                          Input:     index
#                          Output:    None
#
#              contains:   A method that checks to see if a value is contained
#                          in the list.
#
#                          Input:     value
#                          Output:    Boolean
#
#    What are the time and auxiliary space complexity of the various
#    methods?
#


class Node(object):
	def __init__(self,v=None,n=None):
		self.value=v
		self.next=n


class LinkedList:
  def __init__(self):
	self.length=0
	self.head=None  # initialization crucial
	self.tail=None  # remember tail


  # Time Complexity: O(1)
  # Auxiliary Space Complexity: O(1)
  def append(self, value):
	self.length+=1
	tmp=Node(value)
	if self.tail is None:
		self.tail=tmp
		self.head=tmp
	else:
		self.tail.next=tmp
		self.tail=self.tail.next


  # Time Complexity: O(n)
  # Auxiliary Space Complexity: O(1)
  def insert(self, value, index):
	if index>self.length or index<0:  # check thoroughly for out of bounds
		return None
	self.length+=1
	tmp=Node(value)
	if index==0:
		tmp.next=self.head
		self.head=tmp
		if self.tail is None:
			self.tail=tmp
	else:
		counter=0
		curr=self.head
		prev=None
		while counter<index:
			counter+=1
			prev=curr
			curr=curr.next
		if counter==index:
			prev.next=tmp
			tmp.next=curr
		if index==self.length-1:
            self.tail=tmp
        else:
            self.tail=curr


  # Time Complexity: O(n)
  # Auxiliary Space Complexity: O(1)
  def remove(self, index):
	if index>=self.length or index<0:
		return None
	self.length-=1
	if index==0:
		self.head=self.head.next
		if self.head is None:
			self.tail=self.head
	else:
		counter=0
		curr=self.head
		while counter<index-1:
			counter+=1
			curr=curr.next
		if curr.next.value==self.tail.value:
			self.tail=curr
		curr.next=curr.next.next


  # Time Complexity: O(n)
  # Auxiliary Space Complexity: O(1)
  def contains(self, value):
	curr=self.head
	while curr is not None:
		if curr.value == value:
			return True
		curr=curr.next
	return False


	
	
	








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
  return hasattr(node, 'next')
expect(test_count, 'has next property', test)

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
  node1.next = node2
  return node1.next.value == 10
expect(test_count, 'able to point to another node', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('LinkedList Class')
test_count = [0, 0]

def test():
  linked_list = LinkedList()
  return isinstance(linked_list, object)
expect(test_count, 'able to create an instance', test)

def test():
  linked_list = LinkedList()
  return hasattr(linked_list, 'head')
expect(test_count, 'has head property', test)

def test():
  linked_list = LinkedList()
  return hasattr(linked_list, 'tail')
expect(test_count, 'has tail property', test)

def test():
  linked_list = LinkedList()
  return hasattr(linked_list, 'length')
expect(test_count, 'has length property', test)

def test():
  linked_list = LinkedList()
  return linked_list.head == None
expect(test_count, 'default head set to None', test)

def test():
  linked_list = LinkedList()
  return linked_list.tail == None
expect(test_count, 'default tail set to None', test)

def test():
  linked_list = LinkedList()
  return linked_list.length == 0
expect(test_count, 'default length set to 0', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('LinkedList Insert Method')
test_count = [0, 0]

def test():
  linked_list = LinkedList()
  return hasattr(linked_list, 'insert') and callable(getattr(linked_list, 'insert'))
expect(test_count, 'has insert method', test)

def test():
  linked_list = LinkedList()
  linked_list.insert(5, 0)
  return linked_list.length == 1 and linked_list.head.value == 5 and linked_list.tail.value == 5
expect(test_count, 'able to insert a node into empty linked list', test)

def test():
  linked_list = LinkedList()
  linked_list.insert(5, 0)
  linked_list.insert(10, 1)
  return linked_list.length == 2 and linked_list.head.value == 5 and linked_list.tail.value == 10
expect(test_count, 'able to insert a node after another node', test)

def test():
  linked_list = LinkedList()
  linked_list.insert(5, 0)
  linked_list.insert(10, 0)
  return linked_list.length == 2 and linked_list.head.value == 10 and linked_list.tail.value == 5
expect(test_count, 'able to insert a node before another node', test)

def test():
  linked_list = LinkedList()
  linked_list.insert(5, 0)
  linked_list.insert(10, 1)
  linked_list.insert(7, 1)
  return linked_list.length == 3 and linked_list.head.value == 5 and linked_list.tail.value == 10 and linked_list.head.next.value == 7
expect(test_count, 'able to insert a node in between two nodes', test)

def test():
  linked_list = LinkedList()
  linked_list.insert(5, -1)
  linked_list.insert(10, 3)
  return linked_list.length == 0 and linked_list.head == None and linked_list.tail == None
expect(test_count, 'does not insert a node if index is out of bounds', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('LinkedList Append Method')
test_count = [0, 0]

def test():
  linked_list = LinkedList()
  return hasattr(linked_list, 'append') and callable(getattr(linked_list, 'append'))
expect(test_count, 'has append method', test)

def test():
  linked_list = LinkedList()
  linked_list.append(5)
  return linked_list.length == 1 and linked_list.head.value == 5 and linked_list.tail.value == 5
expect(test_count, 'able to append a node into empty linked list', test)

def test():
  linked_list = LinkedList()
  linked_list.append(5)
  linked_list.append(10)
  return linked_list.length == 2 and linked_list.head.value == 5 and linked_list.tail.value == 10
expect(test_count, 'able to append a second node into linked list', test)

def test():
  linked_list = LinkedList()
  linked_list.append(5)
  linked_list.append(10)
  linked_list.append(15)
  return linked_list.length == 3 and linked_list.head.value == 5 and linked_list.tail.value == 15
expect(test_count, 'able to append a third node into linked list', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('LinkedList Remove Method')
test_count = [0, 0]

def test():
  linked_list = LinkedList()
  return hasattr(linked_list, 'remove') and callable(getattr(linked_list, 'remove'))
expect(test_count, 'has remove method', test)

def test():
  linked_list = LinkedList()
  linked_list.append(5)
  linked_list.append(10)
  linked_list.remove(0)
  return linked_list.length == 1 and linked_list.head.value == 10 and linked_list.tail.value == 10
expect(test_count, 'able to remove a node from the head', test)

def test():
  linked_list = LinkedList()
  linked_list.append(5)
  linked_list.append(10)
  linked_list.remove(1)
  return linked_list.length == 1 and linked_list.head.value == 5 and linked_list.tail.value == 5
expect(test_count, 'able to remove a node from the tail', test)

def test():
  linked_list = LinkedList()
  linked_list.append(5)
  linked_list.append(10)
  linked_list.append(15)
  linked_list.remove(1)
  return linked_list.length == 2 and linked_list.head.value == 5 and linked_list.tail.value == 15
expect(test_count, 'able to remove a node in between two nodes', test)

def test():
  linked_list = LinkedList()
  linked_list.append(5)
  linked_list.remove(0)
  return linked_list.length == 0 and linked_list.head == None and linked_list.tail == None
expect(test_count, 'able to remove the only node in a linked list', test)

def test():
  linked_list = LinkedList()
  linked_list.append(5)
  linked_list.remove(-1)
  linked_list.remove(2)
  return linked_list.length == 1 and linked_list.head.value == 5 and linked_list.tail.value == 5
expect(test_count, 'does not remove a node when the index is out of bounds', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('LinkedList Contains Method')
test_count = [0, 0]

def test():
  linked_list = LinkedList()
  return hasattr(linked_list, 'contains') and callable(getattr(linked_list, 'contains'))
expect(test_count, 'has contains method', test)

def test():
  linked_list = LinkedList()
  linked_list.append(5)
  linked_list.append(10)
  linked_list.append(15)
  return linked_list.contains(15) == True
expect(test_count, 'returns True if linked list contains value', test)

def test():
  linked_list = LinkedList()
  linked_list.append(5)
  linked_list.append(10)
  linked_list.append(15)
  return linked_list.contains(8) == False
expect(test_count, 'returns False if linked list contains value', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

