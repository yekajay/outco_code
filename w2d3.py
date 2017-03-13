#
#  Homework VI
#
#  Problem 1: Quicksort
#
#  Prompt:    Given an unsorted list of integers, return the list
#             sorted using quicksort.
#
#             What are the time and auxilliary space complexity?
#
#  Input:     An unsorted list of integers
#  Output:    A sorted list of integers
#
#  Example:   input = [3,9,1,4,7] , output = [1,3,4,7,9]
#
#
#  Problem 2: Mergesort
#
#  Prompt:    Given an unsorted list of integers, return the list
#             sorted using mergesort.
#
#             What are the time and auxilliary space complexity?
#
#  Input:     An unsorted list of integers
#  Output:    A sorted list of integers
#
#  Example:   input = [3,9,1,4,7] , output = [1,3,4,7,9]
#

import random

# Time Complexity: O(n log n)
# Auxiliary Space Complexity: O(log n)
def quicksort(input):
	def quicksort_partition(start_index,end_index):
		rn=random.randrange(start_index,end_index)
		input[rn],input[end_index]=input[end_index],input[rn]
		
		pivot=input[end_index]
		index=start_index
		for i in range(start_index,end_index):
			if input[i]<pivot:
				input[i],input[index]=input[index],input[i]
				index+=1
		input[index],input[end_index]=input[end_index],input[index]
		return index
	
	def quicksort_helper(start_index,end_index):
		if start_index<end_index:
			index=quicksort_partition(start_index,end_index)
			quicksort_helper(start_index,index-1)
			quicksort_helper(index+1,end_index)
		
	quicksort_helper(0,len(input)-1)
	return input



# Time Complexity: O(n log n)
# Auxiliary Space Complexity: O(n)
def mergesort(input):
	if len(input)==0:
		return input
	def mergesort_merge(left_arr,right_arr):
		result=[]
		i=0
		j=0
		while i<len(left_arr) and j<len(right_arr):
			if left_arr[i]<=right_arr[j]:
				result.append(left_arr[i])
				i+=1
			else:
				result.append(right_arr[j])
				j+=1
		while i<len(left_arr):
			result.append(left_arr[i])
			i+=1
		while j<len(right_arr):
			result.append(right_arr[j])
			j+=1
		return result
		
	def mergesort_split(arr):
		if len(arr)==1:
			return arr
		left_arr=arr[:len(arr)//2]
		right_arr=arr[len(arr)//2:]
		left_arr=mergesort_split(left_arr)
		right_arr=mergesort_split(right_arr)
		arr=mergesort_merge(left_arr,right_arr)
		return arr
	
	return mergesort_split(input)
	















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


print('Quick Sort Tests')
test_count = [0, 0]

def test():
  example = quicksort([3,9,1,4,7])
  return lists_equal(example, [1,3,4,7,9])
expect(test_count, 'should sort example input', test)

def test():
  example = quicksort([])
  return lists_equal(example, [])
expect(test_count, 'should return empty array for empty input', test)

def test():
  example = quicksort([10])
  return lists_equal(example, [10])
expect(test_count, 'should sort single-element input', test)

import random
def test():
  work = []
  for i in xrange(0, 1000):
    work.append(int(random.random() * 1000))
  example = quicksort(work)
  return len(example) == 1000 and is_sorted(example)
expect(test_count, 'should sort moderate-sized input', test)

def test():
  work = []
  for i in xrange(0, 1000000):
    work.append(int(random.random() * 1000000))
  example = quicksort(work)
  return len(example) == 1000000 and is_sorted(example)
expect(test_count, 'should sort large input', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Merge Sort Tests')
test_count = [0, 0]

def test():
  example = mergesort([3,9,1,4,7])
  return lists_equal(example, [1,3,4,7,9])
expect(test_count, 'should sort example input', test)

def test():
  example = mergesort([])
  return lists_equal(example, [])
expect(test_count, 'should return empty array for empty input', test)

def test():
  example = mergesort([10])
  return lists_equal(example, [10])
expect(test_count, 'should sort single-element input', test)

import random
def test():
  work = []
  for i in xrange(0, 1000):
    work.append(int(random.random() * 1000))
  example = mergesort(work)
  return len(example) == 1000 and is_sorted(example)
expect(test_count, 'should sort moderate-sized input', test)

def test():
  work = []
  for i in xrange(0, 1000000):
    work.append(int(random.random() * 1000000))
  example = mergesort(work)
  return len(example) == 1000000 and is_sorted(example)
expect(test_count, 'should sort large input', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


