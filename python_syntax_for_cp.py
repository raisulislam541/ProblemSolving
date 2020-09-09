# basic method of input output
# input N
from click._compat import raw_input
from sys import stdin, stdout
import sys

n = int(raw_input())

# input of an array

arr = [int(x) for x in raw_input().split()]

# input via readline method
n = stdin.readline()

# array input similar method
arr = [int(x) for x in stdin.readline().split()]

# When you want to
# take input of list of integers given in a single line


def get_list(): return list(map(int, sys.stdin.readline().strip().split()))

# name, *line = input().split()
# The * is being used to grab additional returns from the split statement.


first, *rest = input().split()
print(first)
print(*rest)

# and ran it and typed in "hello my name is bob" It would print out
# hello
# ['my', 'name', 'is', 'bob']


# Occurrence Counter in List

