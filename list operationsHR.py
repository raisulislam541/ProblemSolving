
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


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# String Split and Join

