# Homework I
#
# Instructions:
# List the Time and Auxiliary Space Complexity of each of the following
# functions. 


# Problem 1:
# Time Complexity: O(1)
# Auxiliary Space Complexity: O(1)

def first_times_last(arr):
  result = None
  if len(arr) < 2:
    return result
  else:
    result = arr[0] * arr[len(arr) - 1]
    return result


# Problem 2:
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(n)

def most_frequent_occurrence(str):
  lower_str = str.lower()
  letters = {}
  most_frequent = []
    
  for i in range(0, len(lower_str)):
    if lower_str[i] in letters:
      letters[lower_str[i]] += 1
    else:
      letters[lower_str[i]] = 1

  for key in letters: 
    if len(most_frequent) == 0 or letters[key] > most_frequent[1]:
      most_frequent = [key, letters[key]]

  return most_frequent[0]


# Problem 3:
# Time Complexity: O(n^2)
# Auxiliary Space Complexity: O(1)

def print_unordered_pairs(arr):
  for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
      print(str(arr[i]) + "," + str(arr[j]))


# Problem 4:
# Time Complexity: O(log n)
# Auxiliary Space Complexity: O(log n)

def sorted_list_search(sorted_list, target):
  def hunt(start, finish):
    if start > finish:
      return False
    mid = (start + finish) / 2
    if sorted_list[mid] == target:
      return True
    elif sorted_list[mid] > target:
      return hunt(start, mid-1)
    else:
      return hunt(mid + 1, finish)
  return hunt(0, len(sorted_list) - 1)


# Problem 5:
# Time Complexity: O(mn)
# Auxiliary Space Complexity: O(mn)

def make_combined_matrix(list_one, list_two): 
  result = []
  for i in range(0, len(list_one)): 
    row = []
    for j in range(0, len(list_two)): 
      row.append(list_two[j] + list_one[i])
    result.append(row)
  return result
