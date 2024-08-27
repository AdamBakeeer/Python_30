def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x > 0 :
        return x
    else:
        return -(x)
    
def higher_order(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    
result = higher_order('square')
print(result(3))

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

result = add_ten()
print(result(5))