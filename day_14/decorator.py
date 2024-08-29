# def uppercase_decorator(func):
#     def wrapper():
        
#         uppercase = func.upper()
#         return uppercase
#     return wrapper

# def split_string_decorator(func):
#     def wrapper():
#         splitted = func.split
#         return splitted
#     return wrapper

# @split_string_decorator
# @uppercase_decorator
# def greeting():
#     return 'Welcome to python'

# print(greeting())

def print_country (function):
    def wrapper(par1, par2, par3):
        function(par1, par2, par3)
        print("I live in {}".format(par3))
    return wrapper

@print_country
def print_full (first, last, country):
    print("I am {} {}.I love to teach".format(first, last, country))

print_full("Adam", "Bakeer", "Jordan")