
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

from cryptography.fernet import Fernet
key = 'vuJq7yG972ty1P5bGttUn5TFYmfTo8vnL7wECo9a3lk='
cipher_suite = Fernet(key)
encoded_text = cipher_suite.encrypt(b"PbLCh@")
decoded_text = cipher_suite.decrypt(encoded_text).decode('utf-8')
print(encoded_text, decoded_text)

from decouple import config
from cryptography.fernet import Fernet

key = config('KEY')
DB_PASS = config("DB_PASSWORD")

cipher_suite = Fernet(key)
decoded_text = cipher_suite.decrypt(DB_PASS.encode('utf-8')).decode('utf-8')
url = f"postgres://{config('DB_USER')}:{decoded_text}@{config('DB_HOST')}:5432/{config('DB_NAME')}"
print(url)