
# DSA Chapter 3 - Algorithm Analysis

# Prefix Averages
B = [3, 4, 5, 6, 7]

# Quadratic time (O(n^2))
def prefix_average1(S):
    n = len(S)
    A = [0] * n
    for i in range(n):          # two for loops 1/2
        total = 0
        for j in range (i+1):   # two for loops 2/2
            total += S[j]
        A[j] = total / (i+1)
    return A

def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for i in range(n):
        A[i] = sum(S[0:i+1]) / (i+1)    # Sum function still requires O(i+1) time to accumulate values.
    return A


# Linear Time (O(n))
def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for i in range(n):      # one for loop
        total += S[i]
        A[i] = total / (i+1)
    return A


# Three Way Set Disjointness
a = {1, 2, 3, 4}
b = {2, 4, 5, 6}
c = {1, 5, 7, 9}
d = {1, 8, 11, 24}

# Cubic Time (O(n^2))
def disjoint1(A, B, C):
    for a in A:                     # for loop 1/3
        for b in B:                 # for loop 2/3
            for c in C:             # for loop 3/3
                if a == b == c:
                    return False
    return True


# Quadratic Time (O(n^2))
def disjoint2(A, B, C):
    for a in A:
        for b in B:
            if a == b:                  # limits the running time to O(n^2) because it short circuits 
                for c in C:             # the computation to max num of pairs between a and b. 
                    if a == c:          # Meaning, it will only run when a pair is found, which is max n times.
                        return False    # So it's n^2 + n which is O(n^2), rather than n^3 which is O(n^3)
    return True


# Element Uniqueness
R = [1, 4, 6, 2, 3, 5]


# Quadratic Time (O(n^2))
def unique1(S):
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True


# nlogn Time using Sorting
def unique2(S):
    temp = sorted(S)                # Sorts list in order and runs in O(nlogn) time
    for j in range(1, len(temp)):   # Loop runs in O(n) time
        if temp[j-1] == temp[j]:    # Total is O(nlogn)
            return False
    return True


if __name__ == '__main__':
    print("\nPrefix Averages\n---------------")
    print("\nQuadratic Time #1:\t", prefix_average1(B))
    print("\nQuadratic Time #2:\t", prefix_average2(B))
    print("\nLinear Time:\t\t", prefix_average3(B))  
    print()  

    print("\nThree Way Set Disjointness\n--------------------------")
    print("\nCubic Time:\t\t", disjoint1(a, b, c))
    print("\nQuadratic Time:\t\t", disjoint2(a, c, d))
    print()

    print("\nElement Uniqueness\n------------------")
    print("\nQuadratic Time:\t\t", unique1(R))
    print("\nnlogn Time:\t\t", unique2(R))
    print()