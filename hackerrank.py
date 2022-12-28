# # def is_leap(year):
# #     leap = False
# #
# #     # Write your logic here
# #     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
# #         leap = True
# #
# #     return leap
# #
# #
# # year = int(input())
# # print(is_leap(year))
# #
# # # Find the Runner-Up Score!
# #
# # from sys import stdin
# #
# # if __name__ == '__main__':
# #     n = stdin.readline()
# #     arr = [int(x) for x in stdin.readline().split()]
# #     max1 = arr[0]
# #     max2 = -99999
# #
# #     for i in range(1, len(arr)):
# #         if max1 < arr[i]:
# #             max2 = max1
# #             max1 = arr[i]
# #         elif max2 < arr[i] and arr[i] < max1:
# #             max2 = arr[i]
# #
# #     print(max2)
# #
# # # nested list problem
# #
# # if __name__ == '__main__':
# #     inputs = [[str(input()), float(input())] for dummy in range(int(input()))]
# #
# #     unique_score = list(set([score for name, score in inputs]))
# #     if unique_score:
# #         unique_score.sort()
# #         second_lowest = unique_score[1]
# #         students = [name for name, score in inputs
# #                     if score == second_lowest]
# #         students.sort()
# #     for i in students:
# #         print(i)
# #
# # # Finding the percentage
# #
# # if __name__ == '__main__':
# #     n = int(input())
# #     student_marks = {}
# #     for _ in range(n):
# #         name, *line = input().split()
# #         scores = list(map(float, line))
# #         student_marks[name] = scores
# #     query_name = input()
# #     values = student_marks.get(query_name)
# #     avg = 0
# #     for i in values:
# #         avg += i
# #     print("{:.2f}".format(avg/len(values)))
# #
# #
# """This module tries to explain AES GCM mode with an example."""
#
# # from Crypto.Cipher import AES
# # from base64 import b64encode
# # someKey = (b'yCDSdRHwp2yu3daAvJNrnB8x7pJgJ8Kh')
# # data = b64encode(b'This is the plain text to encrypt')
# # cipher = AES.new(someKey, AES.MODE_GCM, nonce=(b'TJQa+XTJDPoimHmZ'), mac_len=16)
# # ciphertext, tag = cipher.encrypt_and_digest(data)
# # print(ciphertext, tag)
# # ciphertext = ciphertext[16:] + tag[:16] + b64encode(b'TJQa+XTJDPoimHmZ')
# # print((b64encode(ciphertext)))
# # print((b"TJQa+XTJDPoimHmZDZvm/5CV8QJ3XDxC+6kjGpwAUvBvddPjhLKSO9lIRWHXOWExXd5DA/8WTx22bZbkDg=="))
#
# import base64
# import hashlib
#
# from Cryptodome.Cipher import AES  # from pycryptodomex v-3.10.4
# from Cryptodome.Random import get_random_bytes
#
# HASH_NAME = "SHA256"
# IV_LENGTH = 12
# ITERATION_COUNT = 65536
# KEY_LENGTH = 32
# SALT_LENGTH = 16
# TAG_LENGTH = 16
#
#
# def encrypt(password, plain_message):
#     salt = get_random_bytes(SALT_LENGTH)  # Random salt of 16 bytes
#     print((salt))
#     secret = get_secret_key(password, salt)
#     print(secret)
#
#     iv = get_random_bytes(IV_LENGTH)  # Random IV of 12 bytes
#     cipher = AES.new(secret, AES.MODE_GCM, iv)
#
#     encrypted_message_byte, tag = cipher.encrypt_and_digest(plain_message.encode("utf-8"))
#     cipher_byte = iv + salt + encrypted_message_byte + tag
#
#     encoded_cipher_byte = base64.b64encode(cipher_byte)
#     return bytes.decode(encoded_cipher_byte)
#
#
# def decrypt(password, cipher_message):
#     decoded_cipher_byte = base64.b64decode(cipher_message)
#
#     iv = decoded_cipher_byte[:IV_LENGTH]
#     salt = decoded_cipher_byte[IV_LENGTH:(IV_LENGTH + SALT_LENGTH)]
#     encrypted_message_byte = decoded_cipher_byte[(IV_LENGTH + SALT_LENGTH):-TAG_LENGTH]
#     tag = decoded_cipher_byte[-TAG_LENGTH:]
#
#     secret = get_secret_key(password, salt)
#     cipher = AES.new(secret, AES.MODE_GCM, iv)
#
#     decrypted_message_byte = cipher.decrypt_and_verify(encrypted_message_byte, tag)
#     return decrypted_message_byte.decode("utf-8")
#
#
# def get_secret_key(password, salt):
#     return hashlib.pbkdf2_hmac(HASH_NAME, password.encode(), salt, ITERATION_COUNT, KEY_LENGTH)
#
#
#
# outputFormat = "{:<25}:{}"
# secret_key = "yCDSdRHwp2yu3daAvJNrnB8x7pJgJ8Kh"
# plain_text = "This is the plain text to encrypt"
#
# print("------ AES-GCM Encryption ------")
# cipher_text = encrypt(secret_key, plain_text)
# print(outputFormat.format("encryption input", plain_text))
# print(outputFormat.format("encryption output", cipher_text))
# print(len(cipher_text))
#
# decrypted_text = decrypt(secret_key, cipher_text)
#
# print("\n------ AES-GCM Decryption ------")
# print(outputFormat.format("decryption input", cipher_text))
# print(outputFormat.format("decryption output", decrypted_text))

import csv

out_list = []
output_dict = {}
file = 'new.csv'

search = input("Search Serial number here: ")
with open(file, 'r') as my_file:
    reader = csv.reader(my_file)
    next(reader)
    for row in reader:
        if row[0] == search:
            print(f"Congratulation ! your input is {search} and match with {search}")
            for i in range(len(row)):
                print(row[i])
            out_list = [row[0], row[1], row[2]]
            output_dict = {"serial_number": row[0], "starting_code": row[1], "key": row[2]}


print(f"your input list values {out_list}\n")
print(f"your matching dictionary {output_dict}")
