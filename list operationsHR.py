
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

