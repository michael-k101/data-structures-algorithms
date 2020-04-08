
# DSA Chapter 4 - Recursion

import os


# Factorial Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# English Ruler
def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(1, 1+num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


# Binary Search
def binary_search(data, target, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


# File System
def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    return total 


# Inefficient Element Uniqueness (O(2^n))
def unique3(S, start, stop):
    if stop - start <= 1: return True
    elif not unique3(S, start, stop-1): return False
    elif not unique3(S, start+1, stop): return False
    else: return S[start] != S[stop-1]


# Inefficient Fibonacci 
def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)


# Efficient Fibonacci
def good_fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (a,b) = good_fibonacci(n-1)
        return (a+b, a)
    
# Linear Recursion
# ----------------

# Linear Sum
def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


# Reverse Sequence
def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)
        

# Computing Powers - Trivial
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * pow(x, n-1)


# Computing Powers - Fast
def power_fast(x,n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


# Binary Recursion
# ----------------

# Binary Sum
def binary_sum(S, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start+stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


# Eliminating Tail Recursion
# --------------------------

# Binary Search - Iterative
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


# Reverse - Iterative
def reverse_iterative(S):
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop-1] = S[stop - 1], S[start]
        start, stop = start + 1, stop - 1

    
if __name__ == '__main__':
    print('\nFactorial\n---------')
    print('Factorial of 5 =', factorial(5))
    print()

    print('English Ruler\n-------------')
    draw_ruler(3, 3)
    print()

    print('\nBinary Search\n-------------')
    print('Index of 3:', binary_search([1,2,3,4,5,6,7,8,9,10], 3, 0, 9)) 
    print()

    print('\nFile System\n-----------')
    print('Disk Usage of /Users/michael/Documents/dev:', disk_usage('/Users/michael/Documents/dev/') // 1000000, 'MB')
    print()

    nums1 = [1,2,3,4,5,6,7,8,9,10]
    print('\nInefficient Element Uniqueness\n------------------------------')
    print('Inefficient Uniqueness Check:', unique3(nums1, 0, 10))
    print()

    print('\nInefficient Fibonacci\n---------------------')
    print('The 4th number in the Fibonacci sequences is', bad_fibonacci(4))
    print()

    print('\nEfficient Fibonacci\n-------------------')
    print('The 10th number in the Fibonacci sequences is', good_fibonacci(10)[0])
    print()

    nums2 = [1,2,3,4,5]
    print('\nLinear Sum\n----------')
    print('The sum of 1, 2, 3, 4, and 5 is', linear_sum(nums2, 5))
    print()

    print('\nReversing a Sequence\n--------------------')
    reverse(nums2, 0, 5)
    print('1, 2, 3, 4, 5 reversed is', nums2)
    print()

    print('\nComputing Powers\n----------------')
    print('Fast:', power_fast(2,100))
    print('Trivial:', power(2, 8))
    print()

    print('\nBinary Sum\n----------')
    print('Binary Sum of [1,2,3,4,5]:', binary_sum(nums2, 0, 5))
    print()

    nums3 = [6, 7, 8, 9, 10]
    print('\nEliminating Tail Recursion (Iteration)\n--------------------------------------')
    print('Binary Search for 9 in', nums3, 'is', binary_search_iterative(nums3, 9))
    reverse_iterative(nums3)
    print('Reverse of 6, 7, 8, 9, 10', 'is', nums3)
    print()