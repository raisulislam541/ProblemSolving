# decorator


# def welcome_user(func):
#     user = input("enter your  user name: ")
#     print(f"hello, {user}")
#     func()  # calling the referenced function
#
#
# def say_hello():
#     print("welcome to my app")
#
#
# welcome_user(say_hello)  # sending the reference to the function
#
# # incomplete decorators
# def decorator():
#     def say_hello():
#         print("Welcome to my app")
#
#     return say_hello
#
#
# my_func = decorator()
# print(my_func)   # printing my_func will just show the reference  object
# my_func()  # will print the actual function


import functools


def new_decorator(func):
    @functools.wraps(func)
    def say_hello(*args, **kwargs):
        func(*args, **kwargs)

        print("Welcome to my app")

    return say_hello


@new_decorator
def welcome_user(please: str):
    user = input(f"{please} enter your  user name: ")
    print(f"hello, {user}")  # calling the referenced function


welcome_user(please="ok")
