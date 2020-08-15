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
