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


def seive_method(n: int):

    prime = [True for i in range(n+1)]
    print(prime)
    p = 2
    while p <= n:
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for i in range(2, n+1):
        if prime[i]:
            print(i)


if __name__ == '__main__':
    n = 100
    seive_method(n=n)


def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i:len(sub_string) + i] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

