# Homework IV                              
#                                                                 
# Problem 1: Insertion Sort                                          
#                                                                 
# Prompt:    Given an unsorted list of integers, return the list   
#            sorted using insertion sort.                            
#                                                                 
#            What are the time and auxilliary space complexity?      
#                                                                 
# Input:     An unsorted list of integers                           
# Output:    A sorted list of integers                              
#                                                                 
# Example:   input = [3,9,1,4,7] , output = [1,3,4,7,9]              
#                                                                 
#                                                                 
#                                                                 
# Problem 2: Selection Sort                                          
#                                                                 
# Prompt:    Given an unsorted list of integers, return the list   
#            sorted using selection sort.                            
#                                                                 
#            What are the time and auxilliary space complexity?      
#                                                                 
# Input:     An unsorted list of integers                           
# Output:    A sorted list of integers                              
#                                                                 
# Example:   input = [3,9,1,4,7] , output = [1,3,4,7,9]              
#                                                                 
#                                                                 
#                                                                 
# Problem 3: Bubble Sort                                             
#                                                                 
# Prompt:    Given an unsorted list of integers, return the list   
#            sorted using bubble sort.                               
#                                                                 
#            What are the time and auxilliary space complexity?      
#                                                                 
# Input:     An unsorted list of integers                           
# Output:    A sorted list of integers                              
#                                                                 
# Example:   input = [3,9,1,4,7] , output = [1,3,4,7,9]              
#

# Time Complexity: O(n^2)
# Auxiliary Space Complexity: O(1)
def insertion_sort(input):
	for i in range(1,len(input)):
		index=i
		while index>0 and input[index]<input[index-1]:
			input[index],input[index-1]=input[index-1],input[index]
			index-=1
	return input


# Time Complexity: O(n^2)
# Auxiliary Space Complexity: O(1)
def selection_sort(input):
	for i in range(len(input)-1):
		for j in range(i+1,len(input)):
			if input[j]<input[i]:
				input[j],input[i]=input[i],input[j]
	return input



# Time Complexity: O(n^2)
# Auxiliary Space Complexity: O(1)
def bubble_sort(input):
	for i in range(len(input)-1,-1,-1):
		for j in range(i):
			if input[j]>input[j+1]:
				input[j],input[j+1]=input[j+1],input[j]
	return input















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

# custom function for checking if list is sorted (linear runtime)
def is_sorted(input):
  if (len(input) < 2):
    return True
  for i in xrange(1, len(input)):
    if (input[i-1] > input[i]):
      return False
  return True


print('Insertion Sort Tests')
test_count = [0, 0]

def test():
  example = insertion_sort([3,9,1,4,7])
  return lists_equal(example, [1,3,4,7,9])
expect(test_count, 'should sort example input', test)

def test():
  example = insertion_sort([])
  return lists_equal(example, [])
expect(test_count, 'should return empty array for empty input', test)

def test():
  example = insertion_sort([10])
  return lists_equal(example, [10])
expect(test_count, 'should sort single-element input', test)

import random
def test():
  work = []
  for i in xrange(0, 1000):
    work.append(int(random.random() * 1000))
  example = insertion_sort(work)
  return len(example) == 1000 and is_sorted(example)
expect(test_count, 'should sort moderate-sized input', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Selection Sort Tests')
test_count = [0, 0]

def test():
  example = selection_sort([3,9,1,4,7])
  return lists_equal(example, [1,3,4,7,9])
expect(test_count, 'should sort example input', test)

def test():
  example = selection_sort([])
  return lists_equal(example, [])
expect(test_count, 'should return empty array for empty input', test)

def test():
  example = selection_sort([10])
  return lists_equal(example, [10])
expect(test_count, 'should sort single-element input', test)

import random
def test():
  work = []
  for i in xrange(0, 1000):
    work.append(int(random.random() * 1000))
  example = selection_sort(work)
  return len(example) == 1000 and is_sorted(example)
expect(test_count, 'should sort moderate-sized input', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Bubble Sort Tests')
test_count = [0, 0]

def test():
  example = bubble_sort([3,9,1,4,7])
  return lists_equal(example, [1,3,4,7,9])
expect(test_count, 'should sort example input', test)

def test():
  example = bubble_sort([])
  return lists_equal(example, [])
expect(test_count, 'should return empty array for empty input', test)

def test():
  example = bubble_sort([10])
  return lists_equal(example, [10])
expect(test_count, 'should sort single-element input', test)

import random
def test():
  work = []
  for i in xrange(0, 1000):
    work.append(int(random.random() * 1000))
  example = bubble_sort(work)
  return len(example) == 1000 and is_sorted(example)
expect(test_count, 'should sort moderate-sized input', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

