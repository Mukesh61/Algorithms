'''
Recursion is one of the most powerful concept. repetition we can achieve using
while loop or for loop, another way is recursion.

function call itself.
- condition to stop the function like in case of factorial if n==0: return 1

import sys

def find_recursion_depth():
    current = sys.getrecursionlimit()
    sys.setrecursionlimit(current)
    print(current)

find_recursion_depth()
'''

def find_factorical(n):
    if n == 0:
        return 1
    return n * find_factorical(n-1)

print(find_factorical(5))
