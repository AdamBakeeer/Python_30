numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

numbers_squared = map(square, numbers)
print(list(numbers_squared))

numbers_squared_2 = map(lambda x:x ** 2, numbers)
print(list(numbers_squared_2))

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def upper_case(name):
    return name.upper()

names_upper = map(upper_case, names)
print(list(names_upper))