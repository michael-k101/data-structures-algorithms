# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.
# Hints: #1, #84, #122, #131

import unittest

def is_permutation(s1, s2):  
  char_count = {}
  for char in s1:
    try:
      char_count[char] += 1
    except KeyError:
      char_count[char] = 1
  for char in s2:
    try:
      char_count[char] -= 1
    except KeyError:
      return False
  for val in char_count.values():
    if val != 0:
      return False
  return True    

class Test(unittest.TestCase):

  def test1(self):
    self.assertEqual(is_permutation("aab","baa"), True)

  def test2(self):
    self.assertEqual(is_permutation("vaaa", "bddd"), False)

  def test3(self):
    self.assertEqual(is_permutation("vaaaa", "vaaaaaa"), False)

  def test4(self):
    self.assertEqual(is_permutation("aa b","ba a"), True)
    
if __name__ == '__main__':
  print(is_permutation("avaa", "vaaa"))
  # unittest.main()