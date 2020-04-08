
# DSA Chapter 5 - Dynamic Arrays

import sys
import ctypes

# List Length and Size
def list_length_and_size(n):
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
        data.append(None)


# Dynamic Array
class DynamicArray:

    def __init__(self):
        self._n = 0                                 # Count of actual elements.
        self._capacity = 1                          # Default array capacity.
        self._A = self._make_array(self._capacity)  # Low level array.
    
    def __len__(self):
        return self._n                              # Returns number of elements.

    def __getitem__(self, k):
        if not 0 <= k < self._n:                    # Check if the requested index.
            raise IndexError('invalid index')       # Is outside of the count of elements.
        return self._A[k]                           # Return item @ index k.

    def append(self, obj):
        if self._n == self._capacity:               # If low level array is full.
            self._resize(2 * self._capacity)        # Double size of underlying array.
        self._A[self._n] = obj                      # Store object in low level array.
        self._n += 1                                # Increment count of elements.

    def insert(self, k, value):
        if self._n == self._capacity:               # If low level array is full.
            self._resize(2 * self._capacity)        # Double size of underlying array.
        for j in range(self._n, k, -1):             # Loop from end of array to index k.
            self._A[j] = self._A[j-1]               # Shift elements to the right by 1.
        self._A[k] = value                          # Set element at index k to value.    
        self._n += 1                                # Increment number of elements.

    def remove(self, value):
        for k in range(self._n):                    # For all elements in the array.
            if self._A[k] == value:                 # If the value is equal to the element.
                for j in range(k, self._n - 1):     # For all elements to the right of index k.
                    self._A[j] = self._A[j+1]       # Shift elements to the left by 1.
                self._A[self._n - 1] = None         # Reset last element to None for garbage collection.
                self._n -= 1                        # Decrement number of elements.
                return                              # Immediately return.
            raise ValueError('value not found')

    def _resize(self, c):
        B = self._make_array(c)                     # Create new low level array with capacity c.
        for k in range(self._n):                    # For all elements in current low level array.
            B[k] = self._A[k]                       # Copy all elements over 
        self._A = B                                 # Reassign old array to new array.
        self._capacity = c                          # Set capacity to new capacity.

    def _make_array(self, c):
        return (c * ctypes.py_object)()             # Return new array with capacity c.
    

# Storing High Scores for a Game

class GameEntry:

    def __init__(self, name, score):
        self._name = name               # Member for game name.   
        self._score = score             # Member for game score.

    def get_name(self):
        return self._name               # Getter for game name.

    def get_score(self):
        return self._score              # Getter for game score.

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)


class Scoreboard:
    
    def __init__(self, capacity=10):
        self._board = [None] * capacity                                             # Initialize board wth None.
        self._n = 0                                                                 # Number of entries.

    def __getitem__(self, k):
        return self._board[k]                                                       # Return item on board.

    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        score = entry.get_score()                                                   # Retrieve score.
        good = self._n < len(self._board) or score > self._board[-1].get_score()    # If score is greater than the smallest score
        if good:                                                                    # or number of entries is less than capacity.
            if self._n < len(self._board):                                          # If number of entries is less that board capacity.
                self._n += 1                                                        # Increment # of entries.
            j = self._n - 1                                                         # Shift scores to the right.
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry                                                  # Insert new score at index j.
    

# Insertion Sort (O(n^2))
def insertion_sort(A):
    for k in range(1, len(A)):          # For all elements starting @ index 1
        cur = A[k]                      # Current value is A[k]
        j = k                           # j index = k index
        while j > 0 and A[j-1] > cur:   #
            A[j] = A[j-1]
            j -= 1
        A[j] = cur


# Caesar Cipher
class CaesarCipher:

    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)
    
    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord ('A')
                msg[k] = code[j]
        return ''.join(msg)


# Tic Tac Toe
class TicTaceToe:

    def __init__(self):
        self._board = [[' '] * 3 for j in range(3)]
        self._player = 'X'

    def mark(self, i, j):
        if not (0 <= i <= 2) and (0 <= j <= 2):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def _is_win(self, mark):
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or
                mark == board[1][0] == board[1][1] == board[1][2] or
                mark == board[2][0] == board[2][1] == board[2][2] or
                mark == board[0][0] == board[1][0] == board[2][0] or
                mark == board[0][1] == board[1][1] == board[2][1] or
                mark == board[0][2] == board[1][2] == board[2][2] or
                mark == board[0][0] == board[1][1] == board[2][2] or
                mark == board[0][2] == board[1][1] == board[2][0])

    def winner(self):
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):
        rows = ['|'.join(self._board[r] for r in range(3))]
        return '\n-----\n'.join(rows)


if __name__ == '__main__':
    print('\nList Length and Size\n--------------------')
    list_length_and_size(6)
    
    print('\nInsertion Sort\n--------------')
    arr = [3,2,11,23,52,13]
    insertion_sort(arr)
    print(arr)
