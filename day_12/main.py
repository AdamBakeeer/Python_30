from mymodule import generate_full_name, sum_2, weight
print(generate_full_name('adam', 'bakeer'))
print(sum_2(2,3))
print(weight(10))

import os
os.mkdir('test_dir')
os.chdir('test_dir')
os.getcwd()
os.rmdir("test_dir")

import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))