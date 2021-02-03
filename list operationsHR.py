#
# p = int(input())
# m_lis = []
# for i in range(p):
#     user_input = input().split()
#     command = user_input[0]
#     if user_input[0] == "print":
#         print(m_lis)
#         print("\n")
#
#     else:
#         command += "(" + ",".join(user_input[1:]) + ")"
#
#         eval("m_lis." + command)
#
# #tuple
#
# n = int(input())
# integer_list = map(int, input().split())
#
# t = tuple(integer_list)
# print(hash(t))
#
#
# def swap_case(s):
#     return s.swapcase()
#
#
# # String Split and Join
#
# def split_and_join(line):
#     return "-".join(line.split(" "))
#
# # mutate string
#
#
# def mutate_string(string, position, character):
#     return string[:position] + character + string[position+1:]
#
#
# def count_substring(string: str, sub_string: str):
#
#     count = string.find(sub_string)
#
#     return count
#
#
# string = input().strip()
# sub_string = input().strip()
#
# p = count_substring(string=string, sub_string=sub_string)
# print(p)
# #
from cryptography.fernet import Fernet
import configobj

config = configobj.ConfigObj('db.env')
index = config['DB_PASSWORD']
print(index)

key = 'vuJq7yG972ty1P5bGttUn5TFYmfTo8vnL7wECo9a3lk='
cipher_suite = Fernet(key)
encoded_text = cipher_suite.encrypt(b"adada23343$#$#").decode('utf-8')
print(encoded_text)

with open("db.env", "w") as f:
    f.write(f"DB_PASSWORD={encoded_text}")
from decouple import config
from cryptography.fernet import Fernet

key = config('KEY')

cipher_suite = Fernet(key)
DB_USER = config('DB_USER')
DB_HOST = config("DB_HOST")
DB_NAME = config('DB_NAME')
config = configobj.ConfigObj('db.env')
index = config['DB_PASSWORD']

decoded_text = cipher_suite.decrypt(index.encode('utf-8')).decode('utf-8')

url = f"postgres://{DB_USER}:{decoded_text}@{DB_HOST}:5432/{DB_NAME}"
print(url)
#



