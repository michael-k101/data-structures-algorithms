# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.
# Hints: #1, #84, #122, #131
# Example: 
# 1. "ba", "ab" --> TRUE
# 2. "logan", "ol" --> FALSE
# 3. "Logan", "olgan" --> FALSE

# Input: 2 strings
# Output: bool
# ---------------------------------------------------------------------------------------
# Questions
# 1. What examples can I get? "dog!!l" != "d      og"
# 2. Can two permutations of different sizes be TRUE? No
# 3. Is it case sensitive? Yes
# 4. Do we count whitespace? Yes

# Psuedocode Algorithm
# ---------------------------------------------------------------------------------------
# Check if strings are equal sizes/lengths. If not, return false, else continue
# add every value from first string to an arrayList
# check character by character of second string is in arrayList
# if so, remove that element from arrayList
# if not, return false
# if youve iterated through entire length of second string, return true

import unittest

def unique(v1, v2):  
  seen_hash = set()
  for char in value:
    if char == ' ':
      continue
    if char in seen_hash:
      continue
    
  

class Test(unittest.TestCase):

  def test1(self):
    self.assertEqual(unique("1234567890qwertyuiopasdfghjkl;zxcvbnm,./'[]\=-!@#$%^&*()"), True)

  def test2(self):
    self.assertEqual(unique("  "), True)

  def test3(self):
    self.assertEqual(unique("hey tom"), True)

    
if __name__ == '__main__':
  unittest.main()