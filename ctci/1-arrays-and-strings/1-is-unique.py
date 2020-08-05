
# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?
# Hints: #44, #777, # 732

import unittest

def unique1(string):  
  seen_hash = set()
  for char in string:
    if char == ' ':
      continue
    if char in seen_hash:
      return False
    seen_hash.add(char)
  return True

def unique2(string):
  vector = [0]*128
  for char in string:
    if char == ' ':
      continue
    if vector[ord(char)]:
      return False
    else:
      vector[ord(char)] = 1
  return True

# Only works for letters a-z
def unique3(string):
  flag = 0
  for char in string:
    if char == " ":
      continue
    val = ord(char) - ord('a')
    if(flag & (1 << val) > 0):
      return False
    flag |= (1 << val)
  return True

class Test(unittest.TestCase):

  def test1_unique_set(self):
    self.assertEqual(unique1("1234567890qwertyuiopasdfghjkl;zxcvbnm,./'[]\=-!@#$%^&*()"), True)

  def test2_unique_set(self):
    self.assertEqual(unique1("  "), True)

  def test3_unique_set(self):
    self.assertEqual(unique1("hey tom"), True)

  def test1_unique_bit_vector(self):
    self.assertEqual(unique2("1234567890qwertyuiopasdfghjkl;zxcvbnm,./'[]\=-!@#$%^&*()"), True)

  def test2_unique_bit_vector(self):
    self.assertEqual(unique2("  "), True)

  def test3_unique_bit_vector(self):
    self.assertEqual(unique2("hey tom"), True)

  def test1_unique_bit(self):
    self.assertEqual(unique3("  "), True)

  def test2_unique_bit(self):
    self.assertEqual(unique3("hey tom"), True)

    
if __name__ == '__main__':
  unittest.main()
