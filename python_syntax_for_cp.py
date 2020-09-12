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

from collections import Counter


def main():
        num_lst = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
        cnt = Counter(num_lst)
        print(dict(cnt))

# first two most occurences

        print(dict(cnt.most_common(2)))


if __name__ == "__main__":
    main()

# Powerful One-Liner

salary = 4000

if salary > 9000:
    tax = 900
elif 3000 < salary < 9000:
    tax = 100
else:
    tax = 0

print(f"Tax to pay : ${tax}")

tax = 900 if salary > 9000 else 100 if 3000 < salary < 5000 else 0

print(f"Tax to pay : ${tax}")

# Check All Chars Uppercase

import string

def is_upper(word):
    return all(c in string.ascii_uppercase for c in list(word))

print(is_upper('HUMANBEING'))
print(is_upper('humanbeing'))

# Loop With Index

lst = ['a', 'b', 'c', 'd']
for index, value in enumerate(lst):
    print(f"{index}, {value}")

for index, value in enumerate(lst, start=10):
    print(f"{index}, {value}")

# Loop Over Multiple Lists at the Same Time
colors = ["red", "green", "yellow", "blue"]
codes = [1, 2, 3, 4]
for color, code in zip(colors, codes):
    print(f"{color}, {code}")


from itertools import zip_longest

colors = ["red", "green", "yellow", "blue"]
codes = [1, 2, 3, 4, 5, 6]

for color, code in zip_longest(colors, codes):
    print(f"{color}, {code}")
# we can fill the empty values with default value like the folowing
for color, code in zip_longest(colors, codes, fillvalue="nothing"):
    print(f"{color}, {code}")

# Transpose 2D Array
chars = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*chars)
print(list(transposed))
chars = [['a', 'b'], ['c', 'd'], ['e', 'f', 'g', 'h']]
transposed = zip_longest(*chars)
print(list(transposed))

# accumulate()

# itertools.accumulate(iterable[, func])

import itertools
import operator
data = [1, 2, 3, 4, 5]
result = list(itertools.accumulate(data, operator.add))
print(result)

# Join String and List Together

str1 = "do"
str2 = "more"
lst = ["Write", "less", "code"]

str3 = ' '.join(lst) + ', ' + str1 + ' ' + str2
print(str3)

# Convert List to Comma Separated String

fruits = ['apple', 'mango', 'orange']
print(','.join(fruits))
numbers = [1, 2, 3, 4, 5]
print(','.join(map(str,numbers)))
items = [1, 'apple', 2, 3, 'orange']
print(', '.join(map(str, items)))

# Flatten Nested List
import itertools
Flatten = lambda x: list(itertools.chain.from_iterable(x))

s = [['Every', 'piece of'], ['software written today is', 'likely'], ['going to'], ['infringe on', "someone else’s", 'patent.']]
print(' '.join(Flatten(s)))

# Calling Different Functions With the Same Arguments Based on Conditions


def product(a, b):
    return a*b


def add(a, b):
    return a+b


c = True

print((product if c else add)(5, 6))

# Sort Dictionary
from operator import itemgetter

d = {'a': 10, 'b': 20, 'c': 5, 'd': 8, 'e': 5}
# sort by value
print(sorted(d.items(), key=lambda x: x[1]))
# sort by key
print(sorted(d.items(), key=itemgetter(0)))
# sort by value and return keys
print(sorted(d, key=d.get))

# Remove Duplicates From List

lst = [7, 3, 3, 5, 6, 5]
# removes duplicates but does not preserves the list order
no_dups = list(set(lst))
print(no_dups)

# removes duplicates and preserves the list order
from collections import OrderedDict
no_dups = list(OrderedDict.fromkeys(lst).keys())
print(no_dups)
