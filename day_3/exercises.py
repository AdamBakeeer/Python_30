""""
#1
age = 20
print('my age' ,age)
#2
height = 1.80 
print('my height', height ,'m')
#3
a = complex(1 + 2j)
print(a)
#4
base_in = float(input('Enter base:'))
height_in = float(input('Enter height:'))
area = 0.5 * base_in * height_in
print('the are of triangle is ', area)
#5
side_a = float(input('enter side a: '))
side_b = float(input('enter side b: '))
side_c = float(input('enter side c: '))
per = side_a + side_b + side_c 
print('the perimeter of the triangle is', per)
#6
side_d = float(input('enter len: '))
side_e = float(input('enter width: '))
area_1 = side_d * side_e
per_1 = 2 * (side_d + side_e)
print('area:', area_1 ,'perimeter', per_1)
#7
radius = float(input('enter radius: '))
area_2 = 3.14 * radius ** 2
circumfrance = 2 * 3.14 * radius
print('area:', area_2 ,'circumfrance', circumfrance)
#12
length_python = len('python')
length_dragon = len('dragon')
comparison = length_dragon != length_python
print(comparison)
#13
py = 'python'
dr = 'dragon'
sub = 'on'

if sub in py and sub in dr:
    print('present in both')

#14
sen = 'I hope this course is not full of jargon.'
subs = 'jargon'
if subs in sen:
    print('present')

#17
num = 10
div = 10 % 2
if div == 0:
    print('even')
"""

#23
rows = 5
col = 5



for i in range(1,rows+1):
    row_value = [i]
    for j in range(1,col -1):
        row_value.append(i ** (j + 1))
    print(" ".join(map(str, row_value)))


