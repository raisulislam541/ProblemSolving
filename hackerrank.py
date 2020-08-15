def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True

    return leap


year = int(input())
print(is_leap(year))

# Find the Runner-Up Score!

from sys import stdin

if __name__ == '__main__':
    n = stdin.readline()
    arr = [int(x) for x in stdin.readline().split()]
    max1 = arr[0]
    max2 = -99999

    for i in range(1, len(arr)):
        if max1 < arr[i]:
            max2 = max1
            max1 = arr[i]
        elif max2 < arr[i] and arr[i] < max1:
            max2 = arr[i]

    print(max2)

