
p = int(input())
m_lis = []
for i in range(p):
    user_input = input().split()
    command = user_input[0]
    if user_input[0] == "print":
        print(m_lis)
        print("\n")

    else:
        command += "(" + ",".join(user_input[1:]) + ")"

        eval("m_lis." + command)

#tuple

n = int(input())
integer_list = map(int, input().split())

t = tuple(integer_list)
print(hash(t))


def swap_case(s):
    return s.swapcase()


# String Split and Join

def split_and_join(line):
    return "-".join(line.split(" "))

# mutate string


def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]


def count_substring(string: str, sub_string: str):

    count = string.find(sub_string)

    return count


string = input().strip()
sub_string = input().strip()

p = count_substring(string=string, sub_string=sub_string)
print(p)
