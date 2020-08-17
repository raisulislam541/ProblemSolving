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

# nested list problem

if __name__ == '__main__':
    inputs = [[str(input()), float(input())] for dummy in range(int(input()))]

    unique_score = list(set([score for name, score in inputs]))
    if unique_score:
        unique_score.sort()
        second_lowest = unique_score[1]
        students = [name for name, score in inputs
                    if score == second_lowest]
        students.sort()
    for i in students:
        print(i)

# Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    values = student_marks.get(query_name)
    avg = 0
    for i in values:
        avg += i
    print("{:.2f}".format(avg/len(values)))

