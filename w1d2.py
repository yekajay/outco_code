# Homework II                               
#                                                                   
# Prompt:   Given a set S, return the power set P(S), which is        
#           a set of all subsets of S.                                
#                                                                   
# Input:    A String                                                  
# Output:   An Array of String representing the power set of the input        
#                                                                   
# Example:  S = "abc", P(S) = ['', 'a', 'b','c','ab','ac','bc','abc']
#                                                                   
# Note:     The input string will not contain duplicate characters
#           The letters in the subset string must be in the same order
#           as the original input.
#           

def power_set(input):
	if len(input)==0:
		return ['']
	def power_set_helper(input_helper,index_helper):
		if index_helper<0:
			return
		power_set_helper(input_helper,index_helper-1)
		for i in range(len(power_set_helper.result)):
			tmp=power_set_helper.result[i]
			tmp+=input_helper[index_helper]
			power_set_helper.result.append(tmp)
		power_set_helper.result.append(input_helper[index_helper])
	power_set_helper.result=[]
	power_set_helper(input,len(input)-1)
	power_set_helper.result.append('')
	return power_set_helper.result
















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

# code for checking if lists contain the same elements
# (do not need to be in the same order)
def lists_matching(lst1, lst2):
  if len(lst1) != len(lst2):
    return False
  else:
    lib = {}
    for i in xrange(0, len(lst1)):
      lib[lst1[i]] = True
    for j in xrange(0, len(lst2)):
      if lib[lst2[j]] == None:
        return False
    return True

print('Power Set Tests')
test_count = [0, 0]

def test():
  example = power_set('abc')
  return lists_matching(example, ['','a','b','c','ab','bc','ab','abc'])
expect(test_count, 'should work on example input', test)

def test():
  example = power_set('')
  return lists_matching(example, [''])
expect(test_count, 'should work on empty input', test)

def test():
  example = power_set('ab')
  return lists_matching(example, ['','a','b','ab'])
expect(test_count, 'should work on two-letter input', test)

def test():
  example = power_set('abcdefg')
  return lists_matching(example, [ '','g','f','fg','e','eg','ef','efg','d',
    'dg','df','dfg','de','deg','def','defg','c','cg','cf','cfg','ce','ceg',
    'cef','cefg','cd','cdg','cdf','cdfg','cde','cdeg','cdef','cdefg','b','bg',
    'bf','bfg','be','beg','bef','befg','bd','bdg','bdf','bdfg','bde','bdeg',
    'bdef','bdefg','bc','bcg','bcf','bcfg','bce','bceg','bcef','bcefg','bcd',
    'bcdg','bcdf','bcdfg','bcde','bcdeg','bcdef','bcdefg','a','ag','af','afg',
    'ae','aeg','aef','aefg','ad','adg','adf','adfg','ade','adeg','adef',
    'adefg','ac','acg','acf','acfg','ace','aceg','acef','acefg','acd','acdg',
    'acdf','acdfg','acde','acdeg','acdef','acdefg','ab','abg','abf','abfg',
    'abe','abeg','abef','abefg','abd','abdg','abdf','abdfg','abde','abdeg',
    'abdef','abdefg','abc','abcg','abcf','abcfg','abce','abceg','abcef',
    'abcefg','abcd','abcdg','abcdf','abcdfg','abcde','abcdeg','abcdef','abcdefg' ])
expect(test_count, 'should work on longer input', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

