numbers = [1, 2, 3, 4, 5]

def is_even(x):
    if x % 2 == 0:
        return True
    return False

even = filter(is_even, numbers)
print(list(even))